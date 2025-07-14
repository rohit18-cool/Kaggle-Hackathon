#!/usr/bin/env python3
"""
Modern Chatbot using ChatterBot library
A supplement to the existing ELIZA chatbot that uses machine learning
to generate more sophisticated and contextually appropriate responses.
"""

import logging
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from chatterbot.response_selection import get_random_response
import time

# Configure logging for debugging and monitoring training progress
logging.basicConfig(level=logging.INFO)

class ModernChatbot:
    """
    A modern chatbot implementation using the ChatterBot library.
    Provides machine learning-based conversation capabilities with
    customizable training and response selection.
    """
    
    def __init__(self, name="ModernBot"):
        """
        Initialize the modern chatbot with ChatterBot configuration.
        
        Args:
            name (str): Name identifier for the chatbot instance
        """
        self.name = name
        
        # Initialize ChatterBot with optimized configuration
        self.chatbot = ChatBot(
            name,
            # Logic adapters determine how the bot selects responses
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'default_response': 'I am not sure how to respond to that.',
                    'maximum_similarity_threshold': 0.90  # Minimum confidence for response selection
                }
            ],
            # Response selection method for choosing from multiple valid responses
            response_selection_method=get_random_response,
            read_only=False  # Allow the bot to learn from conversations
        )
        
        # Initialize trainers for different types of learning
        self.corpus_trainer = ChatterBotCorpusTrainer(self.chatbot)  # For structured language data
        self.list_trainer = ListTrainer(self.chatbot)  # For custom conversation pairs
        
        print(f"🤖 {self.name} initialized successfully!")
    
    def train_with_corpus(self):
        """
        Train the chatbot using the English corpus dataset.
        This provides the bot with general language understanding and
        common conversation patterns.
        """
        print("📚 Training with English corpus...")
        try:
            # Train using the built-in English corpus (conversations, greetings, etc.)
            self.corpus_trainer.train("chatterbot.corpus.english")
            print("✅ Training completed!")
        except Exception as e:
            print(f"⚠️  Training error: {e}")
    
    def train_with_custom_data(self, conversations):
        """
        Train the chatbot with custom conversation data.
        Useful for domain-specific knowledge or personalized responses.
        
        Args:
            conversations (list): List of conversation pairs for training
        """
        print("🎯 Training with custom data...")
        try:
            # Train on each conversation sequence
            for conversation in conversations:
                self.list_trainer.train(conversation)
            print("✅ Custom training completed!")
        except Exception as e:
            print(f"⚠️  Custom training error: {e}")
    
    def get_response(self, user_input):
        """
        Generate a response to user input using the trained model.
        
        Args:
            user_input (str): The user's message
            
        Returns:
            str: The bot's generated response
        """
        try:
            # Get response from ChatterBot's trained model
            response = self.chatbot.get_response(user_input)
            return str(response)
        except Exception as e:
            return f"Sorry, I encountered an error: {e}"
    
    def chat_loop(self):
        """
        Main interactive conversation loop.
        Handles user input, generates responses, and provides
        special commands for training and status information.
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
                    # Display database statistics
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
    Create sample conversation data for custom training.
    These examples help the bot learn specific response patterns
    and improve its conversational abilities.
    
    Returns:
        list: List of conversation sequences for training
    """
    return [
        # Conversation 1: Greeting and general help
        [
            "Hello",
            "Hi there! How are you doing?",
            "I'm doing great, thanks!",
            "That's wonderful to hear!",
            "What can you help me with?",
            "I can help you with various topics, answer questions, or just chat!"
        ],
        # Conversation 2: Weather inquiry (with limitation acknowledgment)
        [
            "What's the weather like?",
            "I don't have access to real-time weather data, but I'd be happy to chat about other topics!",
            "That's okay",
            "Is there anything else you'd like to talk about?"
        ],
        # Conversation 3: Joke request
        [
            "Tell me a joke",
            "Why don't scientists trust atoms? Because they make up everything! 😄",
            "That's funny!",
            "I'm glad you liked it! Do you have any other questions?"
        ]
    ]

def main():
    """
    Main function to initialize and run the modern chatbot.
    Sets up training data and starts the interactive conversation.
    """
    print("🚀 Starting Modern Chatbot...")
    
    # Create chatbot instance
    bot = ModernChatbot("ModernBot")
    
    # Train with general English corpus data
    bot.train_with_corpus()
    
    # Train with custom conversation examples
    custom_conversations = create_sample_conversations()
    bot.train_with_custom_data(custom_conversations)
    
    # Start interactive conversation loop
    bot.chat_loop()

if __name__ == "__main__":
    main() 