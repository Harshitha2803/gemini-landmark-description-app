import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# Configure Gemini API
GOOGLE_API_KEY = 'AIzaSyBPnEnVH0sCH8r_CJw8xzfTbOX-N2Ts_r4'  # Access API key from Streamlit secrets
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro-vision')


def summarize_image_gemini(image_data):
    """
    Analyzes an image using Gemini Pro Vision and generates a 5-line summary
    of the landmarks, historical, and cultural context.
    Args:
        image_data: BytesIO object containing the image data.
    Returns:
        str: A 5-line summary of the image.
    """
    try:
        img = Image.open(image_data)

        response = model.generate_content([
            "You are an AI that summarizes images in 5 concise lines, describing the landmarks, historical, and cultural context.",
            img
        ])

        return response.text

    except Exception as e:
        return f"Error: Unable to process the image. {e}"



# Streamlit App
st.title("Landmark Image Summarizer")

uploaded_image = st.file_uploader("Upload an image of a landmark", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    st.image(uploaded_image, caption="Uploaded Image.", use_column_width=True)
    st.write("Analyzing...")

    try:
        # Get the summary from Gemini
        summary = summarize_image_gemini(uploaded_image)

        st.write("### Summary:")
        st.write(summary)

    except Exception as e:
        st.error(f"An error occurred: {e}")