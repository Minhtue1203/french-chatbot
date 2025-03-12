import streamlit as st
import requests

# Titre de l'application
st.title("📝 Correcteur de grammaire français")

# Champ de texte pour l'utilisateur
user_input = st.text_area("Entrez une phrase à corriger :")

if st.button("Corriger"):
    if user_input:
        response = requests.post(
            "http://127.0.0.1:8000/correct",
            json={"text": user_input}
        )
        corrected_text = response.json()["corrected_text"]
        st.write("✅ **Texte corrigé :**")
        st.success(corrected_text)
    else:
        st.warning("Veuillez entrer une phrase.")
