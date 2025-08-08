import time

def launch_screen():
    print("🚀 Welcome to TitanChatX 🚀")
    print("Fusion of WhatsApp + Free Fire + Futuristic AI")
    print("---------------------------------------------")

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Chat Mode")
        print("2. Game Lobby")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            print("\n💬 [Chat Mode]")
            print("Chat system coming soon... Stay tuned!")
            time.sleep(1)
        elif choice == "2":
            print("\n🎮 [Game Lobby]")
            print("Gaming integration under development...")
            time.sleep(1)
        elif choice == "3":
            print("\nExiting TitanChatX. See you soon! 👋")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    launch_screen()
    main_menu()
