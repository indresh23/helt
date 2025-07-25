# Required Imports
from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

# Configure the Google Generative AI API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the Gemini model (latest valid model ID)
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to get model output
def my_output(query: str) -> str:
    response = model.generate_content(query)
    return response.text

# Streamlit UI
st.set_page_config(page_title="your_bot")
st.header("your_bot")

# Input field
input = st.text_input("Input", key="input")
submit = st.button("Ask your query")

# On submit
if submit:
    response = my_output(input)
    st.subheader("The Response is:")
    st.write(response)
