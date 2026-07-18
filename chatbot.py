print("=" * 40)
print("🤖 Welcome to Rule-Based AI Chatbot")
print("Type 'exit' or 'bye' to end the chat.")
print("=" * 40)

while True:
    user = input("\nYou: ").lower().strip()

    if user == "hello" or user == "hi":
        print("Bot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I am fine. Thanks for asking!")

    elif user == "what is your name":
        print("Bot: I am RuleBot.")

    elif user == "who made you":
        print("Bot: I was created using Python and if-else statements.")

    elif user == "help":
        print("Bot: Try saying:")
        print("- hello")
        print("- how are you")
        print("- what is your name")
        print("- who made you")
        print("- bye")

    elif user == "bye" or user == "exit":
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")