"""Voice Interaction Module for Lisa-Agent

Provides text-to-speech and speech-to-text capabilities.
Supports pyttsx3 (offline) and gTTS (online) for TTS.
Uses SpeechRecognition for STT.
"""

import os
import sys
from typing import Optional, Callable
import tempfile

try:
    import pyttsx3
    PYTTSX3_AVAILABLE = True
except ImportError:
    PYTTSX3_AVAILABLE = False
    print("Warning: pyttsx3 not installed. Offline TTS unavailable.")

try:
    from gtts import gTTS
    GTTS_AVAILABLE = True
except ImportError:
    GTTS_AVAILABLE = False
    print("Warning: gTTS not installed. Online TTS unavailable.")

try:
    import speech_recognition as sr
    SR_AVAILABLE = True
except ImportError:
    SR_AVAILABLE = False
    print("Warning: SpeechRecognition not installed. STT unavailable.")

try:
    import pygame
    PYGAME_AVAILABLE = True
except ImportError:
    PYGAME_AVAILABLE = False


class TextToSpeech:
    """Handles text-to-speech conversion using various engines"""
    
    def __init__(self, engine: str = "auto", voice_rate: int = 150):
        """
        Initialize TTS engine.
        
        Args:
            engine: TTS engine to use ('pyttsx3', 'gtts', or 'auto')
            voice_rate: Speech rate for pyttsx3 (words per minute)
        """
        self.engine_type = engine
        self.voice_rate = voice_rate
        self.tts_engine = None
        
        if engine == "auto":
            if PYTTSX3_AVAILABLE:
                self.engine_type = "pyttsx3"
            elif GTTS_AVAILABLE:
                self.engine_type = "gtts"
            else:
                raise ImportError("No TTS engine available. Install pyttsx3 or gTTS.")
        
        if self.engine_type == "pyttsx3":
            if not PYTTSX3_AVAILABLE:
                raise ImportError("pyttsx3 not installed. Run: pip install pyttsx3")
            self._init_pyttsx3()
        elif self.engine_type == "gtts":
            if not GTTS_AVAILABLE:
                raise ImportError("gTTS not installed. Run: pip install gTTS")
    
    def _init_pyttsx3(self):
        """Initialize pyttsx3 engine"""
        self.tts_engine = pyttsx3.init()
        self.tts_engine.setProperty('rate', self.voice_rate)
        
        # Get available voices
        voices = self.tts_engine.getProperty('voices')
        if voices:
            # Try to set a female voice (Lisa)
            for voice in voices:
                if 'female' in voice.name.lower() or 'zira' in voice.name.lower():
                    self.tts_engine.setProperty('voice', voice.id)
                    break
    
    def speak_pyttsx3(self, text: str) -> bool:
        """
        Speak text using pyttsx3 (offline).
        
        Args:
            text: Text to speak
            
        Returns:
            True if successful, False otherwise
        """
        try:
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
            return True
        except Exception as e:
            print(f"pyttsx3 error: {e}")
            return False
    
    def speak_gtts(self, text: str, lang: str = 'en') -> bool:
        """
        Speak text using gTTS (online).
        
        Args:
            text: Text to speak
            lang: Language code (default: 'en')
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Create temporary file for audio
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
                temp_file = fp.name
            
            # Generate speech
            tts = gTTS(text=text, lang=lang, slow=False)
            tts.save(temp_file)
            
            # Play audio
            if PYGAME_AVAILABLE:
                pygame.mixer.init()
                pygame.mixer.music.load(temp_file)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
                pygame.mixer.quit()
            elif sys.platform == 'darwin':  # macOS
                os.system(f'afplay {temp_file}')
            elif sys.platform == 'win32':  # Windows
                os.system(f'start {temp_file}')
            else:  # Linux
                os.system(f'mpg123 {temp_file}')
            
            # Clean up
            try:
                os.remove(temp_file)
            except:
                pass
            
            return True
            
        except Exception as e:
            print(f"gTTS error: {e}")
            return False
    
    def speak(self, text: str) -> bool:
        """
        Speak text using configured engine.
        
        Args:
            text: Text to speak
            
        Returns:
            True if successful, False otherwise
        """
        if not text:
            return False
        
        if self.engine_type == "pyttsx3":
            return self.speak_pyttsx3(text)
        elif self.engine_type == "gtts":
            return self.speak_gtts(text)
        else:
            print(f"Unknown TTS engine: {self.engine_type}")
            return False


class SpeechToText:
    """Handles speech-to-text conversion using Google Speech Recognition"""
    
    def __init__(self):
        """Initialize STT recognizer"""
        if not SR_AVAILABLE:
            raise ImportError("SpeechRecognition not installed. Run: pip install SpeechRecognition")
        
        self.recognizer = sr.Recognizer()
        self.microphone = None
    
    def listen(self, timeout: int = 5, phrase_time_limit: int = 10) -> Optional[str]:
        """
        Listen for speech and convert to text.
        
        Args:
            timeout: Maximum time to wait for speech to start
            phrase_time_limit: Maximum time for phrase
            
        Returns:
            Recognized text or None if failed
        """
        try:
            with sr.Microphone() as source:
                print("Listening...")
                # Adjust for ambient noise
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                
                # Listen for audio
                audio = self.recognizer.listen(
                    source,
                    timeout=timeout,
                    phrase_time_limit=phrase_time_limit
                )
                
                print("Processing speech...")
                # Recognize speech using Google Speech Recognition
                text = self.recognizer.recognize_google(audio)
                return text
                
        except sr.WaitTimeoutError:
            print("No speech detected within timeout period.")
            return None
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return None
        except sr.RequestError as e:
            print(f"Speech recognition service error: {e}")
            return None
        except Exception as e:
            print(f"Error during speech recognition: {e}")
            return None


class VoiceAssistant:
    """Combined voice assistant with both TTS and STT capabilities"""
    
    def __init__(self, tts_engine: str = "auto", enable_stt: bool = True):
        """
        Initialize voice assistant.
        
        Args:
            tts_engine: TTS engine to use ('pyttsx3', 'gtts', or 'auto')
            enable_stt: Whether to enable speech-to-text
        """
        self.tts = TextToSpeech(engine=tts_engine)
        self.stt = SpeechToText() if enable_stt and SR_AVAILABLE else None
    
    def speak(self, text: str) -> bool:
        """Speak text"""
        return self.tts.speak(text)
    
    def listen(self, timeout: int = 5) -> Optional[str]:
        """Listen for speech input"""
        if not self.stt:
            print("Speech-to-text not available.")
            return None
        return self.stt.listen(timeout=timeout)
    
    def conversation_loop(self, response_callback: Callable[[str], str]):
        """
        Run interactive voice conversation loop.
        
        Args:
            response_callback: Function that takes user input and returns response
        """
        if not self.stt:
            print("Speech-to-text not available. Cannot run conversation loop.")
            return
        
        self.speak("Hello! I'm Lisa. How can I help you today?")
        
        while True:
            # Listen for user input
            user_input = self.listen()
            
            if not user_input:
                continue
            
            print(f"You said: {user_input}")
            
            # Check for exit commands
            if any(word in user_input.lower() for word in ['goodbye', 'bye', 'exit', 'quit']):
                self.speak("Goodbye! Have a great day!")
                break
            
            # Get response from callback
            response = response_callback(user_input)
            print(f"Lisa: {response}")
            
            # Speak response
            self.speak(response)


def test_voice_features():
    """Test voice interaction features"""
    print("=== Voice Interaction Module Test ===")
    print(f"pyttsx3 available: {PYTTSX3_AVAILABLE}")
    print(f"gTTS available: {GTTS_AVAILABLE}")
    print(f"SpeechRecognition available: {SR_AVAILABLE}")
    print()
    
    # Test TTS
    try:
        tts = TextToSpeech()
        print(f"Using TTS engine: {tts.engine_type}")
        print("Testing text-to-speech...")
        tts.speak("Hello! I am Lisa, your voice assistant.")
        print("TTS test completed.\n")
    except Exception as e:
        print(f"TTS test failed: {e}\n")
    
    # Test STT
    if SR_AVAILABLE:
        try:
            print("Testing speech-to-text...")
            print("Please speak something (you have 5 seconds):")
            stt = SpeechToText()
            text = stt.listen(timeout=5)
            if text:
                print(f"You said: {text}")
            print("STT test completed.\n")
        except Exception as e:
            print(f"STT test failed: {e}\n")


if __name__ == "__main__":
    test_voice_features()
