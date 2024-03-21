# 004_AI_Children_Storybook_Generator

import os
from openai import OpenAI
from IPython.display import Image

import streamlit as st
from StoryMethods import StoryMethods as sm


client = OpenAI(
    api_key=st.secrets("OPENAI_API_KEY")
)

def main():
    story_methods = sm()

    # Streamlit layouts
    st.title = "Children story generator"

    user_prompt = st.text_area("Enter a prompt for the story:")

    # Generate the story
    if st.button("Generate story"):
        generated_story = story_methods.story_ai(client, user_prompt)
        st.write('Generated story')
        st.write(generated_story)

        st.divider()

        # Generate a detailed prompt to generate a cover from the story
        design_prompt = story_methods.design_ai(client, generated_story)

        # Generate an image based on the detailed design prompt
        image_url = story_methods.cover_ai(client, design_prompt)
        st.image(image_url, caption='Generated cover image', use_column_width=True)


if __name__ == "__main__":
    main()