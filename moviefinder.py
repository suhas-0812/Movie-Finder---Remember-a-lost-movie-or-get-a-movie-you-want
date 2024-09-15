import openai
import json
import streamlit as st

# Set your API key
openai.api_key = st.secrets["openai"]["API_KEY"]

def get_movie_using_user_prompt(user_prompt):

    # OpenAI API call
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are a dynamic movie recommendation assistant. Your task is to provide movie recommendations based on the user's prompt. It is really important to ensure that the recommendations are relevant to details provided in the prompt, such as actor names, movie names, genres, or specific themes. Output should be in strict JSON format with a 'movies' key containing an array of three movie objects. Each object should include 'movie_name', 'year_of_release', 'cast', 'description', 'director' and 'original_language'. Keep the description short. Ensure the most relevant movie is first."
            },
            {
                "role": "user",
                "content": user_prompt
            },
        ],
        temperature=1.2,
        max_tokens=400,
        top_p=0.9,
        frequency_penalty=0,
        presence_penalty=0.5,
        response_format={"type": "json_object"}
    )
    print(response['choices'][0]['message']['content'].strip())
    return json.loads(response['choices'][0]['message']['content'].strip())

