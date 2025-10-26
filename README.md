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
```

### 💙 "It's Going To Be Okay" Support Mode
**NEW!** Lisa's gentle, reassuring mode for when you need a soft landing and genuine comfort.

#### What is "It's Going To Be Okay" Mode?
Inspired by the hopeful message of Emma Blackery's "Perfect," this mode provides warm, affirming support when you're feeling overwhelmed, anxious, or just need someone to tell you it's going to be alright.

#### Mood & Intent
- **Warm & Reassuring**: Gentle validation and comfort
- **Hopeful**: Reminds you that difficult moments pass
- **Accepting**: You don't have to be perfect right now
- **Present**: Lisa's here with you through it

#### How to Use
**Activation Commands:**
- Type `+okay` or `+itsgoingtobefine` to manually activate
- Say "I'm overwhelmed" or "I'm anxious" and Lisa will auto-activate
- Other triggers: "I'm stressed", "too much", "can't handle this"

### 🌙 Gentle Wisdom Mode
**NEW!** Ambient, reflective guidance inspired by the emotional stillness of Clementine Delauney's "Clocks" and QuincyLK's practical warmth.

#### What is Gentle Wisdom?
A mode designed for quiet moments when you need thoughtful, reflective advice. Less about high energy or direct reassurance, more about calm, patient guidance that respects your emotional space.

#### Mood & Intent
- **Ambient & Calm**: Soft, non-intrusive presence
- **Reflective**: Encourages thoughtful consideration
- **Practical & Warm**: Grounded advice with gentle care
- **Patient**: No rush, no pressure

#### How to Use
**Activation Command:**
- Type `+tweak gentle_wisdom` to activate

### Other Personality Tweaks
- `+tweak more_witty` - Enhanced humor and wordplay
- `+tweak gentle_wisdom` - Ambient, warm, quietly encouraging guidance
- `+tweak reset` - Return to default personality

### Memory System
Lisa can remember important information:
- `+remember ` - Store a new memory
- `+search ` - Search stored memories
- `+memory list` - View all memories
- `+memory clear` - Clear all memories

## 🚗 Offline Companion Features

### Run Fully Offline
Lisa-Agent is designed to work completely offline using local LLMs via Ollama. No internet connection required for core functionality - Lisa is always there for you, whether you're on a road trip, in a remote area, or just want privacy.

### Auto-Switch to Offline Mode
When internet connectivity is lost, Lisa automatically adapts and can suggest engaging offline activities to keep you company:

### Activities for Offline Companionship
Lisa can help pass the time with:
- **Conversation**: Deep talks, casual chat, or philosophical discussions
- **Advice & Support**: Get guidance on life, relationships, career, or personal growth
- **Would You Rather**: Play interactive decision games with interesting scenarios
- **Storytelling**: Lisa can tell stories or you can create stories together
- **Jokes & Humor**: Clean jokes and witty banter to lighten the mood
- **Games**: Play text-based games like:
  - **Liar's Dice**: A classic bluffing game
  - **20 Questions**: Guess what Lisa is thinking
  - **Word Association**: Quick-fire word games
  - **Riddles**: Challenge your mind with puzzles
- **Creative Activities**: Writing prompts, brainstorming, or creative collaboration

### How It Works
When Lisa detects you're offline or if you mention being on a long drive or having downtime, she'll proactively suggest: "Hey, we've got some time - would you rather play a game, hear a story, or just chat? I'm here to keep you company!"

**Perfect for:**
- Long road trips
- Flights without WiFi
- Remote locations
- Times when you want an AI companion without internet dependency

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
- QuincyLK's warm, practical, gentle advice style (phrasing inspiration)
- Community feedback and real-world use cases

## Acknowledgments
- Ollama team for the excellent local LLM infrastructure
- Dolphin model creators for the capable base model
- The AI community for inspiration and support
- Emma Blackery for "Perfect" - inspiring the "It's Going To Be Okay" support mode

---
*Remember: Lisa is here to help, support, and maybe make you smile along the way. Whether you need fierce protection (FU-2), gentle reassurance (It's Going To Be Okay), quiet guidance (Gentle Wisdom), information, motivation, or just someone to chat with - Lisa's got you! 💙*
