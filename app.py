import streamlit as st
import requests

st.title("📊 Stock AI Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.write(msg)

user_input = st.text_input("Ask about stocks...")

if st.button("Send"):
    if user_input:
        st.session_state.messages.append(f"You: {user_input}")

        try:
            res = requests.post(
                "http://127.0.0.1:5000/chat",
                json={"message": user_input}
            )
            data = res.json()
            bot_reply = data.get("response", "No response")

        except Exception as e:
            bot_reply = f"Error: {e}"

        st.session_state.messages.append(f"Bot: {bot_reply}")
        st.rerun()