class StoryMethods:

    def story_ai(self, client, prompt):
        story_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a bestseller fantasy story writer. You'll take user's prompt and generate a 100 words short story for young adults."},
            {"role": "user", "content": prompt}
        ],
        max_tokens = 400,
        temperature = 1.3
        )

        story = story_response.choices[0].message.content
        return story

    def title_ai(self, client, story):
        story_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a marketing specialist with the story provided, come up with a attractive title for the story."},
            {"role": "user", "content": story}
        ],
        max_tokens = 100,
        temperature = 1.3
        )

        title = story_response.choices[0].message.content
        return title

    def cover_ai(self, client, image_prompt):
        image_response = client.images.generate(
        model="dall-e-3",
        prompt=image_prompt,
        size="1024x1024",
        quality="standard",
        n=1,
        )

        image_url = image_response.data[0].url
        return image_url
    
    # take the generated story and generate a story
    def design_ai(self, client, story):
        design_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """Based on the story given, you will design a detailed imgae prompt for the cover image of this story. The image prompt
                                            should include theme of the story with relevant colour, the output should be within 100 characters"""},
            {"role": "user", "content": story}
        ],
        max_tokens = 100,
        temperature = 1.3
        )

        design_prompt = design_response.choices[0].message.content
        return design_prompt