from openai import OpenAI

import streamlit as st
from main_methods import StoryMethods as sm

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

def main():
    # Streamlit layouts
    st.title("Story and cover generator")

    user_prompt = st.text_area("Enter a prompt for the story:")

    # Generate the story
    if st.button("Generate story"):
        generated_story = sm.story_ai(client, user_prompt)
        title = sm.title_ai(client, generated_story)
        st.header(title)

        # Generate a detailed prompt to generate a cover from the story
        design_prompt = sm.design_ai(client, generated_story)

        # Generate an image based on the detailed design prompt
        image_url = sm.cover_ai(client, design_prompt)
        st.image(image_url, caption='Generated cover image', use_column_width=True)

        st.divider()

        st.write(generated_story)

if __name__ == "__main__":
    main()
