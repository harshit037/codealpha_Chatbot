def chatbot():
    print("===================================")
    print(" SIMPLE CHATBOT PROJECT ")
    print("===================================")
    print("Type 'bye' to exit the chatbot.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello" or user_input == "hi":
            print("Bot: Hi! How can I help you?")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user_input == "what is your name":
            print("Bot: My name is ChatBot.")

        elif user_input == "help":
            print("Bot: I can chat with you. Try saying hello!")

        elif user_input == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")


chatbot()
