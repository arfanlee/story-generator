# 004_AI_Children_Storybook_Generator

from openai import OpenAI

import streamlit as st
from StoryMethods import StoryMethods as sm

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

def main():
    story_methods = sm()

    # Streamlit layouts
    st.title("Story and cover generator")

    user_prompt = st.text_area("Enter a prompt for the story:")

    # Generate the story
    if st.button("Generate story"):
        generated_story = story_methods.story_ai(client, user_prompt)
        title = story_methods.title_ai(client, generated_story)
        st.header(title)

        # Generate a detailed prompt to generate a cover from the story
        design_prompt = story_methods.design_ai(client, generated_story)

        # Generate an image based on the detailed design prompt
        image_url = story_methods.cover_ai(client, design_prompt)
        st.image(image_url, caption='Generated cover image', use_column_width=True)

        st.divider()

        st.write_stream(generated_story)

if __name__ == "__main__":
    main()