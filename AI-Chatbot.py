import os
import requests
import streamlit as st
from dotenv import load_dotenv

# API token
load_dotenv()
API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

st.title("AI Chatbot with Hugging Face & Streamlit")

user_input = st.text_input("You:")

if st.button("Send") and user_input:
    with st.spinner("Thinking..."):
        try:
            response = requests.post(
                API_URL,
                headers={"Authorization": f"Bearer {API_TOKEN}"},
                json={"inputs": user_input}
            )
            data = response.json()

            if isinstance(data, list) and "generated_text" in data[0]:
                st.write("**Bot:**", data[0]["generated_text"])
            
            elif "error" in data:
                st.write("**Bot:**", "API Error: " + data["error"])
            else:
                st.write("**Bot:**", "Unexpected response from API.")

        except Exception as e:
            st.write("**Bot:**", f"An error occurred: {e}")
