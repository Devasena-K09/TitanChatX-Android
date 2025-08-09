# lobby.py - Free Fire style matchmaking simulation

import time
import random

avatars = ["🔥", "💀", "⚡", "🦅", "🎯", "🛡️"]

def start_lobby():
    print("\n🎮 Free Fire Fusion Mode - TitanChatX\n")
    username = input("Enter your in-game name: ")
    avatar = random.choice(avatars)
    print(f"\nWelcome {username}! Your avatar: {avatar}")
    
    print("\n⏳ Searching for players...")
    players = []
    for i in range(1, 6):  # Simulating 5 other players
        time.sleep(random.uniform(0.8, 1.5))
        new_player = f"Player_{random.randint(1000,9999)} {random.choice(avatars)}"
        players.append(new_player)
        print(f"✅ {new_player} joined the lobby")

    print("\n🔥 All players ready! Match starting in...")
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)

    print("\n🚀 Match Started! Good luck, warrior!")
