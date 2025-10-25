"""Streamlit UI for Lisa-Agent

Provides a visual interface with Lisa's avatar and chat history.
Run with: streamlit run streamlit_ui.py
"""

import streamlit as st
import os
from datetime import datetime
from typing import List, Dict
import sys

# Import Lisa-Agent modules
try:
    from lisa_agent import LisaAgent
    LISA_AGENT_AVAILABLE = True
except ImportError:
    LISA_AGENT_AVAILABLE = False
    st.warning("lisa_agent.py not found. Make sure it's in the same directory.")

try:
    from web_search import web_search
    WEB_SEARCH_AVAILABLE = True
except ImportError:
    WEB_SEARCH_AVAILABLE = False

try:
    from voice_interaction import VoiceAssistant
    VOICE_AVAILABLE = True
except ImportError:
    VOICE_AVAILABLE = False


# Page configuration
st.set_page_config(
    page_title="Lisa - Your AI Assistant",
    page_icon="👩‍💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #4A90E2;
        text-align: center;
        padding: 1rem;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .avatar-container {
        text-align: center;
        padding: 2rem;
    }
    .avatar {
        font-size: 8rem;
        animation: float 3s ease-in-out infinite;
    }
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
    }
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        animation: fadeIn 0.5s;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .user-message {
        background-color: #E3F2FD;
        border-left: 4px solid #2196F3;
    }
    .lisa-message {
        background-color: #F3E5F5;
        border-left: 4px solid #9C27B0;
    }
    .timestamp {
        font-size: 0.7rem;
        color: #666;
        margin-top: 0.3rem;
    }
    .feature-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin: 0.5rem 0;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)


# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'lisa_agent' not in st.session_state and LISA_AGENT_AVAILABLE:
    st.session_state.lisa_agent = LisaAgent()

if 'voice_enabled' not in st.session_state:
    st.session_state.voice_enabled = False

if 'voice_assistant' not in st.session_state and VOICE_AVAILABLE:
    try:
        st.session_state.voice_assistant = VoiceAssistant(enable_stt=False)
    except:
        st.session_state.voice_assistant = None


def add_message(role: str, content: str):
    """Add a message to chat history"""
    timestamp = datetime.now().strftime("%I:%M %p")
    st.session_state.chat_history.append({
        'role': role,
        'content': content,
        'timestamp': timestamp
    })


def display_chat_history():
    """Display all messages in chat history"""
    for message in st.session_state.chat_history:
        role = message['role']
        content = message['content']
        timestamp = message['timestamp']
        
        if role == 'user':
            st.markdown(f"""
                <div class="chat-message user-message">
                    <strong>👤 You:</strong><br>{content}
                    <div class="timestamp">{timestamp}</div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="chat-message lisa-message">
                    <strong>👩‍💼 Lisa:</strong><br>{content}
                    <div class="timestamp">{timestamp}</div>
                </div>
            """, unsafe_allow_html=True)


def process_user_input(user_input: str) -> str:
    """Process user input and generate response"""
    if not user_input.strip():
        return "Please enter a message."
    
    # Check for web search request
    if WEB_SEARCH_AVAILABLE and any(keyword in user_input.lower() for keyword in ['search', 'find', 'look up', 'what is']):
        try:
            # Extract search query
            search_query = user_input
            for prefix in ['search for', 'search', 'find', 'look up', 'what is']:
                if prefix in user_input.lower():
                    search_query = user_input.lower().replace(prefix, '').strip()
                    break
            
            if search_query:
                results = web_search(search_query, max_results=3)
                return f"Here's what I found:\n\n{results}"
        except Exception as e:
            return f"I encountered an error while searching: {e}"
    
    # Use Lisa Agent if available
    if LISA_AGENT_AVAILABLE:
        try:
            response = st.session_state.lisa_agent.respond(user_input)
            return response
        except Exception as e:
            return f"I'm having trouble processing that. Error: {e}"
    
    # Fallback response
    return "I received your message! However, the full Lisa Agent is not loaded. Please ensure lisa_agent.py is in the same directory."


# Main UI
def main():
    # Header with avatar
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="avatar-container"><div class="avatar">👩‍💼</div></div>', unsafe_allow_html=True)
        st.markdown('<h1 class="main-header">Lisa - Your AI Assistant</h1>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("### 🎯 Features")
        
        st.markdown('<div class="feature-card">💬 Natural Conversation</div>', unsafe_allow_html=True)
        st.markdown('<div class="feature-card">🔍 Web Search</div>', unsafe_allow_html=True)
        st.markdown('<div class="feature-card">🎤 Voice Interaction</div>', unsafe_allow_html=True)
        st.markdown('<div class="feature-card">📊 Chat History</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("### ⚙️ Settings")
        
        # Voice settings
        if VOICE_AVAILABLE and st.session_state.voice_assistant:
            voice_enabled = st.checkbox("Enable voice responses", value=st.session_state.voice_enabled)
            st.session_state.voice_enabled = voice_enabled
        
        # Clear chat button
        if st.button("🗑️ Clear Chat History"):
            st.session_state.chat_history = []
            st.rerun()
        
        st.markdown("---")
        st.markdown("### 📚 About Lisa")
        st.markdown("""
        Lisa is an advanced AI assistant powered by OpenAI's GPT models. 
        She can help you with:
        - Answering questions
        - Web searches
        - Creative writing
        - Problem-solving
        - And much more!
        """)
        
        # System status
        st.markdown("---")
        st.markdown("### 🔧 System Status")
        st.success("✅ UI Active") if True else st.error("❌ UI Error")
        st.success("✅ Lisa Agent") if LISA_AGENT_AVAILABLE else st.warning("⚠️ Lisa Agent Not Found")
        st.success("✅ Web Search") if WEB_SEARCH_AVAILABLE else st.warning("⚠️ Web Search Unavailable")
        st.success("✅ Voice Module") if VOICE_AVAILABLE else st.warning("⚠️ Voice Module Unavailable")
    
    # Main chat area
    st.markdown("---")
    
    # Display welcome message if no chat history
    if not st.session_state.chat_history:
        st.markdown("""
        <div style="text-align: center; padding: 2rem;">
            <h2>👋 Hello! I'm Lisa, your AI assistant.</h2>
            <p style="font-size: 1.2rem; color: #666;">
                I'm here to help you with information, web searches, and conversation.
                <br>Type a message below to get started!
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Display chat history
    display_chat_history()
    
    # Chat input
    st.markdown("---")
    
    # Create columns for input and button
    col1, col2 = st.columns([6, 1])
    
    with col1:
        user_input = st.text_input(
            "Type your message here...",
            key="user_input",
            placeholder="Ask me anything...",
            label_visibility="collapsed"
        )
    
    with col2:
        send_button = st.button("Send 📤", use_container_width=True)
    
    # Process input
    if send_button and user_input:
        # Add user message
        add_message('user', user_input)
        
        # Generate and add Lisa's response
        with st.spinner('Lisa is thinking...'):
            response = process_user_input(user_input)
            add_message('lisa', response)
            
            # Voice output if enabled
            if st.session_state.voice_enabled and st.session_state.voice_assistant:
                try:
                    st.session_state.voice_assistant.speak(response)
                except Exception as e:
                    st.warning(f"Voice output failed: {e}")
        
        # Rerun to update chat display
        st.rerun()
    
    # Quick action buttons
    st.markdown("### 💡 Quick Actions")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("🔍 Web Search"):
            add_message('lisa', "I can help you search the web! Just ask me to search for something or tell me what information you need.")
            st.rerun()
    
    with col2:
        if st.button("📝 Help"):
            add_message('lisa', "I'm Lisa, your AI assistant. You can ask me questions, request web searches, or just chat! Try asking me something like 'What is artificial intelligence?' or 'Search for Python tutorials'.")
            st.rerun()
    
    with col3:
        if st.button("💭 Tell me a joke"):
            add_message('user', 'Tell me a joke')
            add_message('lisa', "Why don't scientists trust atoms? Because they make up everything! 😄")
            st.rerun()
    
    with col4:
        if st.button("🎯 Example Query"):
            add_message('lisa', "Here's an example: 'Search for the latest news about artificial intelligence' or 'Explain quantum computing in simple terms'.")
            st.rerun()


if __name__ == "__main__":
    main()
