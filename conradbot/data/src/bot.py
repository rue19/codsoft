import json
import random
from src.nlp_utils import load_intents, classify_intent

with open("data/quotes.json") as f:
    responses = json.load(f)

intents = load_intents()

def get_response(user_input):
    intent = classify_intent(user_input, intents)
    if intent in responses:
        return random.choice(responses[intent])
    else:
        return "I don’t know what to say to that. Maybe some things are better left unsaid."
