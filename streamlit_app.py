import streamlit as st
import requests

# Title of the app
st.title('Anime Image Generator')

# Text input for Turkish text
user_input = st.text_input('Enter some Turkish text:')

if st.button('Generate Image'):
    if user_input:
        # Placeholder URL for the anime image generation API
        url = 'http://your-anime-image-api.com/generate'
        response = requests.post(url, json={'text': user_input})
        if response.status_code == 200:
            image_url = response.json().get('image_url')
            st.image(image_url, caption='Generated Anime Image')
        else:
            st.error('Error generating image. Please try again.')
    else:
        st.warning('Please enter some text before generating an image.')