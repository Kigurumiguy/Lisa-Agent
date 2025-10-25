# Lisa-Agent
A modern AI agent inspired by Weird Science's Lisa - adaptive, witty, and genuinely supportive.

🆕 **NEW FEATURES**: Web Search, Voice Interaction, and Visual Streamlit UI!

## Overview
Lisa-Agent is an AI assistant project that combines the power of Dolphin (via Ollama) with a modular Python framework to create an intelligent, personality-driven assistant. Drawing inspiration from the iconic character Lisa from Weird Science, this agent is designed to be more than just a tool - it's a helpful companion that adapts to your needs with wit, intelligence, and genuine support.

## Features
### Core Capabilities
- **Q&A and Advice**: Ask anything and get thoughtful, structured responses
- **Motivational Support**: Request pep talks and encouragement
- **Entertainment**: Ask for clean jokes and light conversation
- **Memory System**: Store and search notes with `+remember` and `+search`
- **Persona Tweaks**: Adjust Lisa's style with `+tweak` commands

### 🆕 Advanced Features
- **🔍 Web Search**: Real-time web search using DuckDuckGo and Bing APIs
- **🎤 Voice Interaction**: Text-to-speech and speech-to-text capabilities
- **🖥️ Visual UI**: Beautiful Streamlit interface with Lisa's avatar
- **📊 Chat History**: Persistent conversation tracking in the UI

## Quick Start

### Prerequisites
- Python 3.9+
- [Ollama](https://ollama.ai/) installed
- Dolphin model pulled (e.g., `dolphin-mistral` or your preferred variant)

### 1. Install Ollama
```bash
# macOS/Linux
curl -fsSL https://ollama.ai/install.sh | sh

# Windows
# Download from https://ollama.ai/download
```

### 2. Pull and Start Dolphin Model
```bash
# Pull the model
ollama pull dolphin-mistral

# Start Ollama server (if not running)
ollama serve
```

### 3. Clone and Setup
```bash
# Clone this repository
git clone https://github.com/Kigurumiguy/Lisa-Agent.git
cd Lisa-Agent

# Install basic dependencies
pip install requests

# Install optional dependencies for advanced features
pip install streamlit pyttsx3 gtts speechrecognition pygame
```

### 4. Choose Your Interface

#### Option A: Command Line Interface
```bash
python lisa_agent.py
```

#### Option B: Visual Streamlit UI (Recommended)
```bash
streamlit run streamlit_ui.py
```

#### Option C: Voice Interaction
```bash
# Test voice features
python voice_interaction.py

# Or enable voice in the UI
# Check "Enable voice responses" in the sidebar
```

## Module Documentation

### 🔍 Web Search Module (`web_search.py`)
Provides real-time web search capabilities.

**Features:**
- DuckDuckGo API integration (free, no API key needed)
- Bing Search API fallback (requires API key)
- Structured search results with titles, snippets, and URLs
- Easy integration with Lisa Agent

**Usage:**
```python
from web_search import web_search

# Simple search
results = web_search("artificial intelligence")
print(results)

# With Bing API key for enhanced results
results = web_search("Python tutorials", bing_api_key="your-key", max_results=5)
```

**Environment Variables:**
- `BING_API_KEY`: Optional Bing Search API key for enhanced results

### 🎤 Voice Interaction Module (`voice_interaction.py`)
Adds voice capabilities with multiple TTS and STT options.

**Text-to-Speech Options:**
- **pyttsx3**: Offline TTS (fast, no internet needed)
- **gTTS**: Online TTS (Google, higher quality)
- Automatic engine selection

**Speech-to-Text:**
- Google Speech Recognition API
- Microphone input support
- Ambient noise adjustment

**Usage:**
```python
from voice_interaction import VoiceAssistant

# Initialize voice assistant
voice = VoiceAssistant(tts_engine="auto")

# Speak text
voice.speak("Hello! I'm Lisa, your voice assistant.")

# Listen for speech
user_input = voice.listen(timeout=5)
if user_input:
    print(f"You said: {user_input}")
```

**Dependencies:**
```bash
# For TTS
pip install pyttsx3 gtts pygame

# For STT
pip install SpeechRecognition pyaudio

# On macOS, you might need:
brew install portaudio
```

### 🖥️ Streamlit UI (`streamlit_ui.py`)
Beautiful web interface with Lisa's visual persona.

**Features:**
- 🎨 Beautiful, responsive design with Lisa's avatar
- 💬 Chat interface with message history
- 🔧 Settings panel with voice toggle
- 📊 System status indicators
- 🚀 Quick action buttons
- 📱 Mobile-friendly layout

**Running the UI:**
```bash
# Start the Streamlit app
streamlit run streamlit_ui.py

# The UI will open at http://localhost:8501
```

**UI Components:**
- **Avatar**: Animated Lisa emoji with floating effect
- **Chat Area**: Conversation history with timestamps
- **Input**: Message input with send button
- **Sidebar**: Features, settings, and system status
- **Quick Actions**: Preset buttons for common tasks

## Installation Guide

### Basic Installation
```bash
# Core functionality only
pip install requests
```

### Full Installation (All Features)
```bash
# Install all optional dependencies
pip install streamlit pyttsx3 gtts speechrecognition pygame pyaudio
```

### Platform-Specific Notes

**Windows:**
```bash
# May need Visual C++ Build Tools for some packages
pip install pipwin
pipwin install pyaudio
```

**macOS:**
```bash
# Install audio dependencies
brew install portaudio
pip install pyaudio
```

**Linux:**
```bash
# Install audio dependencies
sudo apt-get install python3-pyaudio portaudio19-dev
# OR
sudo yum install python3-pyaudio portaudio-devel
```

## Configuration

### Environment Variables
- `OLLAMA_BASE_URL` (default: `http://localhost:11434`)
- `LISA_MODEL` (default: `dolphin-mistral`)
- `BING_API_KEY` (optional: for enhanced web search)

### Custom Model
```bash
# Use a different Dolphin variant
export LISA_MODEL="dolphin-mixtral"
python lisa_agent.py
```

### Bing Search Setup (Optional)
1. Get a Bing Search API key from Azure Cognitive Services
2. Set the environment variable:
   ```bash
   export BING_API_KEY="your-api-key-here"
   ```
3. Web search will automatically use both DuckDuckGo and Bing

## Example Usage

### Command Line
```bash
Lisa Agent (Ollama • Dolphin)
Type 'exit' or 'quit' to leave. Type 'help' for tips.

You> What are 3 ways to learn faster?
Lisa> Here are three evidence-based techniques to accelerate learning:
• **Active recall**: Test yourself frequently instead of just re-reading...

You> Search for Python machine learning tutorials
Lisa> Here's what I found:

1. Python Machine Learning Tutorial - Real Python
   A comprehensive guide to machine learning in Python...
   URL: https://realpython.com/python-machine-learning/

You> +remember I'm learning machine learning with Python
Lisa> Noted. I won't forget.
```

### Memory System
```bash
You> +remember I have a meeting with Sarah on Friday
Lisa> Noted. I won't forget.

You> +search meeting
Lisa> Memory hits:
  1. I have a meeting with Sarah on Friday
  2. I'm learning machine learning with Python
```

## Architecture

### Core Modules
- **`OllamaClient`**: Handles communication with local Ollama server
- **`Persona`**: Manages Lisa's personality and system prompts
- **`MemoryStore`**: Simple in-memory storage (ready for persistence upgrades)
- **`LisaAgent`**: Core agent orchestration and routing

### Advanced Modules
- **`WebSearchEngine`**: Real-time web search with multiple API backends
- **`VoiceAssistant`**: Combined TTS/STT with multiple engine support
- **`Streamlit UI`**: Web-based visual interface with chat history

### Integration Flow
```
User Input → Lisa Agent → [Web Search] → [Voice Output] → UI Display
     ↓                        ↓              ↓              ↓
  Memory Store ←→ Response Generation ←→ TTS Engine ←→ Chat History
```

## Troubleshooting

### Common Issues

**Ollama Connection:**
```bash
# Check if Ollama is running
curl http://localhost:11434/api/version

# Start Ollama if needed
ollama serve
```

**Voice Issues:**
```bash
# Test microphone
python -c "import speech_recognition as sr; print('Microphone test:', sr.Microphone.list_microphone_names())"

# Test TTS
python voice_interaction.py
```

**Missing Dependencies:**
```bash
# Check what's installed
pip list | grep -E "streamlit|pyttsx3|gtts|speech"

# Install missing packages
pip install [missing-package]
```

## Upgrade Notes

### From Previous Version
If you had Lisa-Agent before the advanced features:

1. **Pull latest changes:**
   ```bash
   git pull origin main
   ```

2. **Install new dependencies:**
   ```bash
   pip install streamlit pyttsx3 gtts speechrecognition pygame
   ```

3. **Try the new UI:**
   ```bash
   streamlit run streamlit_ui.py
   ```

4. **Enable web search:**
   - No setup needed for DuckDuckGo
   - Optional: Get Bing API key for enhanced results

## Goals
- **Adaptive Intelligence**: Leverage Dolphin's capabilities to understand context and provide relevant assistance
- **Witty Interaction**: Inject personality and humor into conversations while maintaining professionalism
- **Supportive Presence**: Offer genuine help and encouragement tailored to user needs
- **Local-First**: Run entirely on your hardware with optional cloud integrations
- **Multi-Modal**: Support text, voice, and visual interaction modes

## Contributing
Feel free to submit issues, feature requests, or pull requests! This project is designed to be hackable and extensible.

### Development Setup
```bash
# Fork and clone
git clone https://github.com/YOUR-USERNAME/Lisa-Agent.git
cd Lisa-Agent

# Install all dependencies
pip install requests streamlit pyttsx3 gtts speechrecognition pygame pyaudio

# Test all modules
python lisa_agent.py
python voice_interaction.py
streamlit run streamlit_ui.py
```

## License
MIT License - see the code for details.

---
*"I'm Lisa. I do things that are good for you and bad for people who aren't nice to you."* 

🚀 Building an AI companion that's got your back - now with voice, vision, and web search capabilities!
