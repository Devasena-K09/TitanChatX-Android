# ai_assistant.py - Futuristic AI for TitanChatX

import random

def get_ai_reply(user_msg):
    msg = user_msg.lower()

    # Custom replies based on keywords
    if "hello" in msg or "hi" in msg:
        return "👋 Hey! TitanChatX AI at your service."
    elif "game" in msg:
        return "🎮 Ready to deploy you into battle mode!"
    elif "free fire" in msg:
        return "🔥 Free Fire mode engaged. Lock and load!"
    elif "bye" in msg:
        return "👋 See you soon, warrior!"
    elif "love" in msg:
        return "❤️ Love detected. Emotions: MAXIMUM."
    else:
        # Random futuristic reply
        return random.choice([
            "🤖 Processing… complete. You’re awesome!",
            "🚀 Mission parameters updated successfully.",
            "⚡ Energy levels optimal. Proceed.",
            "🛡️ Shields up, Captain!"
        ])
