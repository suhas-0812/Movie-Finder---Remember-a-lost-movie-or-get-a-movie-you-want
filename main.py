import streamlit as st
from moviefinder import get_movie_using_user_prompt

# Set up page configuration to use a wide layout
st.set_page_config(page_title="Movie Recommendation Bot", layout="wide")

# Main title
st.title("🎬 Discover Your Perfect Movie Match Instantly! 🎥")

# Subheader
st.subheader("Things you can do with this bot:")

col1, col2, col3 =st.columns(3)

with col1:
    st.markdown("""
        **🔍 Remember a Forgotten Movie:**  
        *This bot helps you find a movie whose plot is stuck in your head, but you can't recall the name. Just type whatever you remember, and let the magic happen!*
    """
    )

with col2:
    st.markdown("""
        **❤️ Liked a Movie? Find a Similar Movie:**  
        *Tell us about a movie you loved, and we'll suggest similar films that match your taste!*          
    """
    )

with col3:
    st.markdown("""
        **🎭 Describe Your Thoughts, Find the Movie:**
        *Share what's in your head, and we'll suggest a movie that matches it.*   
    """
    )

# Text input bar for user input
user_input = st.text_input("", key="user_input", placeholder="Type your message here...", label_visibility="collapsed")
placeholder = st.empty()
if st.button("Recommend"):
    if not user_input.strip():
        placeholder.error("This field is required. Please type your message.")
    else:
        recommended_movies=get_movie_using_user_prompt(user_input)        
        st.markdown("### Movies that matched your requirement")
        for movie in recommended_movies['movies']:
            st.subheader(movie['movie_name'])
            st.write("Release Year: "+str(movie['year_of_release']))
            st.write("Language: "+movie['original_language'])
            cast=""
            for actor in movie['cast']:
                if cast=="":
                    cast+=actor
                else:
                    cast+=", "+actor
            st.write("Cast: "+cast)
            st.write("Director: "+movie['director'])
            st.write("Description: "+movie['description'])
            st.write()
            