import json
import random
import re

# Load intents from a JSON file
intents = json.loads(open('intents.json').read())

def get_response(intents, user_input):
    user_input = user_input.lower()

    for intent in intents['intents']:
        for pattern in intent['patterns']:
            if re.search(pattern, user_input):
                return random.choice(intent['responses'])

    return "I'm sorry, but I'm not sure how to help with that."

# Test the chatbot
while True:
    user_input = input("User: ")
    response = get_response(intents, user_input)
    print("Chatbot:", response)
