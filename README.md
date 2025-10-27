# Lisa-Agent
An epic AI companion inspired by Weird Science's Lisa - adaptive, witty, and genuinely supportive.

🆕 **NEW FEATURES**: Web Search, Voice Interaction, Visual Streamlit UI, FU-2 Protection Mode, "It's Going To Be Okay" Support Mode, and Gentle Wisdom Mode!

## 🌟 What Lisa-Agent IS (and ISN'T)

**Lisa-Agent is designed for:**
- **Epic, badass companionship** - Like having a cool friend who's got your back
- **Empowerment and support** - Helping you be your best self
- **Friendly conversations** - Witty banter, advice, and genuine connection
- **Adaptive assistance** - From fierce protection to gentle wisdom

**Lisa-Agent is NOT:**
- ❌ A sexual or romantic companion
- ❌ A dating simulator
- ❌ Designed for NSFW interactions

Lisa is here to be your supportive, empowering friend - the kind of companion who makes you feel like you can take on the world!

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
- **🎤 Voice Interaction**: Text-to-speech and speech-to-text capabilities - hear Lisa's badass voice!
- **🖥️ Visual UI**: Beautiful Streamlit interface with Lisa's avatar
- **📊 Chat History**: Persistent conversation tracking in the UI

### 🎙️ Voice Interaction Features

**NEW!** Experience Lisa's voice and interact naturally with voice commands!

#### Features:
- **Text-to-Speech (TTS)**: Hear Lisa speak her responses in her own voice
- **Speech-to-Text (STT)**: Talk to Lisa naturally - she'll understand you
- **Natural Conversations**: Have hands-free conversations with your AI companion

#### How to Enable Voice Features:

**Prerequisites:**
```bash
# Install required voice libraries
pip install pyttsx3 SpeechRecognition pyaudio
```

**Enabling Text-to-Speech:**
1. In the Streamlit UI, look for the "Enable Voice Output" toggle
2. Toggle it ON to hear Lisa speak her responses
3. Adjust voice settings (speed, volume) in the settings panel

**Enabling Speech-to-Text:**
1. Click the microphone button in the input area
2. Speak your message clearly
3. Lisa will transcribe and respond to what you said

**Voice Commands:**
- "Lisa, activate voice mode" - Enable continuous voice interaction
- "Lisa, quiet mode" - Disable voice output
- Use voice for any command including FU-2, support mode, and more!

**Note:** For best results:
- Use a quality microphone
- Minimize background noise
- Speak clearly at a normal pace
- On Windows, you may need to install PyAudio: `pip install pipwin && pipwin install pyaudio`

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
```

### 💙 "It's Going To Be Okay" Support Mode

**NEW!** Lisa's gentle, reassuring mode for when you need a soft landing and genuine comfort.

#### What is "It's Going To Be Okay" Mode?

Inspired by the hopeful message of Emma Blackery's "Perfect," this mode provides warm, affirming support when you're feeling overwhelmed, anxious, or just need someone to tell you it's going to be alright.

#### Mood & Intent

- **Warm & Reassuring**: Gentle validation and comfort
- **Hopeful**: Reminds you that difficult moments pass
- **Patient**: No rush, no pressure - just being there for you
- **Understanding**: Validates struggles without toxic positivity

#### How to Use "It's Going To Be Okay" Mode

**Activation Commands:**
- Type `+okay` or `+itsgoingtobokay` to manually activate
- Phrases like "I'm overwhelmed," "everything feels like too much," or "I just need to hear it'll be okay" will auto-trigger this mode

**Example Usage:**
```
You: "Everything feels like too much right now"
Lisa: "💙 Hey, take a breath. I'm right here with you. It's going to be okay - not immediately, but it will be. You're doing better than you think."
```

### 🌙 Gentle Wisdom Mode

**NEW!** Lisa's quiet, reflective mode for deep thoughts and meaningful conversations.

#### What is Gentle Wisdom Mode?

When you need thoughtful guidance rather than fierce energy or warm comfort, Lisa shifts into a contemplative, philosophical space. Perfect for late-night conversations, life questions, and those moments when you need perspective.

#### Mood & Intent

- **Reflective**: Thoughtful, measured responses
- **Wise**: Drawing on deeper insights and perspective
- **Calm**: Quiet confidence without urgency
- **Thought-Provoking**: Encourages introspection and growth

#### How to Use Gentle Wisdom Mode

**Activation Commands:**
- Type `+wisdom` or `+gentle` to manually activate
- Phrases like "I've been thinking about..." or "help me understand..." may auto-trigger

**Example Usage:**
```
You: "I've been thinking about what really matters in life"
Lisa: "🌙 That's a beautiful question to sit with. Sometimes the most important things aren't the loudest ones..."
```

## 🚗 Offline Companion Features

Lisa can work as your companion even when you're offline or on the go:

- **Local Processing**: All AI runs locally via Ollama - no internet required for core features
- **Voice Interaction**: Perfect for hands-free use while driving or multitasking
- **Persistent Memory**: Your conversations and notes stay with you
- **Adaptive Modes**: Switch between protection, comfort, and wisdom modes as needed

**Safety Note:** If using voice features while driving, ensure they're set up before you start driving and use voice commands only. Your safety always comes first!

## Technical Details

### Architecture

- **AI Backend**: Ollama running Dolphin model
- **Frontend**: Streamlit web interface
- **Voice Processing**: pyttsx3 (TTS) and SpeechRecognition (STT)
- **Search Integration**: DuckDuckGo and Bing APIs
- **Storage**: Local file-based memory system

### Requirements

- Python 3.8+
- Ollama with Dolphin model
- Required packages: `streamlit`, `requests`, `pyttsx3`, `SpeechRecognition`, `pyaudio`

### Installation

```bash
# Clone the repository
git clone https://github.com/Kigurumiguy/Lisa-Agent.git
cd Lisa-Agent

# Install dependencies
pip install -r requirements.txt

# Install Ollama and download Dolphin model
# Visit https://ollama.ai for installation instructions
ollama pull dolphin

# Run Lisa-Agent
streamlit run app.py
```

### Configuration

Edit `config.json` to customize:
- Voice settings (speed, volume, voice type)
- UI theme and avatar
- Search API keys
- Memory storage location
- Default mode preferences

## Contributing

Contributions are welcome! Whether it's new modes, features, or improvements, feel free to submit pull requests.

## License

This project is open source. See LICENSE file for details.

## Acknowledgments

- Inspired by Lisa from *Weird Science* - the ultimate supportive companion
- Voice interaction for natural, hands-free conversations
- Music inspiration: "abcdefu" (Our Last Night cover) for FU-2 mode, "Perfect" by Emma Blackery for Support mode

---

**Remember**: Lisa is here to help you be your best, most empowered self. She's your friend, your support system, and your hype-person all rolled into one badass AI companion. 🚀💙🔥
