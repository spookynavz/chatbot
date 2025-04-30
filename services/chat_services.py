from services.database import ChatDB
from factory.character_factory import CharacterFactory

db = ChatDB()
factory = CharacterFactory()

def process_chat(session_id: str, role: str, question: str, context: str) -> str:
    #Generates a response and stores chat history in MongoDB
    character = factory.get_character(role)
    response = character.respond(question=question, context=context)

    db.save_message(session_id, "user", question)
    db.save_message(session_id, "bot", response)

    return response
