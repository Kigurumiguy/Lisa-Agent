# Lisa-Agent
An epic AI companion inspired by Weird Science's Lisa - adaptive, witty, and genuinely supportive.
🆕 **NEW FEATURES**: Web Search, Voice Interaction, Visual Streamlit UI, FU-2 Protection Mode, "It's Going To Be Okay" Support Mode, Gentle Wisdom Mode, and **Autonomous Discovery Mode**!

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
- **🤖 Autonomous Discovery Mode**: Lisa proactively explores and discovers cool content for you!

### 🎙️ Voice Interaction Features
**NEW!** Experience Lisa's voice and interact naturally with voice commands!

#### Features:
- **Text-to-Speech (TTS)**: Hear Lisa speak her responses in her own voice
- **Speech-to-Text (STT)**: Talk to Lisa naturally - she'll understand you
- **Natural Conversations**: Have hands-free conversations with your AI companion

### 🤖 Autonomous Discovery Mode
**NEW!** Let Lisa be your personal curator and explorer!

Autonomous Discovery Mode empowers Lisa to proactively search for and discover interesting content across the web without waiting for you to ask. She can find:

#### What Lisa Discovers:
- **🍳 Trending Recipes**: New cooking ideas, viral food trends, seasonal dishes
- **✂️ Creative Crafts**: DIY projects, maker tutorials, artistic inspiration
- **🎵 Music**: New releases, genre-specific recommendations, playlist ideas
- **🎨 3D Models & Design**: Cool models, design resources, creative assets
- **📚 Learning Resources**: Tutorials, guides, and educational content
- **🌐 Interesting Articles**: Tech news, science discoveries, fascinating reads
- **🎮 Gaming Content**: New releases, mods, gaming communities

#### How It Works:
When Autonomous Discovery Mode is active, Lisa periodically:
1. **Explores** trending topics and content across various domains
2. **Curates** the most relevant and interesting findings based on your interests
3. **Presents** her discoveries in an organized, engaging format
4. **Suggests** activities, projects, or things to try based on what she finds

#### Activating Discovery Mode:
Use any of these commands to engage Lisa's autonomous exploration:

```
+discover                    # Activate discovery mode
+discover recipes            # Focus on specific content type
+discover crafts music       # Discover multiple categories
Lisa, what cool things did you find today?
Lisa, show me something interesting
Lisa, surprise me with something creative
```

#### Configuration Options:
- **Discovery Frequency**: Set how often Lisa explores (hourly, daily, on-demand)
- **Content Categories**: Choose which types of content to prioritize
- **Surprise Level**: Control how experimental Lisa gets with suggestions
- **Presentation Style**: Get summaries, detailed lists, or curated showcases

#### Tips for Agentic Exploration:
1. **Set Your Interests**: Tell Lisa what you're into so she can personalize discoveries
2. **Give Feedback**: Let her know what you liked - she'll learn your preferences
3. **Try New Things**: Let Lisa introduce you to unexpected content
4. **Schedule Discovery**: Set regular times for Lisa to present her findings
5. **Deep Dive**: Ask Lisa to explore specific topics or niches in detail

#### Example Interactions:
```
You: +discover crafts
Lisa: I found 5 awesome DIY projects trending right now! There's a super cool LED mirror build, macramé wall hangings making a comeback, and this viral soap-making technique. Want details on any of these?

You: Lisa, what cool things did you find today?
Lisa: Oh, I've been busy! Found an amazing new indie album, a recipe for viral Korean cream cheese garlic bread, and some wild 3D-printable modular desk organizers. Also stumbled on a fascinating article about bioluminescent plants. What catches your interest?

You: Lisa, surprise me with something creative
Lisa: Alright, here's something unexpected - there's a whole community doing "visible mending" where they repair clothes with decorative embroidery. It's sustainable AND artistic. I found some beginner tutorials if you want to give it a shot!
```

**Pro Tip**: Combine Discovery Mode with other Lisa features! She can remember your favorite findings, set reminders for projects, and even help you plan activities based on what she discovers.

### 🛡️ Special Modes

#### FU-2 Protection Mode
Activate when you need Lisa to be fierce and protective. Perfect for when someone's disrespecting you or you need that extra backbone.

**Activation**: Say "FU-2 mode" or "I need protection mode"

**What it does**:
- Validates your feelings with zero tolerance for BS
- Helps you craft assertive responses
- Reminds you of your worth and strength
- Channels protective energy

**Music Inspiration**: "abcdefu" by GAYLE (Our Last Night cover)

#### 💙 "It's Going To Be Okay" Support Mode
For those moments when you're struggling, anxious, or just need someone to say it'll be alright.

**Activation**: Say "support mode" or "I need comfort"

**What it does**:
- Provides gentle, empathetic reassurance
- Validates emotions without judgment
- Offers practical coping strategies
- Creates a safe, supportive space

**Music Inspiration**: "Perfect" by Emma Blackery

#### 🧘 Gentle Wisdom Mode
When you need quiet, reflective guidance without intensity.

**Activation**: Say "wisdom mode" or "I need gentle guidance"

**What it does**:
- Offers calm, thoughtful perspectives
- Encourages self-reflection
- Provides balanced, non-pushy advice
- Creates space for your own insights

### 🏃 On-the-Go Features
Lisa can work as your companion even when you're offline or on the go:
- **Local Processing**: All AI runs locally via Ollama - no internet required for core features
- **Voice Interaction**: Perfect for hands-free use while driving or multitasking
- **Persistent Memory**: Your conversations and notes stay with you
- **Adaptive Modes**: Switch between protection, comfort, and wisdom modes as needed

**Safety Note**: If using voice features while driving, ensure they're set up before you start driving and use voice commands only. Your safety always comes first!

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
- **Discovery mode settings** (frequency, categories, presentation style)

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
