from google import genai
from dotenv import load_dotenv
from time import sleep

import streamlit as st
st.set_page_config(
    page_title=" AI Travel Assistant by Ayush", page_icon="✈️", layout="wide"
)

# 2. Custom CSS with the New Travel Live Background
st.markdown(
    """
    <style>
    /* Import Modern Font */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        color: #ffffff !important;
    }

    /* ✨ New Sunset Horizon & Ocean Breeze Live Animated Background */
    @keyframes sunsetTravel {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .stApp {
        background: linear-gradient(-45deg, #0f172a, #1e1b4b, #831843, #0284c7, #0f766e);
        background-size: 400% 400%;
        animation: sunsetTravel 18s ease infinite;
    }

    /* Glassmorphism Card Containers */
    .card-box {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.07), rgba(255, 255, 255, 0.02));
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 20px;
        padding: 24px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
        margin-bottom: 20px;
    }

    /* Style Streamlit Inputs */
    div.stTextInput input {
        background-color: rgba(15, 23, 42, 0.65) !important;
        color: #ffffff !important;
        border: 1.5px solid rgba(255, 255, 255, 0.18) !important;
        border-radius: 14px !important;
        padding: 14px 18px !important;
        font-size: 15px !important;
        transition: all 0.3s ease !important;
    }

    div.stTextInput input:focus {
        border-color: #38bdf8 !important;
        box-shadow: 0 0 18px rgba(56, 189, 248, 0.4) !important;
        background-color: rgba(15, 23, 42, 0.85) !important;
    }

    /* Custom Button Style */
    .stButton button {
        background: linear-gradient(135deg, #0284c7, #38bdf8);
        color: white;
        border: none;
        border-radius: 14px;
        padding: 12px 24px;
        font-weight: 700;
        font-size: 16px;
        width: 100%;
        box-shadow: 0 4px 15px rgba(2, 132, 199, 0.4);
        transition: all 0.3s ease;
    }

    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 22px rgba(56, 189, 248, 0.6);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 3. App Header UI
st.markdown(
    """
    <div class="card-box">
        <h1 style="margin:0; font-size: 28px;">✈️  AI Travel Assistant by Ayush</h1>
        <p style="color: #cbd5e1; margin-top: 8px; margin-bottom: 0;">Your intelligent companion for creating bespoke travel itineraries.</p>
    </div>
    """,
    unsafe_allow_html=True,
)
st.title("🌍 Travel Assistant")
st.markdown(
    """
    <style>
    /* Glassmorphism Card Style */
    .travel-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.08), rgba(255, 255, 255, 0.02));
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 20px;
        padding: 24px;
        color: #ffffff;
        box-shadow: 0 10px 30px 0 rgba(0, 0, 0, 0.3);
        margin-bottom: 20px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .travel-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px 0 rgba(0, 0, 0, 0.4);
        border-color: rgba(0, 210, 255, 0.4);
    }
    
    /* Neon/Soft Tag Badge */
    .travel-badge {
        background: rgba(0, 210, 255, 0.15);
        color: #00d2ff;
        padding: 5px 14px;
        border-radius: 50px;
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        display: inline-block;
        margin-bottom: 12px;
    }
    
    /* Title & Description Typography */
    .travel-title {
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 8px;
        color: #ffffff;
        letter-spacing: 0.5px;
    }
    
    .travel-desc {
        font-size: 14px;
        color: #cbd5e1;
        line-height: 1.6;
        margin-bottom: 18px;
    }
    
    /* Meta Information Footer */
    .travel-meta {
        display: flex;
        gap: 20px;
        font-size: 13px;
        color: #94a3b8;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        padding-top: 14px;
    }
    
    .travel-meta span {
        display: flex;
        align-items: center;
        gap: 6px;
    }
    </style>

    <!-- HTML Template for the Card -->
    <div class="travel-card">
        <span class="travel-badge">✨ AI Recommended Escape</span>
        <div class="travel-title">🌴 Welcome, User</div>
        <div class="travel-desc">
            IWelcome to Travel Assistant made by Ayush Yerawar with lots of paitente and efforts by gemini.
        </div>
        <div class="travel-meta">
            <span>☀️ 28°C Sunny</span>
            <span>⭐ 4.9/5.0 (3.2k reviews)</span>
            <span>💰 From $450/week</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
load_dotenv()
client = genai.Client()
with open("chat.txt","r") as f:
     history=f.read()
query= st.text_input(
    label="Search Destination",
    placeholder="Where You Wanna Go?  ",
    label_visibility="collapsed",
)

# Dynamic response handler based on user input
if query:
  st.success(
      f"✨ Crafting your custom itinerary for **{query}**. Hang tight!"
  )

days = st.text_input(
    label="Trip Duration in Days",
    placeholder="Enter your number of dayss",
    label_visibility="collapsed",
)

# Input Validation & Action Handling using 'days'
if days:
  if days.isdigit() and int(days) > 0:
    st.success(f"🗓️ Perfect! Crafting a customized **{days}-day** action plan.")
  else:
    st.error("⚠️ Please enter a valid positive number (e.g., 3, 7, 10).")

if st.button("Plan Trip"):
      with st.spinner("Planning Your Trip..."):
         sleep(12)

history= history+ "user  :"+ query

while True:
    interaction = client.interactions.create(
        model="gemini-3.5-flash-lite",
        input=history,system_instruction=(f'''you are an experinced travel planner who alwys gives answer in 
                bullet points and always gives answer in max ten lines.
                example
                user-plan me a two days {query} trip
                assistance-hey  boy travelling to {query} is so much fun in firstt day we will
                explore together 
                plan a trip for user and give the output always in bullet points but each point of 3 to 5 lines with proper day schedule
                and the user is asking for the trip for place {query} for time duration of {days} days
                '''),
                generation_config={"temprature":0.7,
                                           "top_k":20,
                                           "max_output_tokens":1000}
    )
    # for i in range(5,1,-1):
    #     print(".",end="",flush=True)
    #     sleep(0.3)
    with open("chat.txt","r") as f:
            data=f.read()
    
    st.subheader( interaction.output_text)
    history=history+"assistant :"+interaction.output_text

    query=st.text-input("where you want to go  :  ")

    history=history+ "user :"+query

    with open("chat.txt","a") as f:
            f.write(history)

    if len(query)==0:
            break
