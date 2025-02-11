import openai
import streamlit as st

# Set up OpenAI API key from Streamlit Secrets (NOT .env)
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Streamlit app title
st.title("REVO Custom Jersey Generator")

# User inputs for customization
jersey_type = st.selectbox("What type of jersey do you want to create?", ["Baseball", "Basketball", "Cheerleading", "Cycling", "American Football", "Hockey", "Lacrosse", "Rugby", "Soccer", "Softball", "Track & Field", "Volleyball", "Wrestling"])
primary_color = st.selectbox("Primary Color", ["Blue", "Red", "Green", "Yellow", "Black", "White", "Gray", "Navy", "Gold", "Orange", "Purple", "Maroon", "Teal", "Silver"])
secondary_color = st.selectbox("Secondary Color", ["Blue", "Red", "Green", "Yellow", "Black", "White", "Gray", "Navy", "Gold", "Orange", "Purple", "Maroon", "Teal", "Silver"])
third_color = st.selectbox("Third Color", ["Blue", "Red", "Green", "Yellow", "Black", "White", "Gray", "Navy", "Gold", "Orange", "Purple", "Maroon", "Teal", "Silver"])

design_elements = st.text_input("Do you have any specific design elements in mind?", "Stripes")
team_name = st.text_input("Anything else you'd like to include? (e.g., team name)", "Wildcats")

# Generate the prompt dynamically
prompt = (
	f"A collection of four professional {jersey_type} jerseys showing Front and Back, displayed in a side-by-side grid. "
    f"Each jersey features {primary_color}, {secondary_color}, and {third_color}  colors. The design includes {design_elements}. "
    f"The jersey should have a sleek and modern look, suitable for a professional team. "
    f"Include the team name '{team_name}' as part of the design. "
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
                # Call OpenAI DALL·E 3 API
                response = openai.images.generate(
                    model="dall-e-3",
                    prompt=prompt,
                    n=1,
                    size="1024x1024",
                    quality="hd"
                )

                # ✅ Correct way to extract image URL
                image_url = response.data[0].url

                # Display the generated image
                st.image(image_url, caption="Generated Jersey Design", use_container_width=True)

            except Exception as e:
                st.error(f"Error generating image: {e}")
    else:
        st.warning("Please provide the necessary details to generate an image.")

# Footer
st.write("Powered by OpenAI's DALL·E 3 model.")


st.markdown("### Disclaimer")
st.markdown("""
This jersey designer is an AI-powered tool intended for **conceptual and quick reference purposes only**. 
The generated designs are **computer-generated renderings** and may not always reflect precise colors, patterns, or branding constraints. 
This service does not provide **actual product manufacturing, printing, or licensing** of any designs.

All images are generated using **OpenAI's DALL·E model**, and while efforts are made to ensure unique designs, 
the system does not recognize trademarks, logos, or copyrights. Users should verify all designs before use in **commercial or official applications**.

By using this app, you acknowledge that the generated designs are for **inspirational and illustrative purposes only**, 
and we do not assume responsibility for any legal or production-related implications.

🔹 **For professional design services or production inquiries, consult a licensed designer or manufacturer.**
""")

