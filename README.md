# Kaggle-Hackathon

A Python chatbot project featuring classic, modern, and specialized chatbot implementations.

## 🤖 Chatbots Included

### 1. ELIZA (Classic Rule-based)
- **File**: `Eliza.py`
- **Type**: Pattern-matching rule-based chatbot
- **Features**: 
  - Classic ELIZA-style responses
  - Pronoun reflection
  - Simple pattern matching
  - No external dependencies

### 2. ModernBot (AI-powered)
- **File**: `modern_chatbot.py`
- **Type**: Machine learning chatbot using ChatterBot
- **Features**:
  - Trained on English corpus
  - Custom conversation training
  - Best match logic adapter
  - SQLite database storage
  - Interactive commands (train, status, quit)

### 3. Aliza Support Bot (Customer Support Specialist)
- **File**: `aliza_support_bot.py`
- **Type**: Specialized customer support chatbot
- **Features**:
  - Support category classification (Account, Billing, Technical, Product)
  - FAQ database with common support questions
  - Support ticket creation and tracking
  - Automatic escalation for urgent issues
  - Conversation history tracking
  - Personalized user experience

## 🚀 Quick Start

### Option 1: Use the Launcher (Recommended)
```bash
python chatbot_launcher.py
```
This will give you a menu to choose between ELIZA, ModernBot, and Aliza Support Bot.

### Option 2: Run Individual Chatbots

**ELIZA:**
```bash
python Eliza.py
```

**ModernBot:**
```bash
python modern_chatbot.py
```

**Aliza Support Bot:**
```bash
python aliza_support_bot.py
```

## 📦 Installation

1. **Install dependencies for ModernBot:**
```bash
pip install -r requirements.txt
```

2. **Download spaCy model (required for ModernBot):**
```bash
python -m spacy download en_core_web_sm
```

## 🎯 Features

### ModernBot Commands
- `train` - Retrain the bot with corpus data
- `status` - Show bot information and database stats
- `quit` / `exit` / `bye` - Exit the chat

### Aliza Support Bot Features
- **Smart Classification**: Automatically categorizes support requests
- **FAQ Database**: Pre-loaded with common support questions and answers
- **Ticket System**: Creates and tracks support tickets
- **Escalation**: Automatically escalates urgent issues to human support
- **Commands**: 
  - `help` - Show available features
  - `create ticket` - Create a support ticket
  - `ticket status` - Check ticket status
  - `quit` - End conversation

### Training
The ModernBot comes pre-trained with:
- English corpus data
- Custom conversation examples
- Jokes and general responses

## 📁 Project Structure
```
Kaggle-Hackathon/
├── Eliza.py              # Classic ELIZA chatbot
├── modern_chatbot.py     # Modern AI chatbot
├── aliza_support_bot.py  # Customer support chatbot
├── chatbot_launcher.py   # Launcher script
├── requirements.txt      # Python dependencies
├── main.py              # Empty main file
└── README.md            # This file
```

## 🔧 Customization

### Adding Custom Training Data
Edit the `create_sample_conversations()` function in `modern_chatbot.py` to add your own conversation examples.

### Modifying ELIZA Patterns
Edit the `patterns` list in `Eliza.py` to add new response patterns.

### Customizing Aliza Support Bot
- **Add Support Categories**: Modify the `support_knowledge` dictionary in `aliza_support_bot.py`
- **Update FAQs**: Add new FAQ entries to the respective categories
- **Modify Escalation Rules**: Update the `should_escalate()` method for different escalation criteria

## 🐛 Troubleshooting

**ModernBot Import Errors:**
- Make sure you've installed all requirements: `pip install -r requirements.txt`
- Download the spaCy model: `python -m spacy download en_core_web_sm`

**Training Issues:**
- The first run may take longer as it downloads and processes training data
- Check your internet connection for corpus downloads

**Aliza Support Bot:**
- No external dependencies required
- Works with Python standard library only

## 📚 Dependencies

### ModernBot Requirements:
- `chatterbot==1.0.8` - Main chatbot library
- `chatterbot-corpus==1.2.0` - Training data
- `sqlalchemy==1.4.46` - Database ORM
- `spacy==3.5.3` - NLP processing
- `nltk==3.8.1` - Natural language toolkit
- `pyyaml==6.0` - YAML parsing

### ELIZA & Aliza Support Bot Requirements:
- No external dependencies (uses only Python standard library)

## 🎯 Use Cases

### ELIZA
- Educational purposes
- Classic chatbot demonstration
- Simple conversation simulation

### ModernBot
- General conversation
- AI/ML learning projects
- Customizable chatbot applications

### Aliza Support Bot
- Customer service automation
- FAQ handling
- Support ticket management
- Customer support training
- Business support systems