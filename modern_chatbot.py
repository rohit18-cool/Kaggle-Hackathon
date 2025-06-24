#!/usr/bin/env python3
"""
Modern Chatbot using ChatterBot library
A supplement to the existing ELIZA chatbot
"""

import logging
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from chatterbot.response_selection import get_random_response
import time

# Configure logging
logging.basicConfig(level=logging.INFO)

class ModernChatbot:
    def __init__(self, name="ModernBot"):
        """
        Initialize the modern chatbot using ChatterBot library
        """
        self.name = name
        self.chatbot = ChatBot(
            name,
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'default_response': 'I am not sure how to respond to that.',
                    'maximum_similarity_threshold': 0.90
                }
            ],
            response_selection_method=get_random_response,
            read_only=False
        )
        
        # Initialize trainers
        self.corpus_trainer = ChatterBotCorpusTrainer(self.chatbot)
        self.list_trainer = ListTrainer(self.chatbot)
        
        print(f"🤖 {self.name} initialized successfully!")
    
    def train_with_corpus(self):
        """
        Train the chatbot with English corpus data
        """
        print("📚 Training with English corpus...")
        try:
            self.corpus_trainer.train("chatterbot.corpus.english")
            print("✅ Training completed!")
        except Exception as e:
            print(f"⚠️  Training error: {e}")
    
    def train_with_custom_data(self, conversations):
        """
        Train the chatbot with custom conversation data
        
        Args:
            conversations (list): List of conversation pairs
        """
        print("🎯 Training with custom data...")
        try:
            for conversation in conversations:
                self.list_trainer.train(conversation)
            print("✅ Custom training completed!")
        except Exception as e:
            print(f"⚠️  Custom training error: {e}")
    
    def get_response(self, user_input):
        """
        Get a response from the chatbot
        
        Args:
            user_input (str): User's message
            
        Returns:
            str: Bot's response
        """
        try:
            response = self.chatbot.get_response(user_input)
            return str(response)
        except Exception as e:
            return f"Sorry, I encountered an error: {e}"
    
    def chat_loop(self):
        """
        Main chat loop for interactive conversation
        """
        print(f"\n{self.name}: Hello! I'm a modern chatbot. How can I help you today?")
        print("(Type 'quit' to exit, 'train' to retrain, 'status' for info)\n")
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'bye']:
                    print(f"{self.name}: Goodbye! It was nice chatting with you!")
                    break
                
                elif user_input.lower() == 'train':
                    print(f"{self.name}: Starting training...")
                    self.train_with_corpus()
                    continue
                
                elif user_input.lower() == 'status':
                    print(f"{self.name}: I'm {self.name}, a modern chatbot powered by ChatterBot!")
                    print(f"Database: {len(self.chatbot.storage.filter())} statements")
                    continue
                
                elif not user_input:
                    continue
                
                # Get and display response
                response = self.get_response(user_input)
                print(f"{self.name}: {response}")
                
            except KeyboardInterrupt:
                print(f"\n{self.name}: Goodbye! Thanks for chatting!")
                break
            except Exception as e:
                print(f"{self.name}: Sorry, something went wrong: {e}")

def create_sample_conversations():
    """
    Create sample conversations for custom training
    """
    return [
        [
            "Hello",
            "Hi there! How are you doing?",
            "I'm doing great, thanks!",
            "That's wonderful to hear!",
            "What can you help me with?",
            "I can help you with various topics, answer questions, or just chat!"
        ],
        [
            "What's the weather like?",
            "I don't have access to real-time weather data, but I'd be happy to chat about other topics!",
            "That's okay",
            "Is there anything else you'd like to talk about?"
        ],
        [
            "Tell me a joke",
            "Why don't scientists trust atoms? Because they make up everything! 😄",
            "That's funny!",
            "I'm glad you liked it! Do you have any other questions?"
        ]
    ]

def main():
    """
    Main function to run the modern chatbot
    """
    print("🚀 Starting Modern Chatbot...")
    
    # Create chatbot instance
    bot = ModernChatbot("ModernBot")
    
    # Train with corpus data
    bot.train_with_corpus()
    
    # Train with custom conversations
    custom_conversations = create_sample_conversations()
    bot.train_with_custom_data(custom_conversations)
    
    # Start chat loop
    bot.chat_loop()

if __name__ == "__main__":
    main() 