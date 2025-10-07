print("Hello I am ChatPy")
print("type 'bye' to end the chat ")
print("Enter 'h' to show help \n")

while True:
    user_input = input("You: ").lower()
    
    if user_input == "hello" or user_input == "hi":
        print("ChatPy: Hey there! How can I help you today?")

    elif "h" == user_input:
        print(""" 
    commands    hello/hi
                how are you
                your name
                bye
        """)
    elif "how are you" in user_input:
        print("ChatPy: I'm doing great thanks for asking!")
    elif "your name" in user_input:
        print("ChatPy: I'm ChatPy, your python chatbot")
    elif "bye" in user_input:
        print("ChatPy: Goodbye! Have a great day!")
        break
    else:
        print("ChatPy: Sorry, I don't understand that yet")