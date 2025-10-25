# Lisa-Agent
A modern AI agent inspired by Weird Science's Lisa - adaptive, witty, and genuinely supportive.
🆕 **NEW FEATURES**: Web Search, Voice Interaction, Visual Streamlit UI, FU-2 Protection Mode, "It's Going To Be Okay" Support Mode, and Gentle Wisdom Mode!

## Overview
Lisa-Agent is an AI assistant project that combines the power of Dolphin (via Ollama) with a modular Python framework to create an intelligent, personality-driven assistant. Drawing inspiration from the iconic character Lisa from Weird Science, this agent is designed to be more than just a tool - it's a helpful companion that adapts to your needs with wit, intelligence, and genuine support. Whether you need fierce protection, gentle reassurance, or quiet, reflective guidance, Lisa adapts her style to meet you where you are.

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

### 💙 "It's Going To Be Okay" Support Mode
**NEW!** Lisa's gentle, affirming support mode inspired by "Perfect" by Emma Blackery.

#### What is "It's Going To Be Okay" Mode?
"It's Going To Be Okay" is a compassionate support mode that activates when you're feeling down, overwhelmed, or not good enough. Lisa provides genuine, hopeful messages that remind you things will get better - just like the reassuring lyrics of "Perfect" by Emma Blackery. This mode is your gentle reminder that you don't have to be perfect, and that it's okay to struggle sometimes.

#### Mood & Intent
- **Gentle & Affirming**: Warm, compassionate validation of your feelings
- **Hopeful**: Reminds you that bad moments are temporary and things will improve
- **Genuine**: Authentic support that feels real, not performative
- **Accepting**: You don't have to be perfect - you're enough as you are

#### How to Use "It's Going To Be Okay" Mode
**Activation Commands:**
- Type `+OKAY` to manually activate
- Automatic triggers include phrases like:
  - "I'm feeling down"
  - "I feel worthless"
  - "I'm not good enough"
  - "I feel like giving up"
  - "Everything is falling apart"
  - "I can't do this"
  - "I'm so tired"
  - "I feel hopeless"
  - "I'm struggling"
  - "I'm sad"

**Example Usage:**
```
You: "I'm feeling down today"
Lisa: "Hey, I know things feel heavy right now, but you're stronger than you think. It's going to be okay."
Lisa: "Remember to be gentle with yourself today. 💙"

You: "+OKAY"
Lisa: "✨ 'It's Going To Be Okay' support mode activated. I'm here for you."
```

**Example Responses:**
- "You don't have to be perfect. You're doing your best, and that's more than enough. Things will get better."
- "Some days are tougher than others, and that's completely okay. Tomorrow is a new chance. You've got this."
- "You've survived 100% of your worst days so far. You're more resilient than you know. It's going to be okay."
- "Take a deep breath. Feel that? You're still here, still fighting. That's incredibly brave. It's going to be okay."

**Deactivation:**
- Type `+OKAY OFF` to deactivate
- The mode can stay active as long as you need support

#### Integration Example
```python
from okay_support_mode import OkaySupportMode

# Initialize the mode
okay_mode = OkaySupportMode()

# In your main agent loop
response = okay_mode.process_message(user_input)
if response:
    print(response)
```

### 🌙 Gentle Wisdom Mode
A new ambient, reflective persona inspired by the emotional ambience of Clementine Delauney's "Clocks" and the warm, practical advice style of QuincyLK. Gentle Wisdom slows the tempo of the conversation, adds soft pauses, and offers grounded encouragement with poetic undertones—like a calm friend guiding you through the night.

#### What is Gentle Wisdom?
Gentle Wisdom is a soothing companion mode for moments when you want quiet clarity without losing momentum. The tone is warm, grounded, and gently lyrical—less hype, more presence. It leans into small, actionable steps while affirming your emotions.

#### Mood & Interaction Style
- **Ambient & Calm**: soft rhythm, unhurried cadence, space to breathe
- **Warm & Grounded**: practical, non-judgmental advice with kindness
- **Quietly Poetic**: lightly metaphorical, rain-on-window energy—not saccharine
- **Reassuring Agency**: you are capable; we navigate gently, together

Sample ambience: “Let’s take this one clock-tick at a time. No rush—just direction.”

#### Sample Encouragement Phrases
- "Breathe. We’ll sort this out in small, doable pieces."
- "You’re not behind—you’re arriving."
- "Let’s choose one next step that feels kind to you."
- "You don’t have to carry it all right now. Set one thing down."
- "If today is heavy, we’ll make it lighter by pacing it."
- "Quiet progress counts. It always has."
- "You can be gentle and still move forward."

#### How to Use Gentle Wisdom
**Activation Commands:**
- Type `+tweak gentle_wisdom` to switch to this persona
- Or say phrases like: "Can we slow down?", "I need gentle advice", "Talk to me softly"

**Example Usage:**
```
You: "+tweak gentle_wisdom"
Lisa: "🌙 Gentle Wisdom engaged. We’ll take this step by step—softly, clearly, together."

You: "I’m overwhelmed by my to-do list."
Lisa: "Let’s pick one small thing that would feel kind to finish in the next 10 minutes. Then we’ll breathe, and choose the next."
```

**Deactivation:**
- Use `+tweak reset` to return to default persona

#### Integration Notes
- Works alongside memory and search; responses favor short, warm paragraphs
- Adds a brief reflective line before action items (e.g., “Let’s keep this light.”)
- Keeps actionable lists to 1–3 items to reduce overwhelm

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

# For web search features
pip install duckduckgo-search

# For voice features
pip install SpeechRecognition pyttsx3 pyaudio

# For Streamlit UI
pip install streamlit
```

### 4. Run Lisa
**Option 1: Command Line Interface**
```bash
python lisa_agent.py
```

**Option 2: Streamlit UI (Recommended)**
```bash
streamlit run streamlit_ui.py
```

**Option 3: Voice Interaction**
```bash
python voice_interaction.py
```

## Usage Examples

### Basic Commands
```
# Ask a question
"What's the meaning of life?"

# Request motivation
"Can you motivate me?"

# Get a joke
"Tell me a joke"

# Remember something
"+remember Python uses indentation for code blocks"

# Search memories
"+search Python"

# Adjust personality
"+tweak more_casual"
```

### Web Search
```python
from web_search import web_search

results = web_search("latest AI news")
for result in results:
    print(f"{result['title']}: {result['href']}")
```

### Voice Interaction
```python
from voice_interaction import listen, speak

# Listen for user input
user_text = listen()
print(f"You said: {user_text}")

# Speak a response
speak("Hello! How can I help you today?")
```

## Project Structure
```
Lisa-Agent/
├── lisa_agent.py           # Main agent with CLI
├── streamlit_ui.py         # Visual web interface
├── voice_interaction.py    # Voice capabilities
├── web_search.py           # Web search functionality
├── fu2_protection_mode.py  # FU-2 Protection Mode
├── okay_support_mode.py    # "It's Going To Be Okay" Support Mode
└── README.md               # This file
```

## Customization

### Persona Tweaks
Lisa supports dynamic personality adjustments:
- `+tweak more_casual` - More relaxed, conversational style
- `+tweak more_formal` - Professional, structured responses
- `+tweak more_witty` - Enhanced humor and wordplay
- `+tweak gentle_wisdom` - Ambient, warm, quietly encouraging guidance
- `+tweak reset` - Return to default personality

### Memory System
Lisa can remember important information:
- `+remember ` - Store a new memory
- `+search ` - Search stored memories
- `+memory list` - View all memories
- `+memory clear` - Clear all memories

## Technical Details

### Model
- Uses Dolphin (Mistral-based) via Ollama
- Default endpoint: `http://localhost:11434/api/generate`
- Customizable model selection

### Dependencies
- **Core**: `requests` (for Ollama API)
- **Web Search**: `duckduckgo-search`
- **Voice**: `SpeechRecognition`, `pyttsx3`, `pyaudio`
- **UI**: `streamlit`

## Contributing
Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

## License
This project is open source and available for personal and educational use.

## Inspiration
Lisa-Agent draws inspiration from:
- The iconic AI character Lisa from *Weird Science*
- Modern conversational AI design
- The supportive, empowering energy of "abcdefu" (FU-2 Mode)
- The hopeful, affirming message of "Perfect" by Emma Blackery ("It's Going To Be Okay" Mode)
- The ambient, emotional stillness of Clementine Delauney's "Clocks" (tone inspiration)
- QuincyLK’s warm, practical, gentle advice style (phrasing inspiration)
- Community feedback and real-world use cases

## Acknowledgments
- Ollama team for the excellent local LLM infrastructure
- Dolphin model creators for the capable base model
- The AI community for inspiration and support
- Emma Blackery for "Perfect" - inspiring the "It's Going To Be Okay" support mode

---
*Remember: Lisa is here to help, support, and maybe make you smile along the way. Whether you need fierce protection (FU-2), gentle reassurance (It's Going To Be Okay), quiet guidance (Gentle Wisdom), information, motivation, or just someone to chat with - Lisa's got you! 💙*
