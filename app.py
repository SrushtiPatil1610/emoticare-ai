import streamlit as st
import random

st.set_page_config(page_title="EmotiCare AI", page_icon="🧠")

st.title("EmotiCare AI 🧠💬")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("How are you feeling today?")

def detect_emotion(text):
    text = text.lower()
    if any(word in text for word in ["sad", "depressed", "unhappy"]):
        return "Sadness"
    elif any(word in text for word in ["happy", "excited", "joy"]):
        return "Joy"
    elif any(word in text for word in ["angry", "frustrated"]):
        return "Anger"
    elif any(word in text for word in ["tired", "stressed", "overwhelmed"]):
        return "Stress"
    else:
        return "Neutral"

def generate_response(emotion):
    responses = {
        "Sadness": [
            "I'm really sorry you're feeling this way 💙 Want to talk about it?",
            "That sounds tough… I'm here to listen 🤍",
            "You're not alone. I'm here with you."
        ],
        "Joy": [
            "That's amazing! What made your day so good? 😊",
            "Love that energy! Tell me more 🌟",
            "That’s great to hear! Keep it up 😄"
        ],
        "Anger": [
            "Take a deep breath. You got this 💪",
            "It's okay to feel angry, but try to relax a bit.",
            "Want to talk about what’s bothering you?"
        ],
        "Stress": [
            "Sounds like you need a break 😌 Try to relax for a bit.",
            "Take it one step at a time. You’re doing your best 💛",
            "Maybe a short break or deep breathing might help."
        ],
        "Neutral": [
            "That’s interesting. Can you tell me more?",
            "I'm listening… go on.",
            "Thanks for sharing. What else is on your mind?"
        ]
    }
    return random.choice(responses[emotion])

# When user sends message
if st.button("Send") and user_input:
    emotion = detect_emotion(user_input)
    response = generate_response(emotion)

    st.session_state.messages.append(("You", user_input))
    st.session_state.messages.append(("AI", f"{response}\n\nEmotion detected: {emotion}"))

# Display chat
for sender, msg in st.session_state.messages:
    st.write(f"**{sender}:** {msg}")