import json
import re

def load_intents():
    with open("data/intents.json") as f:
        return json.load(f)

def classify_intent(user_input, intents_data):
    user_input = user_input.lower()
    for intent, patterns in intents_data.items():
        for pattern in patterns:
            if re.search(rf"\b{pattern}\b", user_input):
                return intent
    return "unknown"
