def get_bot_response(user_input):
    """Processes user input and returns a predefined response."""
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return "Hi!"
    elif user_input in ["how are you", "how are you?", "how's it going"]:
        return "I'm fine, thanks!"
    elif user_input in ["what is your name", "what's your name", "who are you"]:
        return "I am a simple rule-based chatbot."
    elif user_input in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye!"
    else:
        return "I'm sorry, I don't understand that phrase yet."

def run_chatbot():
    print("=== Simple Rule-Based Chatbot ===")
    print("Type 'bye' or 'exit' to end the chat.\n")

    while True:
        user_msg = input("You: ")
        response = get_bot_response(user_msg)
        print(f"Bot: {response}")

        if user_msg.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
            break

if __name__ == "__main__":
    run_chatbot()