import json
import random

# Load the JSON data from the intents2.json file
with open('intents2.json', 'r') as file:
    intents = json.load(file)['intents']

# Process the intents and build a dictionary to map patterns to their respective responses
patterns_responses = {}

for intent in intents:
    patterns = intent.get('patterns', [])
    responses = intent.get('responses', [])
    for pattern in patterns:
        patterns_responses[pattern] = responses

# Chatbot logic to handle user input and generate responses
def chatbot_response(user_input):
    for pattern, responses in patterns_responses.items():
        if pattern.lower() in user_input.lower():
            return random.choice(responses)
    return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Chat loop
print("Bot: Hello! How can I assist you?")
while True:
    user_input = input("User: ")
    if user_input.lower() in ['exit', 'end', 'quit']:
        print("Bot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Bot:", response)
