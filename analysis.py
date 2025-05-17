import google.generativeai as genai

import streamlit as st
import os
genai.configure(api_key=os.getenv("GOOGLE_GEMINI_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_analysis(prompt):
    if prompt is not None:
       st.markdown("")
    else:
        st.warning("Could not  your Birth Chart...")
    response = model.generate_content(prompt)
    return (st.write(response.text))
