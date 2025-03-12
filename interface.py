import streamlit as st
import requests

# Titre de l'application
st.title("📝 Correcteur de grammaire français")

# Champ de texte pour l'utilisateur
user_input = st.text_area("✍️ Entrez une phrase à corriger :")

# Sélecteur de style
style_options = {
    "Correction standard (neutre)": "standard",
    "Formel (ton professionnel)": "formel",
    "Courant (ton naturel et fluide)": "courant",
    "Familier (ton détendu et spontané)": "familier",
}
style_choice = st.selectbox("🎭 Choisissez un style de correction :", list(style_options.keys()))

if st.button("✅ Corriger"):
    if user_input:
        # Envoi de la requête à l'API FastAPI avec le texte et le style sélectionné
        response = requests.post(
            "http://127.0.0.1:8000/correct",
            json={"text": user_input, "style": style_options[style_choice]}
        )

        if response.status_code == 200:
            data = response.json()
            corrected_text = data.get("corrected_text", "❌ Erreur lors de la correction.")

            # Affichage du résultat
            st.subheader("✏️ Texte corrigé :")
            st.success(corrected_text)
        else:
            st.error("🚨 Une erreur s'est produite lors de la correction.")
    else:
        st.warning("⚠️ Veuillez entrer une phrase à corriger.")
