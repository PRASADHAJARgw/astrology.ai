import google.generativeai as genai

import streamlit as st
import os
genai.configure(api_key=os.getenv("GOOGLE_GEMINI_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_analysis(prompt):
    if prompt is not None:
        response = model.generate_content(prompt)
        return response.text  # <-- Return only the text!
    else:
        st.warning("Could not generate your Birth Chart...")
        return ""  # Return empty string if prompt is None