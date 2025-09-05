responses = {
    "hi": "Hello! How can I help you?",
    "how are you": "I'm doing well, thank you!",
    "bye": "Goodbye! Have a nice day!"
}

def chatbot():
    print("Chatbot started (type 'exit' to stop):")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'exit':
            print("Chatbot stopped.")
            break
        response = responses.get(user_input, "Sorry, I don't understand.")
        print("Bot:", response)

chatbot()
