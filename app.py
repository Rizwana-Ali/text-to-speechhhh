


# import streamlit as st
# from gtts import gTTS
# import os
# from io import BytesIO

# # Title of the app
# st.title("Text-to-Speech App with Multiple Male Voices")

# # Description
# st.write("""
# This app converts your text into speech using more than 10 male voices. 
# Enter your text below, select a voice, and click the 'Generate Speech' button.
# You can also download the generated audio file.
# """)

# # Text input
# text = st.text_area("Enter your text here:", height=150)

# # List of male voices (language and accent combinations)
# voices = {
#     "English (US) - Male 1": "en-us",
#     "English (US) - Male 2": "en-us",
#     "English (UK) - Male 1": "en-gb",
#     "English (UK) - Male 2": "en-gb",
#     "Australian English - Male": "en-au",
#     "Indian English - Male": "en-in",
#     "Canadian English - Male": "en-ca",
#     "South African English - Male": "en-za",
#     "Irish English - Male": "en-ie",
#     "Scottish English - Male": "en-sc",
#     "French - Male": "fr-fr",
#     "German - Male": "de-de",
#     "Spanish - Male": "es-es",
#     "Italian - Male": "it-it",
#     "Portuguese - Male": "pt-pt",
# }

# # Dropdown to select voice
# selected_voice = st.selectbox("Select a voice:", list(voices.keys()))

# # Button to generate speech
# if st.button("Generate Speech"):
#     if text.strip() == "":
#         st.warning("Please enter some text to generate speech.")
#     else:
#         with st.spinner("Generating speech..."):
#             # Get the language code for the selected voice
#             lang_code = voices[selected_voice]
            
#             # Create a gTTS object
#             tts = gTTS(text=text, lang=lang_code, slow=False)
            
#             # Save the audio file to a BytesIO object
#             audio_bytes = BytesIO()
#             tts.write_to_fp(audio_bytes)
#             audio_bytes.seek(0)
            
#             # Play the audio file
#             st.audio(audio_bytes, format="audio/mp3")
            
#             # Add a download button
#             st.download_button(
#                 label="Download Audio",
#                 data=audio_bytes,
#                 file_name="output.mp3",
#                 mime="audio/mp3"
#             )

# # Footer
# st.markdown("---")
# st.write("Made with ❤️ using Streamlit and gTTS")























import streamlit as st
from gtts import gTTS
import os
from io import BytesIO

# Title of the app
st.title("Text-to-Speech App with Male Voices")

# Description
st.write("""
This app converts your text into speech using male voices. 
Enter your text below, select a voice, and click the 'Generate Speech' button.
You can also download the generated audio file.
""")

# Text input
text = st.text_area("Enter your text here:", height=150)

# List of male voices (language and accent combinations)
voices = {
    "English (US) - Male": "en-us",  # Often male
    "English (UK) - Male": "en-gb",  # Often male
    "Australian English - Male": "en-au",  # Often male
    "Indian English - Male": "en-in",  # Often male
    "Canadian English - Male": "en-ca",  # Often male
    "South African English - Male": "en-za",  # Often male
    "French - Male": "fr-fr",  # Often male
    "German - Male": "de-de",  # Often male
    "Spanish - Male": "es-es",  # Often male
    "Italian - Male": "it-it",  # Often male
    "Portuguese - Male": "pt-pt",  # Often male
}

# Dropdown to select voice
selected_voice = st.selectbox("Select a voice:", list(voices.keys()))

# Button to generate speech
if st.button("Generate Speech"):
    if text.strip() == "":
        st.warning("Please enter some text to generate speech.")
    else:
        with st.spinner("Generating speech..."):
            # Get the language code for the selected voice
            lang_code = voices[selected_voice]
            
            # Create a gTTS object
            tts = gTTS(text=text, lang=lang_code, slow=False)
            
            # Save the audio file to a BytesIO object
            audio_bytes = BytesIO()
            tts.write_to_fp(audio_bytes)
            audio_bytes.seek(0)
            
            # Play the audio file
            st.audio(audio_bytes, format="audio/mp3")
            
            # Add a download button
            st.download_button(
                label="Download Audio",
                data=audio_bytes,
                file_name="output.mp3",
                mime="audio/mp3"
            )

# Footer
st.markdown("---")
st.write("Made with ❤️ using Streamlit and gTTS")