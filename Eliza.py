#!/usr/bin/env python3
"""
ELIZA - Classic Rule-based Chatbot
A Python implementation of the original ELIZA chatbot (1966) by Joseph Weizenbaum.
Uses pattern matching and pronoun reflection to simulate therapeutic conversation.
"""

import re
import random

# Dictionary mapping first-person pronouns to second-person equivalents
# This enables the chatbot to "reflect" user statements back as questions
reflections = {
    "am": "are",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "are": "am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

def reflect(fragment):
    """
    Transform first-person pronouns to second-person in a text fragment.
    This creates the illusion that ELIZA is asking about the user's own statements.
    
    Args:
        fragment (str): Text fragment to transform
        
    Returns:
        str: Fragment with pronouns reflected
    """
    tokens = fragment.lower().split()
    reflected = [reflections.get(word, word) for word in tokens]
    return ' '.join(reflected)

# Pattern-response pairs defining ELIZA's conversation rules
# Each tuple contains: (regex pattern, list of possible responses)
patterns = [
    # Pattern: User expresses a need
    (r'I need (.*)',
     ["Why do you need {0}?",
      "Would it really help you to get {0}?",
      "Are you sure you need {0}?"]),

    # Pattern: User asks why ELIZA doesn't do something
    (r'Why don\'?t you ([^\?]*)\??',
     ["Do you really think I don't {0}?",
      "Perhaps eventually I will {0}.",
      "Do you really want me to {0}?"]),

    # Pattern: User asks why they can't do something
    (r'Why can\'?t I ([^\?]*)\??',
     ["Do you think you should be able to {0}?",
      "If you could {0}, what would you do?",
      "I don't know -- why can't you {0}?",
      "Have you really tried?"]),

    # Pattern: User expresses inability
    (r'I can\'?t (.*)',
     ["How do you know you can't {0}?",
      "Perhaps you could {0} if you tried.",
      "What would it take for you to {0}?"]),

    # Pattern: User describes their state with "I am"
    (r'I am (.*)',
     ["Did you come to me because you are {0}?",
      "How long have you been {0}?",
      "How do you feel about being {0}?"]),

    # Pattern: User describes their state with "I'm"
    (r'I\'?m (.*)',
     ["Why are you {0}?",
      "How does being {0} make you feel?",
      "Do you enjoy being {0}?"]),

    # Pattern: User mentions mother
    (r'(.*) mother(.*)',
     ["Tell me more about your mother.",
      "What was your relationship with your mother like?",
      "How do you feel about your mother?"]),

    # Pattern: Greeting
    (r'Hello(.*)',
     ["Hello... I'm glad you could drop by today.",
      "Hi there... how are you today?",
      "Hello, how are you feeling today?"]),

    # Pattern: Exit command
    (r'Quit',
     ["Thank you for talking with me.",
      "Goodbye.",
      "Have a great day!"]),

    # Default pattern: Catch-all for unmatched input
    (r'(.*)',
     ["Please tell me more.",
      "Let's change focus a bit... Tell me about your family.",
      "Can you elaborate on that?",
      "Why do you say that {0}?",
      "I see.",
      "Very interesting.",
      "{0}.",
      "I see. And what does that tell you?",
      "How does that make you feel?",
      "How do you feel when you say that?"])
]

def eliza_chat():
    """
    Main conversation loop for ELIZA chatbot.
    Processes user input through pattern matching and generates appropriate responses.
    """
    print("ELIZA: Hello. How are you feeling today?")
    
    while True:
        user_input = input("YOU: ")
        
        # Check for exit commands
        if user_input.lower() in ['quit', 'exit']:
            print("ELIZA: Goodbye. Take care!")
            break
        
        # Process input through pattern matching
        for pattern, responses in patterns:
            match = re.match(pattern, user_input, re.IGNORECASE)
            if match:
                # Select random response from available options
                response = random.choice(responses)
                
                # Extract captured groups and apply pronoun reflection
                groups = match.groups()
                reflected_groups = [reflect(g) for g in groups]
                
                # Format response with reflected pronouns
                print("ELIZA:", response.format(*reflected_groups))
                break

if __name__ == "__main__":
    eliza_chat()