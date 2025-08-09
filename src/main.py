import time

def ascii_logo():
    print(r"""
████████╗██╗████████╗ █████╗ ███╗   ██╗ ██████╗██╗  ██╗██╗   ██╗
╚══██╔══╝██║╚══██╔══╝██╔══██╗████╗  ██║██╔════╝██║  ██║╚██╗ ██╔╝
   ██║   ██║   ██║   ███████║██╔██╗ ██║██║     ███████║ ╚████╔╝ 
   ██║   ██║   ██║   ██╔══██║██║╚██╗██║██║     ██╔══██║  ╚██╔╝  
   ██║   ██║   ██║   ██║  ██║██║ ╚████║╚██████╗██║  ██║   ██║   
   ╚═╝   ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   
          Fusion of WhatsApp + Free Fire + Futuristic AI
    """)

def launch_screen():
    ascii_logo()
    print("-------------------------------------------------------------")

def fake_chat():
    print("\n💬 TitanChatX AI Chat Mode")
    print("Type 'exit' to return to the main menu.\n")
    while True:
        user_msg = input("You: ")
        if user_msg.lower() == "exit":
            print("Exiting Chat Mode...\n")
            break
        else:
            time.sleep(0.5)
            print(f"TitanAI: Processing '{user_msg}' ... 🤖")
            time.sleep(1)
            print(f"TitanAI: Reply feature coming soon! Stay tuned 🚀\n")

def fake_game_lobby():
    print("\n🎮 TitanChatX Game Lobby")
    print("Loading Free Fire-style futuristic lobby...")
    time.sleep(1)
    print("🕹 Players Online: 256")
    print("🔥 Current Map: Neo-Battleground")
    print("⚔ Upcoming Event: Titan Wars\n")
    time.sleep(1)
    input("Press Enter to return to the main menu...")

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Chat Mode")
        print("2. Game Lobby")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            fake_chat()
        elif choice == "2":
            fake_game_lobby()
        elif choice == "3":
            print("\nExiting TitanChatX. See you soon! 👋")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    launch_screen()
    main_menu()

from chat import start_chat

print("1. Chat Mode")
print("2. Game Lobby")
print("3. Exit")

choice = input("Select option: ")

if choice == "1":
    start_chat()
elif choice == "2":
    print("🎮 Game Lobby Coming Soon...")
elif choice == "3":
    print("👋 Goodbye!")
else:
    print("❌ Invalid Option")
