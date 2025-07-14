#!/usr/bin/env python3
"""
Modern Chatbot using ChatterBot library
A supplement to the existing ELIZA chatbot

This implementation leverages the ChatterBot library to create a more sophisticated
conversational AI that can learn from training data and adapt its responses.
"""

import logging
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from chatterbot.response_selection import get_random_response
import time

# Configure logging for debugging and monitoring chatbot behavior
logging.basicConfig(level=logging.INFO)

class ModernChatbot:
    """
    Advanced chatbot implementation using ChatterBot framework
    
    This class provides a modern alternative to the classic ELIZA chatbot,
    featuring machine learning capabilities, corpus training, and adaptive responses.
    """
    
    def __init__(self, name="ModernBot"):
        """
        Initialize the modern chatbot with ChatterBot configuration
        
        Args:
            name (str): Name identifier for the chatbot instance
        """
        self.name = name
        
        # Configure ChatterBot with logic adapters for intelligent response selection
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
        
        # Initialize training components for knowledge acquisition
        self.corpus_trainer = ChatterBotCorpusTrainer(self.chatbot)
        self.list_trainer = ListTrainer(self.chatbot)
        
        print(f"🤖 {self.name} initialized successfully!")
    
    def train_with_corpus(self):
        """
        Train the chatbot using English corpus data for general conversation skills
        
        This method loads and processes the ChatterBot English corpus to provide
        the chatbot with a foundation of conversational patterns and responses.
        """
        print("📚 Training with English corpus...")
        try:
            self.corpus_trainer.train("chatterbot.corpus.english")
            print("✅ Training completed!")
        except Exception as e:
            print(f"⚠️  Training error: {e}")
    
    def train_with_custom_data(self, conversations):
        """
        Train the chatbot with domain-specific conversation data
        
        Args:
            conversations (list): List of conversation pairs for specialized training
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
        Generate contextual response based on user input
        
        Args:
            user_input (str): User's message to process
            
        Returns:
            str: Bot's generated response or error message
        """
        try:
            response = self.chatbot.get_response(user_input)
            return str(response)
        except Exception as e:
            return f"Sorry, I encountered an error: {e}"
    
    def chat_loop(self):
        """
        Interactive conversation loop with user interface
        
        Provides a command-driven interface where users can:
        - Have natural conversations with the bot
        - Trigger retraining with 'train' command
        - Check bot status with 'status' command
        - Exit gracefully with quit commands
        """
        print(f"\n{self.name}: Hello! I'm a modern chatbot. How can I help you today?")
        print("(Type 'quit' to exit, 'train' to retrain, 'status' for info)\n")
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                # Handle exit commands
                if user_input.lower() in ['quit', 'exit', 'bye']:
                    print(f"{self.name}: Goodbye! It was nice chatting with you!")
                    break
                
                # Handle training command
                elif user_input.lower() == 'train':
                    print(f"{self.name}: Starting training...")
                    self.train_with_corpus()
                    continue
                
                # Handle status command
                elif user_input.lower() == 'status':
                    print(f"{self.name}: I'm {self.name}, a modern chatbot powered by ChatterBot!")
                    print(f"Database: {len(self.chatbot.storage.filter())} statements")
                    continue
                
                # Skip empty input
                elif not user_input:
                    continue
                
                # Generate and display response
                response = self.get_response(user_input)
                print(f"{self.name}: {response}")
                
            except KeyboardInterrupt:
                print(f"\n{self.name}: Goodbye! Thanks for chatting!")
                break
            except Exception as e:
                print(f"{self.name}: Sorry, something went wrong: {e}")

def create_sample_conversations():
    """
    Create specialized conversation datasets for custom training
    
    Returns:
        list: Structured conversation pairs for domain-specific training
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
    Main execution function for the modern chatbot application
    
    Initializes the chatbot, performs training, and launches the interactive
    conversation interface.
    """
    print("🚀 Starting Modern Chatbot...")
    
    # Create chatbot instance with default configuration
    bot = ModernChatbot("ModernBot")
    
    # Perform initial training with English corpus
    bot.train_with_corpus()
    
    # Enhance with custom conversation patterns
    custom_conversations = create_sample_conversations()
    bot.train_with_custom_data(custom_conversations)
    
    # Launch interactive conversation interface
    bot.chat_loop()

if __name__ == "__main__":
    main() 