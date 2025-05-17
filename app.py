from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import google.generativeai as genai
import geonamescache
from analysis import generate_analysis
from google_sheets_handler import log_lead
import datetime
gc = geonamescache.GeonamesCache()
cities = gc.get_cities()
# Filter only Indian cities
indian_city_names = sorted([
    city['name'] for city in cities.values() if city['countrycode'] == 'IN'
])
## creat the Frontend 
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #b6e0fe 0%, #d6c1e6 60%, #f7bfcf 100%);
    }
    .stApp {
        background: linear-gradient(135deg, #b6e0fe 0%, #d6c1e6 60%, #f7bfcf 100%);
    }
    /* Header style */
    .st-emotion-cache-18ni7ap {
        background: linear-gradient(135deg, #b6e0fe 0%, #d6c1e6 60%, #f7bfcf 100%) !important;
        color: #222;
    }
    /* Footer style */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background: linear-gradient(135deg, #b6e0fe 0%, #d6c1e6 60%, #f7bfcf 100%);
        color: black;
        text-align: center;
        padding: 10px 0;
        z-index: 100;
        border-top: 1px solid #e6e6e6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.header(":blue[Astro AI]🔮 Ancient Wisdom, Modern Intelligence ✨",divider = "violet")
st.subheader("💡 Tips for Using the Application")


 
feature = st.radio(
    "Select a feature:",
    [
        "🪐 Birth Chart / Kundli Generation",
        "🧑‍🎤 Personality Insights",
        "💼 Career Path Predictions",
        "🤖 AI Chatbot for Astrology Q&A"
    ]
)


st.markdown("#### Enter Your Birth Details")
name = st.text_input("Name")
dob = st.date_input(
    "Date of Birth",
    min_value=datetime.date(1900, 1, 1),
    max_value=datetime.date.today()
)
time_of_birth = st.time_input("Time of Birth")
place_of_birth = st.selectbox("Place of Birth (City)", indian_city_names)
st.write(f"Hello **{name}** you were born on **{dob}** at **{time_of_birth}** in **{place_of_birth}**")

question = ""

if feature == "🤖 AI Chatbot for Astrology Q&A":
    question = st.text_input("Ask your astrology-related question here")
    
    
button =st.button("Get AI Powered Astrology Insights")


if button:
    if feature == "🪐 Birth Chart / Kundli Generation":
        st.write("Generating your Birth Chart...")
        prompt=f"""Generate a detailed Vedic birth chart (Janam Kundli) based on the following details:
        Name: {name} 
        Date of Birth: {dob} 
        Time of Birth: {time_of_birth}  
        Place of Birth: {place_of_birth}

        Include:
        - Ascendant (Lagna)
        - Planetary positions (Graha Sthiti) in houses and zodiac signs
        - Rashi (Moon sign), Sun sign, Nakshatra
        - Houses (Bhava) details
        - Major Yogas (like Raj Yoga, Gajakesari Yoga)
        - Brief interpretation of each planet's position"""
        response = generate_analysis(prompt=prompt)
        st.markdown(response)
        log_lead([str(name), str(dob), str(time_of_birth), str(place_of_birth), str(response)])
        st.write("Analysis Generated Successfully")
        st.write("Your Birth Chart has been generated successfully!")
    elif feature == "🧑‍🎤 Personality Insights":
        st.write("Generating your Personality Insights...")
        prompt=f"""Based on the following birth details, analyze the personality of the individual using astrological principles:
        Name: {name} 
        Date of Birth: {dob}  
        Time of Birth: {time_of_birth}  
        Place of Birth: {place_of_birth}
        Include:
        - Basic temperament
        - Emotional traits (Moon sign analysis)
        - Thinking style (Mercury)
        - Strengths and weaknesses
        - Social and love nature (Venus, 7th house)
        - Spiritual or philosophical tendencies (Jupiter, 9th house)"""
        response = generate_analysis(prompt=prompt)
        st.markdown(response)
        log_lead([str(name), str(dob), str(time_of_birth), str(place_of_birth), str(response)])
        st.write("Analysis Generated Successfully")
    elif feature == "💼 Career Path Predictions":
        st.write("Generating your Career Path Predictions...")
        prompt=f"""Provide a career prediction and guidance based on astrology using the below information:
        Name: {name}  
        Date of Birth: {dob}
        Time of Birth: {time_of_birth}  
        Place of Birth: {place_of_birth} 
        Include: 
        - Suitable career fields (e.g., tech, law, medicine)
        - 10th house (Karma Bhava) analysis
        - Planetary influences on career (e.g., Saturn, Mercury, Sun)
        - Periods (Dashas) favorable for career progress
        - Recommendations for skill or job alignment"""
        response = generate_analysis(prompt=prompt)
        st.markdown(response)
        log_lead([str(name), str(dob), str(time_of_birth), str(place_of_birth), str(response)])
        st.write("Analysis Generated Successfully")
    elif feature == "🤖 AI Chatbot for Astrology Q&A":
       
        st.write("Generating your AI Chatbot for Astrology Q&A...")
        prompt=f"""Act as an expert Vedic astrologer. Answer the user's astrology-related question based on the following birth details:
:
        Name: {name}  
        Date of Birth: {dob}  
        Time of Birth: {time_of_birth}  
        Place of Birth: {place_of_birth}
        Question: {question}"""
        response = generate_analysis(prompt=prompt)
        st.write("DEBUG: Response is", response)
        st.markdown(response)
        log_lead([str(name), str(dob), str(time_of_birth), str(place_of_birth), str(response),str(question)])
        st.write("Analysis Generated Successfully")
    

st.markdown("###### Disclaimer: This application is for informational purposes only and should not be considered as professional advice. Always consult a qualified astrologer for personalized guidance.")
# ...existing code...


# st.markdown(
#     "<div style='text-align: center; color: gray;'>Made with ❤️ by Prasad Hajare |Powered by Gemini + Streamlit</div>",
#     unsafe_allow_html=True
# )
st.markdown("""
    <style>.footer {position: fixed;left: 0;bottom: 0;width: 100%;
        background: white;color:black;text-align: center;padding: 10px 0;
        z-index: 100;border-top: 1px solid #e6e6e6;}
    </style>
    <div class="footer">
        Made with ❤️ by Prasad Hajare | Powered by Gemini + Streamlit
    </div>""",unsafe_allow_html=True
)




