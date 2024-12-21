import google.generativeai as genai
from PIL import Image
import os
import numpy as np
import re
GOOGLE_API_KEY='AIzaSyDVzaWeKuZEyL4_tqZB-wvFeGLsH5XBu6ckk'
if not GOOGLE_API_KEY:
   raise Exception("Set the GOOGLE_API_KEY environment variable")

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

def predict(image_path):
    prompt = "What is this an image of? give me a description of the image in just 50 words directly without any heading"

    try:
        image = Image.open(image_path)
    except Exception as e:
        return f"Error opening image: {image_path}, {e}"

    try:
        response = model.generate_content([prompt, image])
    except Exception as e:
        return f"Error with the Gemini model, skipping image {image_path}, {e}"

    try:
        prediction = response.text.strip()
        return f"Predicted Class: {prediction}"
    except AttributeError:
       return f"Error: Response doesn't contain any text from {image_path}"
