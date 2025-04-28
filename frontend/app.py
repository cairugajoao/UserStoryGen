import streamlit as st
import requests

st.title("UserStoryGen")
description = st.text_input("Describe task:")

if st.button("Generate User Story"):
    if description.strip() != "":
        response = requests.post(
            "http://localhost:8000/generate_user_story",
            json={"text": description}
        )
        if response.status_code == 200:
            story = response.json()["user_story"]
            st.success("Generated Story:")
            st.write(story)
        else:
            st.error("Error: Generating User Story.")

