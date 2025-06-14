"""
Basic Chatbot using NLTK
"""

import nltk
import random
import string

# Download necessary NLTK resources
nltk.download('punkt')

# Predefined responses
responses = {
    "hello": "Hi there! How can I help you?",
    "how are you": "I'm just a bot, but I'm doing great! How can I assist you?",
    "bye": "Goodbye! Have a great day!",
    "default": "Sorry, I didn't understand that. Can you rephrase?"
}

# Function to clean and process user input
def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# Simple chatbot function
def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        user_input = preprocess(user_input)

        if user_input == "bye":
            print("Chatbot: " + responses["bye"])
            break
        elif user_input in responses:
            print("Chatbot: " + responses[user_input])
        else:
            print("Chatbot: " + responses["default"])

if __name__ == "__main__":
    chatbot()
