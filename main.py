import streamlit as st
from factory.character_factory import CharacterFactory

factory = CharacterFactory()

st.title("Chatbot")
st.write("Choose a role and ask a question to receive a role-specific response.")

role = st.selectbox("Select Role", options=["Engineer", "Doctor"])

question = st.text_input("Ask your question:")

if st.button("Get Response"):
    if role and question:
        try:
            character = factory.get_character(role.lower())
            response = character.respond(question=question)
            st.markdown("Response")
            st.success(response)
        except ValueError as e:
            st.error(str(e))
    else:
        st.warning("Please select a role and enter a question.")
