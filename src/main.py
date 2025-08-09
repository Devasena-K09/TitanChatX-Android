from chat import start_chat
from lobby import start_lobby

print("\n████████╗██╗████████╗ █████╗ ███╗   ██╗ ██████╗██╗  ██╗██╗   ██╗")
print("╚══██╔══╝██║╚══██╔══╝██╔══██╗████╗  ██║██╔════╝██║  ██║╚██╗ ██╔╝")
print("   ██║   ██║   ██║   ███████║██╔██╗ ██║██║     ███████║ ╚████╔╝ ")
print("   ██║   ██║   ██║   ██╔══██║██║╚██╗██║██║     ██╔══██║  ╚██╔╝  ")
print("   ██║   ██║   ██║   ██║  ██║██║ ╚████║╚██████╗██║  ██║   ██║   ")
print("   ╚═╝   ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ")
print(" Fusion of WhatsApp + Free Fire + Futuristic AI - TitanChatX")

while True:
    print("\n1. Chat Mode")
    print("2. Game Lobby")
    print("3. Exit")

    choice = input("Select option: ")

    if choice == "1":
        start_chat()
    elif choice == "2":
        start_lobby()
    elif choice == "3":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid Option")
