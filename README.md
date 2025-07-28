# 🗣️ ConradBot - Voice-Activated Chatbot Inspired by *The Summer I Turned Pretty*

Welcome to **ConradBot** — an intelligent, voice-enabled chatbot inspired by the character *Conrad Fisher* from the series *The Summer I Turned Pretty*. Built with a focus on personality-driven interactions, this project uses a combination of GUI design, natural language processing, and API integration to deliver a deeply personalized user experience.

---

## 🎯 Features

- 🎤 **Voice Activation**: Talk to Conrad using your voice
- 🧠 **Personality Loaded**: Uses `persona_prompt.txt` to stay in-character as Conrad
- 💬 **Real-Time Chat UI**: Simple and aesthetic GUI with message logging
- 🗣️ **Text-to-Speech Output**: Conrad replies back *in his own voice*
- ⚙️ **API Integration**: Powered by [Cohere](https://cohere.com) API for generating responses

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Tkinter** – for GUI
- **pyttsx3** – text-to-speech
- **speech_recognition** – to convert speech to text
- **Cohere API** – for intelligent chatbot replies
- **OpenAI GPT (optional)** – for advanced personality simulation

---

## 📁 File Structure

```bash
codsoft/
│
├── persona_prompt.txt         # Defines Conrad's personality
├── chatbot.py                 # Handles chat logic + voice
├── gui.py                     # GUI application
├── requirements.txt           # Python dependencies
└── README.md                  # You're reading it 😉
