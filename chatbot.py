def chatbot():
    print("Welcome to ChatBot! Type 'exit' to end the chat.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "hello":
            print("Bot: Hi!")
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Bot: Goodbye!")
            break
        elif user_input == "exit":
            print("Bot: Chat ended. Have a great day!")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()
