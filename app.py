import streamlit as st
from gtts import gTTS
import os

# Interfaz de usuario con Streamlit
st.title("🎙️ Generador de Audio con gTTS (Google Text-to-Speech)")

# Entrada de texto
text = st.text_area("Ingrese el texto para convertir en audio:", height=200)

# Selección de idioma
languages = {"Español": "es", "Inglés": "en", "Francés": "fr"}
language = st.selectbox("Seleccione el idioma:", list(languages.keys()))

if st.button("🎧 Generar Audio"):
    if not text.strip():
        st.error("⚠️ Por favor ingrese un texto válido.")
    else:
        try:
            # Generar audio con gTTS
            tts = gTTS(text=text, lang=languages[language], slow=False)
            audio_path = "audio.mp3"
            tts.save(audio_path)

            st.success("✅ Audio generado con éxito!")

            # Mostrar reproductor de audio
            with open(audio_path, "rb") as audio_file:
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format="audio/mp3")

        except Exception as e:
            st.error(f"❌ Error al generar el audio: {str(e)}")
