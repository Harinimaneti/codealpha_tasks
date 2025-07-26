## 🧠 Simple Rule-Based Chatbot in Python

This project is a basic *text-based rule-driven chatbot* written in Python. It demonstrates fundamental concepts like conditionals, loops, user input handling, and basic functions.

### 📋 Features

* Responds to specific user inputs such as:

  * "hello" → "Hi!"
  * "how are you" → "I'm fine, thanks!"
  * "bye" or "exit" → ends the chat
* Handles unknown inputs with a default response.
* Continuous conversation using a while loop.
* Case-insensitive user input using .lower().

### 📌 How It Works

1. The chatbot() function starts by welcoming the user.
2. It enters a loop to repeatedly take user input.
3. Based on the input, it checks predefined conditions using if-elif-else:

   * If the input matches a known phrase, the bot gives a predefined reply.
   * If the user types "bye" or "exit", the loop ends, and the chat is closed.
   * For any unknown input, it replies with a generic message.
4. The bot continues the conversation until the user ends it.

### 🧪 Example Output


Welcome to ChatBot! Type 'exit' to end the chat.
You: hello
Bot: Hi!
You: how are you
Bot: I'm fine, thanks!
You: what's up
Bot: Sorry, I don't understand that.
You: bye
Bot: Goodbye!


### 🛠 Key Python Concepts Used

* if-elif-else statements
* while loops
* String manipulation using .lower()
* Basic input/output operations

### 🚀 Getting Started

To run the chatbot:

bash
python chatbot.py
