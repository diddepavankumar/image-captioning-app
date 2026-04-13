import streamlit as st
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
from gtts import gTTS
from googletrans import Translator
import tempfile
import os

# Load model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

translator = Translator()

st.set_page_config(page_title="Image Captioning Siri+", layout="centered")

st.title("🧠 Image Captioning - Siri+ (Voice Enabled)")
st.write("Upload an image to generate captions in English & Hindi with voice output.")

# ---------------- UI OPTIONS ----------------
language_choice = st.selectbox(
    "🌐 Select Voice Output Language",
    ["English", "Hindi", "Both"]
)

accessibility_mode = st.checkbox("♿ Enable Accessibility Mode")

if accessibility_mode:
    st.markdown(
        "<style>html, body, [class*='css']  {font-size: 20px !important;}</style>",
        unsafe_allow_html=True
    )

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader("📸 Choose an image...", type=["jpg", "jpeg", "png"])

# ---------------- TTS FUNCTION ----------------
def generate_speech(text, lang):
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(temp_file.name)
        return temp_file.name
    except Exception as e:
        st.error(f"TTS Error: {e}")
        return None

# ---------------- MAIN LOGIC ----------------
if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_container_width=True)
    st.write("⏳ Generating caption...")

    try:
        # Generate English caption
        inputs = processor(images=image, return_tensors="pt")  # pyright: ignore[reportCallIssue]
        out = model.generate(**inputs)
        english_caption = processor.decode(out[0], skip_special_tokens=True)

        # Translate to Hindi
        hindi_caption = translator.translate(english_caption, dest="hi").text

        # Display captions
        st.subheader("📝 Captions")
        st.write(f"🇬🇧 English: {english_caption}")
        st.write(f"🇮🇳 Hindi: {hindi_caption}")

        # Generate audio
        english_audio = None
        hindi_audio = None

        if language_choice in ["English", "Both"]:
            english_audio = generate_speech(english_caption, "en")

        if language_choice in ["Hindi", "Both"]:
            hindi_audio = generate_speech(hindi_caption, "hi")

        # ---------------- AUTO PLAY ----------------
        if accessibility_mode:
            if english_audio:
                st.audio(english_audio, autoplay=True)
            if hindi_audio:
                st.audio(hindi_audio, autoplay=True)

        # ---------------- REPLAY BUTTONS ----------------
        st.subheader("🔊 Replay Audio")

        col1, col2 = st.columns(2)

        with col1:
            if english_audio and st.button("▶ Play English"):
                st.audio(english_audio)

        with col2:
            if hindi_audio and st.button("▶ Play Hindi"):
                st.audio(hindi_audio)

    except Exception as e:
        st.error(f"Error generating caption: {e}")

# ---------------- CLEANUP ----------------
def cleanup():
    try:
        for file in os.listdir(tempfile.gettempdir()):
            if file.endswith(".mp3"):
                os.remove(os.path.join(tempfile.gettempdir(), file))
    except:
        pass
