import streamlit as st
import uuid
from factory.character_factory import CharacterFactory
from services.chat_services import process_chat
from services.database import ChatDB

st.set_page_config(page_title="Chatbot")
st.title("Multi-Character Chatbot")

#factory = CharacterFactory()
db = ChatDB()
session_id = st.session_state.get("session_id", str(uuid.uuid4()))
st.session_state["session_id"] = session_id

# Sidebar for role selection
role = st.selectbox("Select Role", options=["Engineer", "Doctor"])
question = st.text_input("Ask your question:")

# Load history and prepare context
history = db.get_last_messages(session_id)
context = "\n".join([f"{m['role']}: {m['message']}" for m in history])


if st.button("Get Response"):
    if role and question:
        try:
            #character = factory.get_character(role.lower())
            response = process_chat(session_id, role.lower(), question, context)

            st.markdown("Response")
            st.success(response)

            with st.expander("Chat History"):
                for msg in history:
                    st.write(f"**{msg['role'].capitalize()}**: {msg['message']}")

        except Exception as e:
            st.error(str(e))
    else:
        st.warning("Please select a role and enter a question.")
