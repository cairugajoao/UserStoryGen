import streamlit as st
import requests

st.title("UserStoryGen")
descricao = st.text_input("Describe task:")

if st.button("Generate User Story"):
    if descricao.strip() != "":
        response = requests.post(
            "http://localhost:8000/gerar_user_story",
            json={"texto": descricao}
        )
        if response.status_code == 200:
            story = response.json()["user_story"]
            st.success("Generated Story:")
            st.write(story)
        else:
            st.error("Error: Generating User Story.")

