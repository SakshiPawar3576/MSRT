# 🎙️ Multilingual Speech Recognition and Transliteration (MSRT)

A Streamlit-based web application that converts speech into text, translates it into multiple languages, and generates spoken audio output. The system also supports Hindi transliteration into Hinglish for improved readability.

---

## 🚀 Features

* 🎧 Upload audio files in **MP3, WAV, or M4A** format
* 🧠 Speech-to-text using **OpenAI Whisper**
* 🌍 Automatic language translation using **Google Translator API**
* 🔊 Text-to-speech generation using **gTTS**
* 🔤 Hindi to Hinglish transliteration
* 🔐 User authentication system (Login, Signup, Forgot Password)
* 💾 SQLite database for storing user credentials
* 🎨 Clean and responsive UI built with Streamlit and custom CSS

---

## 🛠️ Technologies Used

| Category           | Tools & Libraries     |
| ------------------ | --------------------- |
| Frontend           | Streamlit             |
| Speech Recognition | Whisper               |
| Translation        | deep-translator       |
| Text-to-Speech     | gTTS                  |
| Audio Processing   | pydub, torchaudio     |
| Database           | SQLite                |
| Transliteration    | indic-transliteration |
| Language           | Python                |

---

## 📂 Project Structure

```
MSRT/
│
├── main.py              # Streamlit application
├── database.py          # Authentication and database logic
├── users.db             # SQLite database file
├── icon.png             # UI image/logo
├── requirements.txt     # Python dependencies
├── packages.txt         # Additional environment packages
└── .gitignore           # Ignored files and folders
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/SakshiPawar3576/MSRT.git
cd MSRT
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
streamlit run main.py
```

---

## 🧪 Supported Languages

The system currently supports translation into:

* English
* Hindi
* Marathi
* Gujarati
* Bengali
* Tamil
* Spanish
* French
* German
* Arabic
* Russian
* Japanese
* Chinese (Simplified)
* Punjabi
* Nepali

---

## 🔐 Authentication System

The application includes a complete login system:

* User Signup
* Secure Login
* Password Reset
* SQLite-based storage

Passwords are stored securely within a local database file (`users.db`).

---

## 🔄 Application Workflow

1. User logs into the system
2. Uploads an audio file
3. Whisper transcribes speech to text
4. Text is translated to selected language
5. Hindi text is optionally transliterated to Hinglish
6. Translated text is converted into speech
7. Output is displayed and playable in the browser

---

## 🖼️ User Interface

The UI is built with custom CSS for:

* Soft blue theme
* Styled login forms
* Custom file uploader
* Responsive layout

---

## 📦 Requirements

Main dependencies:

```
streamlit
whisper
torch
torchaudio
pydub
deep-translator
gTTS
indic-transliteration
```

---

## ⚠️ Notes

* Whisper models are downloaded automatically on first run.
* Internet connection is required for translation and text-to-speech.
* Large audio files may take longer to process depending on system performance.

---

## 📸 Screenshots

*(Add screenshots here before submission or presentation)*

---

## 👩‍💻 Author

**Sakshi Pawar**
BSc IT Student – Mumbai University

GitHub: [https://github.com/SakshiPawar3576](https://github.com/SakshiPawar3576)

---

## 📜 License

This project is developed for academic and educational purposes.
