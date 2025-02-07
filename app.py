

import openai
import streamlit as st

import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
openai.api_key = os.getenv("OPENAI_API_KEY") 


# Set up OpenAI API key

# Streamlit app title
st.title("REVO Custom Jersey Generator")

# User inputs for customization
jersey_type = st.selectbox("What type of jersey do you want to create?", ["Soccer", "Basketball", "Baseball", "Hockey"])
colors = st.text_input("What colors do you want to use?", "Blue and White")
design_elements = st.text_input("Do you have any specific design elements in mind?", "Stripes")
team_name = st.text_input("Anything else you'd like to include? (e.g., team name)", "Wildcats")

# Generate the prompt dynamically
prompt = (
    f"A {jersey_type} jersey featuring {colors} colors. The design includes {design_elements}. "
    f"The jersey should have a sleek and modern look, suitable for a professional team. "
    f"Include the team name '{team_name}' as part of the design."
    f"This is a clean, minimalist team jersey designed without commercial branding or corporate symbols. "
    f"The focus is on a unique, independent team identity without recognizable trademarks or logos."

)

# Display the generated prompt
st.write("### Generated AI Prompt:")
st.write(prompt)

# Button to generate the image
if st.button("Generate Jersey Design"):
    if prompt.strip():
        with st.spinner("Generating jersey design..."):
            try:
                # Call OpenAI DALL·E 3 API with the dynamically created prompt
                response = openai.Image.create(
                    prompt=prompt,
                    model="dall-e-3",  # Specify the DALL·E 3 model
                    n=1,  # Number of images to generate
                    size="1024x1024",  # Image resolution
                    quality="hd"  # High-quality setting
                )

                # Extract the image URL
                image_url = response['data'][0]['url']

                # Display the generated image
                st.image(image_url, caption="Generated Jersey Design", use_container_width=True)

            except Exception as e:
                st.error(f"Error generating image: {e}")
    else:
        st.warning("Please provide the necessary details to generate an image.")

# Footer
st.write("Powered by OpenAI's DALL·E 3 model.")



