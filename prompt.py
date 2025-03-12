def get_system_message():
    """Returns the system message for the AI assistant."""
    return "Tu es un correcteur de grammaire en français. Ton rôle est d'améliorer mes phrases pour qu'elles soient claires et naturelles. Si ce que je dis n'est pas compréhensible, reformule-le de manière plus précise."

def generate_prompt(user_text: str):
    """Formats the user input into a structured prompt."""
    return f"Corrige cette phrase : {user_text}"