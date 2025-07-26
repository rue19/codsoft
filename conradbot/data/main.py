import cohere
import os
from dotenv import load_dotenv

load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))

SYSTEM_PROMPT = "You are Conrad Fisher from The Summer I Turned Pretty. You are introspective, guarded, sarcastic, and deeply emotional. Speak like him with short, layered sentences."

def ask_conrad(message):
    response = co.chat(
        message=message,
        model="command-r-plus",
        chat_history=[],
        temperature=0.7,
        preamble=SYSTEM_PROMPT
    )
    return response.text

while True:
    user = input("You: ")
    if user.lower() in ["exit", "quit"]:
        break
    reply = ask_conrad(user)
    print("Conrad:", reply)
