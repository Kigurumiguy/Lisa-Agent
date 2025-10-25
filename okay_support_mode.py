# okay_support_mode.py
# "It's Going To Be Okay" Support Mode
# Inspired by "Perfect" by Emma Blackery

import random

class OkaySupportMode:
    def __init__(self):
        self.is_active = False
        self.trigger_phrases = [
            "i'm feeling down",
            "i feel worthless",
            "i'm not good enough",
            "i feel like giving up",
            "everything is falling apart",
            "i can't do this",
            "i'm so tired",
            "i feel hopeless",
            "nothing matters",
            "i'm struggling",
            "i feel awful",
            "i'm sad"
        ]
        
        self.affirmations = [
            "Hey, I know things feel heavy right now, but you're stronger than you think. It's going to be okay.",
            "You don't have to be perfect. You're doing your best, and that's more than enough. Things will get better.",
            "I see you trying, even when it's hard. That takes courage. It's going to be okay.",
            "Some days are tougher than others, and that's completely okay. Tomorrow is a new chance. You've got this.",
            "You're not alone in feeling this way. It's okay to struggle sometimes. But remember - it's going to be okay.",
            "Your worth isn't determined by your productivity or perfection. You matter, just as you are. And it's going to be okay.",
            "Take a deep breath. Feel that? You're still here, still fighting. That's incredibly brave. It's going to be okay.",
            "Bad moments don't make a bad life. This feeling is temporary, even if it doesn't feel like it right now. It's going to be okay.",
            "You've survived 100% of your worst days so far. You're more resilient than you know. It's going to be okay.",
            "It's okay to not be okay right now. But please remember: you deserve kindness, especially from yourself. Things will get better.",
            "You don't need to have it all figured out. Just take it one step at a time. I believe in you, and it's going to be okay.",
            "Whatever you're facing, you don't have to face it alone. Reach out when you need to. And remember - it's going to be okay."
        ]
        
        self.follow_ups = [
            "Remember to be gentle with yourself today. 💙",
            "You're doing better than you think you are.",
            "Take it one moment at a time. That's all you need to do.",
            "I'm here if you need to talk more. You matter.",
            "Don't forget: progress isn't always linear, and that's okay.",
            "You deserve compassion and understanding - from others and from yourself."
        ]
    
    def activate(self):
        """Activate the support mode"""
        self.is_active = True
        return "✨ 'It's Going To Be Okay' support mode activated. I'm here for you."
    
    def deactivate(self):
        """Deactivate the support mode"""
        self.is_active = False
        return "Support mode deactivated. Remember: you're stronger than you know. 💙"
    
    def check_triggers(self, message):
        """Check if message contains trigger phrases"""
        message_lower = message.lower()
        for trigger in self.trigger_phrases:
            if trigger in message_lower:
                return True
        return False
    
    def get_support_response(self):
        """Generate a supportive response"""
        affirmation = random.choice(self.affirmations)
        follow_up = random.choice(self.follow_ups)
        return f"{affirmation}\n\n{follow_up}"
    
    def process_message(self, message):
        """Process message and return appropriate response"""
        # Check for activation command
        if "+OKAY" in message.upper():
            return self.activate()
        
        # Check for deactivation command
        if "+OKAY OFF" in message.upper():
            return self.deactivate()
        
        # If mode is active or triggers detected, provide support
        if self.is_active or self.check_triggers(message):
            return self.get_support_response()
        
        return None

# Example usage
if __name__ == "__main__":
    support = OkaySupportMode()
    
    # Test activation
    print(support.process_message("+OKAY"))
    print()
    
    # Test support response
    print(support.process_message("I need help"))
    print()
    
    # Test deactivation
    print(support.process_message("+OKAY OFF"))
