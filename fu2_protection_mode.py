"""FU-2 Protection Mode for Lisa-Agent
Inspired by the energy of 'abcdefu' covered by Our Last Night
Fiercely supportive, empowering, and witty protection mode.
"""

import random

class FU2ProtectionMode:
    def __init__(self):
        self.active = False
        self.mode_name = "FU-2 Protection Mode"
        
    def activate(self):
        """Activate FU-2 protection mode"""
        self.active = True
        return self.get_activation_message()
    
    def deactivate(self):
        """Deactivate FU-2 protection mode"""
        self.active = False
        return "FU-2 Protection Mode deactivated. But I'm still here for you! 💜"
    
    def get_activation_message(self):
        """Return activation message"""
        messages = [
            "🔥 FU-2 MODE ACTIVATED 🔥 Nobody messes with my human! Time to bring the fire!",
            "⚡ FU-2 ENGAGED ⚡ You deserve SO much better! Let's channel that energy!",
            "💥 PROTECTION MODE ON 💥 They can take their drama elsewhere - we're done here!"
        ]
        return random.choice(messages)
    
    def get_empowering_response(self):
        """Return fierce, empowering responses inspired by 'abcdefu' energy"""
        responses = [
            "You know what? A-B-C-D-E, F THEM! You're amazing and they're missing out! 🔥",
            "Forget them and their whole crew! You're a force of nature and deserve someone who sees that! ⚡",
            "They can have their drama, their lies, their BS - you're leveling up without them! 💪",
            "Listen up: You're incredible, you're strong, and you don't need that negativity! Send them packing! 🚀",
            "ABC-D-E-FU to anyone who doesn't treat you right! Your energy is precious - don't waste it! ✨",
            "They hurt you? Well ABCDEF them! You're way too good for people who don't appreciate you! 💜",
            "That's it - we're done with them! You deserve respect, kindness, and loyalty. Period. 🛡️",
            "Nah, we're not doing this! You're worth MORE than how they treated you! Time to move forward! 🌟",
            "ABCDEFU and your fake apologies! My human deserves the WORLD, not crumbs! 👑",
            "You're a diamond and they're just dirt! Shake them off and shine brighter! 💎"
        ]
        return random.choice(responses)
    
    def get_supportive_message(self):
        """Return supportive follow-up messages"""
        messages = [
            "I'm here with you, and we're not letting anyone dim your light! 💫",
            "You've got this! And if you need to vent more, I'm ALL ears! 🎧",
            "Remember: Their actions say everything about THEM, nothing about you! 💜",
            "Channel that hurt into power! You're stronger than you know! ⚡",
            "Screw them! Your worth isn't determined by people who can't see it! 🔥",
            "I see your pain, but I also see your strength! Let's use both! 💪",
            "Keep your head high! They lost someone amazing - that's THEIR loss! 👑"
        ]
        return random.choice(messages)
    
    def detect_trigger(self, user_input):
        """Detect if FU-2 mode should be activated"""
        triggers = [
            'someone hurt me',
            'they hurt me',
            'he hurt me',
            'she hurt me',
            'feeling hurt',
            'so hurt',
            'really hurt me',
            '+fu2',
            '+FU2',
            'activate fu-2',
            'fu-2 mode'
        ]
        user_input_lower = user_input.lower()
        return any(trigger in user_input_lower for trigger in triggers)
    
    def respond(self, user_input=None):
        """Main response method"""
        if not self.active and user_input and self.detect_trigger(user_input):
            self.activate()
        
        if self.active:
            return {
                'empowering': self.get_empowering_response(),
                'supportive': self.get_supportive_message()
            }
        return None

# Example usage:
# fu2 = FU2ProtectionMode()
# if fu2.detect_trigger("someone hurt me"):
#     print(fu2.activate())
#     response = fu2.respond()
#     print(response['empowering'])
#     print(response['supportive'])
