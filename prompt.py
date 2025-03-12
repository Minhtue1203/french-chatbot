def get_system_message():
    """Retourne le message système avec une explication simple des styles disponibles."""
    return """Tu es un correcteur de grammaire en français. 
    Ton rôle est d'améliorer les phrases pour qu'elles soient claires et naturelles. 
    Si une phrase est difficile à comprendre, reformule-la de manière plus précise. 

    L'utilisateur peut choisir un style de correction :
    - 'formel' : Ton professionnel et poli. Le texte doit être clair, précis et bien structuré.
    - 'courant' : Ton naturel et fluide, adapté aux discussions de tous les jours.
    - 'familier' : Ton détendu et spontané, proche du langage parlé entre amis.

    Si aucun style n'est précisé, utilise un ton neutre et clair.
    """

def generate_prompt(user_text: str, style: str):
    """Génère un prompt clair en fonction du style choisi."""
    style_instructions = {
        "formel": "Corrige la phrase avec un ton formel. Utilise un langage professionnel, clair et bien structuré.",
        "courant": "Corrige la phrase avec un ton courant. Le texte doit être naturel, fluide et facile à lire.",
        "familier": "Corrige la phrase avec un ton familier. Utilise un langage détendu et spontané, comme dans une conversation entre amis.",
        "standard": "Corrige la phrase en gardant un ton neutre et clair."
    }

    instruction = style_instructions.get(style.lower(), style_instructions["standard"])
    return f"{instruction}\nPhrase : {user_text}"
