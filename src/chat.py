# chat.py - WhatsApp-style chat simulation

import random
import time

# Contact list
contacts = ["Riya", "Aarav", "Tuti-Bot 🤖", "FreeFire Buddy 🔫"]

# Pre-set AI replies
replies = [
    "Haan bolo...",
    "Abhi busy hu, baad me msg karna.",
    "😂😂😂",
    "Kya baat hai, tum serious lag rahi ho!",
    "Mission ready hai, bas tumhara signal chahiye 🚀",
    "Lekin tum jeet paogi? 😏"
]

def start_chat():
    print("\n📱 WhatsApp Fusion Mode - TitanChatX\n")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact}")

    choice = input("\nKisse chat karna chahoge? (number): ")
    try:
        contact_index = int(choice) - 1
        if 0 <= contact_index < len(contacts):
            chat_with(contacts[contact_index])
        else:
            print("❌ Invalid choice!")
    except ValueError:
        print("❌ Please enter a number!")

def chat_with(contact):
    print(f"\n💬 Chat started with {contact}")
    print("Type 'exit' to go back.\n")
    while True:
        msg = input("You: ")
        if msg.lower() == "exit":
            break
        if msg.strip() == "":
            print("❌ Please type something!")
            continue
        print("Typing...", end="\r")
        time.sleep(random.uniform(0.5, 1.5))
        from ai_assistant import get_ai_reply
print(f"{contact}: {get_ai_reply(msg)}")
