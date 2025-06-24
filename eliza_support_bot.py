#!/usr/bin/env python3
"""
Aliza Support Bot
A specialized customer support chatbot for handling support queries and FAQs
"""

import re
import random
import json
import datetime
from typing import Dict, List, Optional

class ElizaSupportBot:
    def __init__(self):
        """Initialize Aliza Support Bot with support-specific knowledge"""
        self.name = "Aliza"
        self.user_name = "Customer"
        self.conversation_history = []
        self.support_tickets = {}
        self.ticket_counter = 1000
        
        # Support categories and responses
        self.support_knowledge = {
            "account": {
                "keywords": ["account", "login", "password", "sign up", "register", "profile"],
                "responses": [
                    "I can help you with account-related issues. What specific problem are you experiencing?",
                    "For account issues, I can assist with login problems, password resets, and account creation.",
                    "Let me help you with your account. Are you having trouble logging in or creating an account?"
                ],
                "faqs": {
                    "how to reset password": "To reset your password, go to the login page and click 'Forgot Password'. You'll receive an email with reset instructions.",
                    "how to create account": "To create an account, visit our signup page and fill in your details. You'll need a valid email address.",
                    "account locked": "If your account is locked, please contact our security team at security@company.com or call 1-800-SUPPORT."
                }
            },
            "billing": {
                "keywords": ["billing", "payment", "invoice", "charge", "subscription", "refund", "money"],
                "responses": [
                    "I can help you with billing and payment questions. What would you like to know?",
                    "For billing issues, I can assist with payments, invoices, and subscription management.",
                    "Let me help you with your billing inquiry. Are you looking for payment information or have a billing question?"
                ],
                "faqs": {
                    "how to pay": "You can pay through our website using credit card, PayPal, or bank transfer. Go to Billing > Payment Methods.",
                    "refund policy": "We offer a 30-day money-back guarantee. Contact billing@company.com for refund requests.",
                    "subscription renewal": "Your subscription will automatically renew unless cancelled 7 days before the renewal date."
                }
            },
            "technical": {
                "keywords": ["error", "bug", "not working", "broken", "crash", "technical", "problem"],
                "responses": [
                    "I can help you troubleshoot technical issues. Can you describe what's happening?",
                    "For technical problems, I'll need some details to help you effectively. What error are you seeing?",
                    "Let me help you resolve this technical issue. What specific problem are you experiencing?"
                ],
                "faqs": {
                    "app not loading": "Try clearing your browser cache and cookies. If the problem persists, try a different browser.",
                    "slow performance": "Check your internet connection and close unnecessary browser tabs. Clear cache if needed.",
                    "error messages": "Please share the exact error message you're seeing so I can provide specific help."
                }
            },
            "product": {
                "keywords": ["product", "feature", "how to", "tutorial", "guide", "help"],
                "responses": [
                    "I can help you learn about our products and features. What would you like to know?",
                    "For product questions, I can provide information about features, tutorials, and usage guides.",
                    "Let me help you with product information. What specific feature or product are you asking about?"
                ],
                "faqs": {
                    "how to use": "Check our Help Center for detailed tutorials and guides. You can also watch our video tutorials.",
                    "feature availability": "Feature availability depends on your subscription plan. Check your plan details in your account.",
                    "product updates": "We regularly update our products. Check our blog for the latest features and improvements."
                }
            }
        }
        
        # Greeting messages
        self.greetings = [
            f"Hello! I'm {self.name}, your customer support assistant. How can I help you today?",
            f"Hi there! I'm {self.name}, here to assist you with any questions or issues you might have.",
            f"Welcome! I'm {self.name}, your dedicated support specialist. What can I help you with today?",
            f"Good day! I'm {self.name}, ready to provide you with excellent customer support. How may I assist you?"
        ]
        
        # Escalation responses
        self.escalation_responses = [
            "I understand this is important. Let me connect you with a human specialist who can better assist you.",
            "This requires specialized attention. I'll transfer you to our expert team right away.",
            "For this complex issue, let me get you in touch with one of our senior support representatives.",
            "I want to ensure you get the best possible help. Let me escalate this to our specialist team."
        ]
        
        print(f"🤖 {self.name} Support Bot initialized and ready to help!")
    
    def get_user_name(self):
        """Get and store the user's name"""
        response = input(f"{self.name}: What's your name? ")
        if response.strip():
            self.user_name = response.strip()
            return f"Nice to meet you, {self.user_name}! How can I help you today?"
        return "How can I help you today?"
    
    def classify_intent(self, user_input: str) -> str:
        """Classify user intent based on keywords"""
        user_input_lower = user_input.lower()
        
        for category, data in self.support_knowledge.items():
            for keyword in data["keywords"]:
                if keyword in user_input_lower:
                    return category
        
        return "general"
    
    def get_faq_response(self, user_input: str, category: str) -> Optional[str]:
        """Check if user input matches any FAQ and return appropriate response"""
        user_input_lower = user_input.lower()
        
        if category in self.support_knowledge:
            faqs = self.support_knowledge[category]["faqs"]
            for question, answer in faqs.items():
                if any(word in user_input_lower for word in question.split()):
                    return answer
        
        return None
    
    def create_support_ticket(self, issue_description: str) -> str:
        """Create a support ticket for the user"""
        self.ticket_counter += 1
        ticket_id = f"TICKET-{self.ticket_counter}"
        
        self.support_tickets[ticket_id] = {
            "user_name": self.user_name,
            "issue": issue_description,
            "created_at": datetime.datetime.now().isoformat(),
            "status": "open"
        }
        
        return f"I've created a support ticket for you: {ticket_id}. Our team will review your issue and get back to you within 24 hours."
    
    def should_escalate(self, user_input: str) -> bool:
        """Determine if the issue should be escalated to human support"""
        escalation_keywords = [
            "urgent", "emergency", "critical", "broken", "not working", 
            "frustrated", "angry", "complaint", "escalate", "manager",
            "human", "speak to someone", "real person"
        ]
        
        user_input_lower = user_input.lower()
        return any(keyword in user_input_lower for keyword in escalation_keywords)
    
    def get_response(self, user_input: str) -> str:
        """Generate appropriate response based on user input"""
        # Store conversation
        self.conversation_history.append({"user": user_input, "timestamp": datetime.datetime.now()})
        
        # Check for exit commands
        if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
            return f"Thank you for contacting {self.name} Support! Have a great day, {self.user_name}!"
        
        # Check for help command
        if user_input.lower() in ['help', 'commands', 'what can you do']:
            return self.get_help_message()
        
        # Check for ticket status
        if "ticket" in user_input.lower() and any(char.isdigit() for char in user_input):
            return self.get_ticket_status(user_input)
        
        # Check for escalation
        if self.should_escalate(user_input):
            return random.choice(self.escalation_responses) + " Please hold while I connect you..."
        
        # Classify intent
        intent = self.classify_intent(user_input)
        
        # Check for FAQ match
        faq_response = self.get_faq_response(user_input, intent)
        if faq_response:
            return faq_response
        
        # Get category-specific response
        if intent in self.support_knowledge:
            responses = self.support_knowledge[intent]["responses"]
            return random.choice(responses)
        
        # General response
        general_responses = [
            "I understand you need help. Could you please provide more details about your issue?",
            "I'm here to help! Can you tell me more about what you're experiencing?",
            "Let me assist you with that. What specific problem are you facing?",
            "I want to make sure I can help you effectively. Could you elaborate on your issue?"
        ]
        
        return random.choice(general_responses)
    
    def get_help_message(self) -> str:
        """Return help information"""
        return f"""
I'm {self.name}, your customer support assistant! Here's what I can help you with:

📋 **Support Categories:**
• Account issues (login, password, registration)
• Billing and payments
• Technical problems
• Product questions and features

🎫 **Commands:**
• "help" - Show this help message
• "create ticket" - Create a support ticket
• "ticket status" - Check ticket status
• "quit" - End conversation

💡 **Tips:**
• Be specific about your issue for better assistance
• I can create support tickets for complex issues
• For urgent matters, I'll escalate to human support

How can I assist you today, {self.user_name}?
"""
    
    def get_ticket_status(self, user_input: str) -> str:
        """Get status of a support ticket"""
        # Extract ticket number from input
        ticket_match = re.search(r'TICKET-(\d+)', user_input.upper())
        if ticket_match:
            ticket_id = f"TICKET-{ticket_match.group(1)}"
            if ticket_id in self.support_tickets:
                ticket = self.support_tickets[ticket_id]
                return f"Ticket {ticket_id} status: {ticket['status'].title()}. Created on {ticket['created_at'][:10]}"
            else:
                return f"Ticket {ticket_id} not found. Please check the ticket number."
        return "Please provide a valid ticket number (e.g., TICKET-1001)"
    
    def chat_loop(self):
        """Main chat loop for Aliza Support Bot"""
        print(f"\n{self.name}: {random.choice(self.greetings)}")
        
        # Get user name if not set
        if self.user_name == "Customer":
            name_response = self.get_user_name()
            print(f"{self.name}: {name_response}")
        
        print(f"\n{self.name}: You can type 'help' anytime to see what I can do, or 'quit' to end our conversation.\n")
        
        while True:
            try:
                user_input = input(f"{self.user_name}: ").strip()
                
                if not user_input:
                    continue
                
                # Get response
                response = self.get_response(user_input)
                print(f"{self.name}: {response}")
                
                # Offer to create ticket for complex issues
                if len(self.conversation_history) > 3 and "ticket" not in user_input.lower():
                    print(f"{self.name}: Would you like me to create a support ticket for this issue? (yes/no)")
                    ticket_response = input(f"{self.user_name}: ").strip().lower()
                    if ticket_response in ['yes', 'y', 'create ticket']:
                        ticket_message = self.create_support_ticket(user_input)
                        print(f"{self.name}: {ticket_message}")
                
            except KeyboardInterrupt:
                print(f"\n{self.name}: Thank you for contacting {self.name} Support! Goodbye!")
                break
            except Exception as e:
                print(f"{self.name}: I apologize, but I encountered an error. Please try again or contact human support.")

def main():
    """Main function to run Aliza Support Bot"""
    print("🚀 Starting Aliza Support Bot...")
    
    # Create and start the bot
    aliza = AlizaSupportBot()
    aliza.chat_loop()

if __name__ == "__main__":
    main() 