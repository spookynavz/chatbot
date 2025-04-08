from factory.character_factory import CharacterFactory

def main():
    factory = CharacterFactory()

    # Example usage
    role = input("Enter role (engineer/doctor): ").strip().lower()
    question = input("Ask a question: ")

    try:
        character = factory.get_character(role)
        response = character.respond(question=question)
        print("\nResponse:\n", response)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
