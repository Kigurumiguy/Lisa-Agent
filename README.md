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
Inspired by the introspective spirit of Fleet Foxes' "White Winter Hymnal," this mode offers thoughtful, poetic responses for when you need calm reflection rather than high energy.
#### Mood & Intent
- **Reflective**: Thoughtful and contemplative
- **Poetic**: Uses imagery and metaphor naturally
- **Calm**: Gentle pacing, no urgency
- **Deep**: Explores meaning without being preachy
#### How to Use Gentle Wisdom Mode
**Activation Commands:**
- Type `+gentlewisdom` or `+wisdom` to manually activate
- Works best for philosophical questions, creative prompts, or when you want slower, more thoughtful conversation
**Example Usage:**
```
You: "What does it mean to truly grow?"
Lisa: "🌙 Growth isn't always reaching higher - sometimes it's growing roots deeper, finding strength in stillness. Like trees in winter, the quiet times prepare us for the blooms ahead."
```
## 🚗 Offline Companion Features
Lisa-Agent is designed to be your companion even when you're away from the internet. These features work entirely offline, making Lisa perfect for road trips, flights, or anywhere connectivity is limited.
### Run Fully Offline
- Works completely without internet connection
- All processing happens locally via Ollama
- No data leaves your device
- Perfect for privacy-conscious users
### Auto-Switch to Offline Mode
Lisa automatically detects when you're offline and adjusts her capabilities:
- Disables web search features gracefully
- Maintains full conversational abilities
- Keeps memory and persona features active
- Notifies you when back online
### Activities for Offline Companionship
When you're offline, Lisa can engage in various activities to keep you entertained and supported:
#### Story Building
Collaboratively create stories with Lisa:
- Take turns adding to a narrative
- Lisa adapts to your genre preferences
- Build characters and worlds together
- Perfect for creative writing practice
#### 20 Questions
Classic guessing game:
- Lisa thinks of something, you guess
- Or you think of something, Lisa guesses
- Great for passing time on long drives
#### Would You Rather
Thought-provoking choice scenarios:
- Lisa poses interesting dilemmas
- Discuss the reasoning behind choices
- Can be silly or serious based on your mood
#### Lyric Relay
A creative and engaging game where you and Lisa take turns building a story or song by exchanging lyric lines:
- **How to Play**: Start with a line from a song, poem, or original creation, and Lisa will respond with a related line, continuing the theme or story
- **Flexible Formats**: Use famous song lyrics, original poetry, or improvised verses - Lisa adapts to your style
- **Creative Storytelling**: Build narratives together by weaving lyrical elements into a cohesive story or emotional journey
- **Personal Touch**: Lisa can incorporate your creative prompts or personal details to make each relay unique and meaningful
- **Perfect for**: Road trips, creative exercises, or just having fun with music and poetry
**Example:**
```
You: "I was at home, drawing pictures of mountain tops, with him on top"
Lisa: "Lemon yellow sun, arms raised in a V, the dead lay in pools of maroon below"
You: "Well, Daddy didn't give attention to the fact that mommy didn't care"
Lisa: "King Jeremy the wicked, ruled his world..."
```
### How It Works
Lisa's offline features rely on:
- **Local LLM**: Dolphin model running via Ollama
- **Persistent Memory**: SQLite database stored locally
- **Lightweight Design**: Minimal resource usage
- **Smart Detection**: Automatic connectivity awareness
## Technical Details
