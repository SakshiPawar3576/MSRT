import streamlit as st
import whisper
import torchaudio
from deep_translator import GoogleTranslator
from gtts import gTTS
import os
from io import BytesIO
from pydub import AudioSegment
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
import streamlit as st
from database import *

st.set_page_config(
    page_title="Multilingual Speech Recognition",
    page_icon="🎙️",
    layout="wide"
)

st.markdown("""
    <style>
        .main {
            background-color: #f4f9ff;
        }

        .block-container {
            padding-top: 2rem;
        }

        .stFileUploader, .stSelectbox {
            background-color: #e6f2ff;
            padding: 15px;
            border-radius: 15px;
            border: 1px solid #cce6ff;
        }

        .result-box {
            background-color: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
            margin-top: 20px;
        }

        h1, h2, h3 {
            color: #003366;
        }
    </style>
""", unsafe_allow_html=True)



st.markdown("""
<style>

/* ===== App Background ===== */
.stApp {
    background-color: #cee4ed;
}

/* ===== Remove Top Header ===== */
header[data-testid="stHeader"] {
    background: transparent !important;
    box-shadow: none !important;
}

div[data-testid="stToolbar"] {
    background: transparent !important;
}

/* ===== FORCE ALL TEXT BLACK ===== */
body, p, span, label, div, h1, h2, h3, h4, h5, h6 {
    color: #000000 !important;
}

/* ===== Sidebar Transparent ===== */
section[data-testid="stSidebar"] {
    background-color: rgba(255,255,255,0.6) !important;
    backdrop-filter: blur(10px);
    border-right: 1px solid #e6f2f8;
}

section[data-testid="stSidebar"] * {
    color: #000000 !important;
}

/* ===== TEXTBOX (REAL FIX) ===== */

/* ===== TEXTBOX – EXACT MATCH TO DROPDOWN ===== */

/* Outer wrapper */
div[data-baseweb="input"] {
    background-color: #ffffff !important;
    border-radius: 12px !important;
}

/* Inner visible box */
div[data-baseweb="input"] > div {
    background-color: #ffffff !important;
    border: 1px solid #d6eaf8 !important;
    border-radius: 12px !important;
    box-shadow: none !important;
}

/* Remove dark theme border layers */
div[data-baseweb="input"] * {
    border-color: #d6eaf8 !important;
}

/* Actual input text */
div[data-baseweb="input"] input {
    background: transparent !important;
    color: #000000 !important;
}

/* Focus state */
div[data-baseweb="input"]:focus-within > div {
    border: 1px solid #d6eaf8 !important;
    box-shadow: none !important;
}
/* ===== SELECTBOX FIX ===== */

/* Dropdown main area */
div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
    color: #000000 !important;
    border-radius: 12px !important;
    border: 1px solid #d6eaf8 !important;
}

/* Dropdown menu options */
ul {
    background-color: #ffffff !important;
    color: #000000 !important;
}

/* ===== BUTTON ===== */
.stButton>button {
    background-color: #66b3ff;
    color: white !important;
    border-radius: 14px;
    height: 48px;
    border: none;
}

.stButton>button:hover {
    background-color: #4da6ff;
}
/* FORM SUBMIT BUTTON FIX */
div[data-testid="stForm"] button {
    background-color: #66b3ff !important;
    color: white !important;
    border-radius: 14px !important;
    height: 48px !important;
    border: none !important;
}

div[data-testid="stForm"] button:hover {
    background-color: #4da6ff !important;
}
/* ===== FILE UPLOADER BLUE STYLE ===== */

div[data-testid="stFileUploader"] {
    background-color: #e6f2ff !important;
    border: 2px dashed #66b3ff !important;
    border-radius: 16px !important;
    padding: 25px !important;
}

/* Drag area inside */
div[data-testid="stFileUploader"] section {
    background-color: #f0f8ff !important;
    border-radius: 12px !important;
}

/* Remove dark drag overlay */
div[data-testid="stFileUploader"] * {
    color: #000000 !important;
}
/* ===== FILE UPLOADER BUTTON ===== */

div[data-testid="stFileUploader"] button {
    background-color: #ffffff !important;
    color: #3399ff !important;
    border: 1px solid #66b3ff !important;
    border-radius: 12px !important;
    font-weight: 500 !important;
}

/* Hover effect */
div[data-testid="stFileUploader"] button:hover {
    background-color: #f0f8ff !important;
    color: #1a8cff !important;
}
img {
    opacity: 0.8;
    filter: blur(1px);
}
.login-box {
    background-color: rgba(255, 255, 255, 0.7);
    padding: 30px;
    border-radius: 15px;
}                       


</style>
""", unsafe_allow_html=True)




create_table()

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

menu = ["Login", "Signup", "Forgot Password"]
choice = st.sidebar.selectbox("Menu", menu)

if not st.session_state.authenticated:

    if choice == "Login":

        left_col, right_col = st.columns([1, 1.2])

        with left_col:
            st.markdown("""
                <div style="
                    background: white;
                    padding: 40px;
                    border-radius: 20px;
                    box-shadow: 0 8px 20px rgba(0,0,0,0.05);
                ">
            """, unsafe_allow_html=True)

            st.markdown("## Login")
            st.caption("Welcome back! Please login to continue.")

            with st.form("login_form"):
                username = st.text_input("Username")
                password = st.text_input("Password", type="password")
                submit = st.form_submit_button("Login", use_container_width=True)

                if submit:
                    user = login_user(username, password)
                    if user:
                            st.session_state["authenticated"] = True
                            st.rerun()
                    else:
                            st.error("Invalid credentials")

                st.markdown("</div>", unsafe_allow_html=True)

            with right_col:
                st.image("icon.png", width="stretch")



    elif choice == "Signup":

        center_col = st.columns([1,2,1])[1]

        with center_col:
            st.markdown("## Create Account")

            new_user = st.text_input("Username")
            email = st.text_input("Email")
            new_pass = st.text_input("Password", type="password")

            if st.button("Signup", use_container_width=True):
                if create_user(new_user, email, new_pass):
                    st.success("Account created successfully")
                else:
                    st.error("Username already exists")
            

    elif choice == "Forgot Password":

        center_col = st.columns([1,2,1])[1]

        with center_col:
            st.markdown("## Reset Password")

            username = st.text_input("Username")
            new_password = st.text_input("New Password", type="password")

            if st.button("Reset", use_container_width=True):
                reset_password(username, new_password)
                st.success("Password updated successfully")
            
    st.stop()



if st.sidebar.button("Logout"):
    st.session_state["authenticated"] = False
    st.rerun()



    



@st.cache_resource
def load_model():
    try:
        return whisper.load_model("base")  
    except Exception as e:
        st.error(f"Error loading Whisper model: {str(e)}")
        return None

model = load_model()


LANGUAGES = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Chinese (Simplified)": "zh-CN",
    "Arabic": "ar",
    "Russian": "ru",
    "Japanese": "ja",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "Nepali": "ne",
    "Bengali": "bn",
    "Tamil": "ta" 
}

st.markdown("<h1 style='text-align:center;'>️ Multilingual Speech Recognition and Transliteration</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Upload audio → Transcribe → Translate → Listen</p>", unsafe_allow_html=True)



uploaded_file = st.file_uploader("Upload Audio", type=["mp3","wav","m4a"])
target_language = st.selectbox("Select Language", list(LANGUAGES.keys()))



if uploaded_file is not None and model is not None:

    with st.spinner("Processing..."):
        try:
            import tempfile
            if "." in uploaded_file.name:
                suffix = "." + uploaded_file.name.split(".")[-1]  # VERY IMPORTANT
            else:
                suffix = ".wav"

            with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
                tmp.write(uploaded_file.read())
                temp_audio_path = tmp.name

            result = model.transcribe(temp_audio_path)
            original_text = result.get("text", "").strip()

            if original_text == "":
                st.error("No speech detected in the audio.")
            else:
                lang_code = LANGUAGES[target_language]

                def translate_large_text(text, target_lang):
                    max_chunk = 4000  # safe limit under 5000
                    chunks = [text[i:i+max_chunk] for i in range(0, len(text), max_chunk)]
    
                    translated_chunks = []
    
                    for chunk in chunks:
                        translated = GoogleTranslator(
                            source="auto",
                            target=target_lang
                        ).translate(chunk)
                        translated_chunks.append(translated)
    
                    return " ".join(translated_chunks)

                translated_text = ""
                translated_text = translate_large_text(original_text, target_lang=lang_code)


                hinglish_text = ""
                if target_language == "Hindi":
                    hinglish_text = transliterate(
                        translated_text,
                        sanscript.DEVANAGARI,
                        sanscript.ITRANS
                    )
                    hinglish_text = hinglish_text.lower().capitalize()

                # Text-to-speech
                tts_path = None
                try:
                    tts = gTTS(translated_text, lang=lang_code)
                    tts_path = "output.mp3"
                    tts.save(tts_path)
                except Exception:
                    st.warning(f"TTS not available for {target_language}")
                    
                st.subheader("Transcribed Text")
                st.write(original_text)

                st.subheader(f"Translated Text ({target_language})")
                st.write(translated_text)

                if target_language == "Hindi":
                    st.subheader("Hinglish Transliteration")
                    st.write(hinglish_text)
                
                if tts_path is not None:
                    st.subheader("Translated Speech")
                    st.audio(tts_path, format="audio/mp3")

            os.remove(temp_audio_path)
            if os.path.exists("output.mp3"):
                os.remove("output.mp3")

        except Exception as e:
            st.error(f"Error processing audio: {e}") 
