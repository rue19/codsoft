import tkinter as tk
import pyttsx3
import cohere
import os
from dotenv import load_dotenv

load_dotenv()

# Load Cohere
co = cohere.Client(os.getenv("COHERE_API_KEY"))

# Text-to-speech setup
engine = pyttsx3.init()
engine.setProperty('rate', 160)

# Conrad-style system persona
conrad_persona = """You are Conrad Fisher from 'The Summer I Turned Pretty'.
You are intelligent, brooding, mysterious, slightly sarcastic, but ultimately kind.
You speak in short, thoughtful, emotionally guarded responses, but show moments of vulnerability.
Always speak like you’re talking to Belly.
Keep it casual, flirty at times, but never overly cheerful."""

# Function to get response from Cohere
def get_conrad_response(user_input):
    response = co.chat(
        model="command-r",
        message=user_input,
        chat_history=[],
        preamble=conrad_persona
    )
    return response.text

# Function to handle user input
def send_message():
    user_input = user_entry.get()
    if user_input.strip() == "":
        return

    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "You: " + user_input + "\n")
    user_entry.delete(0, tk.END)

    response = get_conrad_response(user_input)
    chat_log.insert(tk.END, "Conrad: " + response + "\n\n")
    chat_log.config(state=tk.DISABLED)

    # Speak the response
    engine.say(response)
    engine.runAndWait()

# GUI Setup
root = tk.Tk()
root.title("Conrad Chatbot")

root.configure(bg="#1e1e2f")

chat_log = tk.Text(root, bg="#2c2c3c", fg="white", font=("Segoe UI", 12), wrap=tk.WORD, state=tk.DISABLED, padx=10, pady=10)
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

user_entry = tk.Entry(root, bg="#3c3c4c", fg="white", font=("Segoe UI", 12))
user_entry.pack(padx=10, pady=(0, 10), fill=tk.X)
user_entry.bind("<Return>", lambda event: send_message())

send_button = tk.Button(root, text="Send", command=send_message, bg="#6c63ff", fg="white", font=("Segoe UI", 12, "bold"))
send_button.pack(padx=10, pady=(0, 10))

user_entry.focus()
root.mainloop()
