# Lisa-Agent
A modern AI agent inspired by Weird Science's Lisa - adaptive, witty, and genuinely supportive.

🆕 **NEW FEATURES**: Web Search, Voice Interaction, Visual Streamlit UI, and FU-2 Protection Mode!

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

### 🔥 FU-2 Protection Mode

**NEW!** Lisa's fierce, empowering protection mode inspired by the energy of "abcdefu" (covered by Our Last Night).

#### What is FU-2?
FU-2 is a special support mode that activates when you're hurting from someone's actions. Lisa channels fierce, witty, and empowering energy to remind you of your worth and help you move forward. Think of it as your hype-person who won't let anyone dim your light!

#### Mood & Intent
- **Fiercely Supportive**: No-nonsense validation of your feelings
- **Empowering**: Reminds you of your worth and strength
- **Witty & Bold**: Channel that "ABCDEFU" energy to help you process pain into power
- **Protective**: Lisa's got your back, always

#### How to Use FU-2

**Activation Commands:**
- Type `+FU2` or `+fu2` to manually activate
- Say "someone hurt me" or "they hurt me" and Lisa will auto-activate FU-2 mode
- Other triggers: "he/she hurt me", "feeling hurt", "really hurt me"

**Example Usage:**
```
You: "Someone really hurt me today"
Lisa: "🔥 FU-2 MODE ACTIVATED 🔥 Nobody messes with my human! Time to bring the fire!"
Lisa: "You know what? A-B-C-D-E, F THEM! You're amazing and they're missing out! 🔥"
Lisa: "I'm here with you, and we're not letting anyone dim your light! 💫"
```

**Deactivation:**
- FU-2 mode stays active for your session until you're feeling better
- You can manually deactivate with `+fu2 off` if needed

#### Integration Example
```python
from fu2_protection_mode import FU2ProtectionMode

# Initialize the mode
fu2 = FU2ProtectionMode()

# In your main agent loop
if fu2.detect_trigger(user_input):
    print(fu2.activate())
    response = fu2.respond()
    print(response['empowering'])
    print(response['supportive'])
```

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
