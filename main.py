print("TitanChatX is running!")
print("Type 'quit' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Bot: Goodbye! 👋")
        break
    elif "hi" in user_input.lower():
        print("Bot: Hello! How can I help you today?")
    elif "how are you" in user_input.lower():
        print("Bot: I'm just a bot, but I'm doing great! 😄")
    else:
        print("Bot: I'm not sure how to respond to that.")
