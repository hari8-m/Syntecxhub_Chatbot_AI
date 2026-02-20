print("AI Chatbot Started (type 'bye' to exit)\n")

chat_history = []

while True:
    user = input("You: ").lower()
    chat_history.append("User: " + user)

    if user in ["hi", "hello", "hey"]:
        reply = "Hello! How can I help you today?"

    elif "your name" in user:
        reply = "I am a simple AI chatbot created for internship project."

    elif "help" in user:
        reply = "You can ask me about AI, internship, or general questions."

    elif "ai" in user:
        reply = "Artificial Intelligence is the simulation of human intelligence by machines."

    elif "internship" in user:
        reply = "This internship helps students gain practical knowledge and skills."

    elif "thank" in user:
        reply = "You're welcome!"

    elif user == "bye":
        reply = "Goodbye! Have a great day!"
        print("Bot:", reply)
        chat_history.append("Bot: " + reply)
        break

    else:
        reply = "Sorry, I don't understand that yet."

    print("Bot:", reply)
    chat_history.append("Bot: " + reply)

print("\nConversation History:")
for line in chat_history:
    print(line)
