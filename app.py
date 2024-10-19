import streamlit as st
import joblib
import pandas as pd
import base64

# Load your models
pipe = joblib.load("myModel.pkl")
svc = joblib.load("mySVCModel.pkl")

# Set up Streamlit page configuration
st.set_page_config(page_title="Spam Detection App", layout="wide")

# Custom CSS for background image
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Path to your local image
image_path = "assets/background.jpg"  # Replace with your actual image path

# Get the base64 encoded image
background_image = get_base64_image(r"C:\Users\akshi\OneDrive\Desktop\SPAMdetection\Only Web Interface\Images\bg.jpg")

# Custom CSS for background image
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url('data:image/jpg;base64,{background_image}');
        background-size: cover;
        background-position: center;
    }}
    .title {{
        color: #ffffff;
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-size: 50px;
    }}
    .subheader {{
        color: #dddddd;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Add page title and description with custom styling
st.markdown("<h1 class='title'>SpamShield</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='subheader'>Check if your text is spam or not</h3>", unsafe_allow_html=True)

# Text input area
input_text = st.text_area("Enter your text here:")

# Layout for the methods
col1, col2 = st.columns(2)

with col1:
    method1 = st.checkbox("Method 1")
with col2:
    method2 = st.checkbox("Method 2")

# Button to check for spam
if st.button("Check"):
    if input_text:
        if method1:
            # Prediction using Model 1
            result1 = pipe.predict([input_text])[0]
            st.write(f"Method 1 Result: {result1}")
        
        if method2:
            # Prediction using Model 2
            result2 = svc.predict([input_text])[0]
            st.write(f"Method 2 Result: {result2}")
        
        if not method1 and not method2:
            st.warning("Please select at least one method.")
    else:
        st.warning("Please enter some text to check.")

# Footer section
st.markdown("---")
st.text("© 2024 Developed by Akshit")
