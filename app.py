from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import io

# Configure the API key for Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to interact with Gemini Pro Vision API
def get_gemini_responses(input_text, image, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    # Pass the PIL image and other inputs to the API
    response = model.generate_content([input_text, image, prompt])
    return response.text

# Set Streamlit page configuration
st.set_page_config(page_title="GeminiDecode: MultiLanguage Document Extraction by Gemini Pro")

# File uploader for image
uploaded_file = st.file_uploader("Choose an image file:", type=["jpeg", "png", "jpg"])
image = None

# Display the uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

# Button to submit and process the image
submit = st.button("Tell me about the Document")

# Input prompt for the model
input_prompt = """You are an expert in understanding invoices.
We will upload an image as an invoice, and you will have to answer any questions based on the uploaded invoice image.
"""

# Header and description for the app
st.header("GeminiDecode: MultiLanguage Document Extraction by Gemini Pro")
text = (
    "Utilizing Gemini Pro AI, this project effortlessly extracts vital information "
    "from diverse multilingual documents, transcending language barriers with precision "
    "and efficiency for enhanced productivity and decision-making."
)
styled_text = f"<span style='font-family:serif;'>{text}</span>"
st.markdown(styled_text, unsafe_allow_html=True)

# Process the image and display the AI response
if submit:
    if image is not None:
        try:
            # Get the response from the Gemini API
            response = get_gemini_responses(input_prompt, image, input_prompt)
            st.subheader("The response is:")
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please upload an image file before submitting.")
