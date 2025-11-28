import streamlit as st
import cv2
import numpy as np
from PIL import Image
import os

# =========================
# Helper Functions
# =========================
def read_image(uploaded_file):
    """Convert uploaded file into OpenCV BGR image."""
    image = Image.open(uploaded_file).convert("RGB")
    arr = np.array(image)
    return cv2.cvtColor(arr, cv2.COLOR_RGB2BGR)

def to_pil(bgr):
    """Convert OpenCV BGR image back to RGB for Streamlit display."""
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    return Image.fromarray(rgb)

def apply_gaussian_blur(bgr, ksize):
    """Apply Gaussian Blur filter."""
    if ksize % 2 == 0: ksize += 1
    return cv2.GaussianBlur(bgr, (ksize, ksize), 0)

def detect_objects(bgr, cascade_path, color=(0,255,0)):
    """Detect objects using Haar Cascade."""
    if not os.path.exists(cascade_path):
        st.error(f"❌ File not found: {cascade_path}")
        return bgr, 0
    cascade = cv2.CascadeClassifier(cascade_path)
    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    objects = cascade.detectMultiScale(gray, 1.1, 5)
    for (x, y, w, h) in objects:
        cv2.rectangle(bgr, (x, y), (x + w, y + h), color, 2)
    return bgr, len(objects)

# =========================
# Streamlit App UI
# =========================
st.set_page_config(page_title="AI Vision App", page_icon="🤖", layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown("""
    <style>
        /* Page background */
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #141E30, #243B55);
            color: white;
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0F2027, #203A43, #2C5364);
            color: white;
        }

        /* Titles */
        h1 {
            text-align: center;
            font-family: 'Trebuchet MS', sans-serif;
            color: #00adb5;
            text-shadow: 2px 2px 4px #000000;
        }

        h2, h3 {
            text-align: center;
            color: #eeeeee;
        }

        /* Buttons */
        div.stButton > button {
            background-color: #00adb5;
            color: white;
            border-radius: 12px;
            border: none;
            padding: 0.7em 1.4em;
            font-size: 1em;
            font-weight: 600;
            transition: all 0.3s ease-in-out;
        }

        div.stButton > button:hover {
            background-color: #007b83;
            transform: scale(1.05);
        }

        /* Slider text */
        .stSlider label {
            color: #00e0ff !important;
            font-weight: bold;
        }

        /* Upload section */
        .stFileUploader label {
            font-size: 1.1em !important;
            color: #00adb5 !important;
            font-weight: 600 !important;
        }

        /* Footer note */
        footer {
            visibility: hidden;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- APP TITLE ----------
st.markdown("<h1>🖼️ AI Vision & Image Processing App</h1>", unsafe_allow_html=True)
st.markdown("<h3>Upload an image and apply cool computer vision operations!</h3>", unsafe_allow_html=True)
st.write(" ")

# ---------- SIDEBAR ----------
st.sidebar.header("⚙️ Settings & Operations")
operation = st.sidebar.selectbox(
    "Choose an operation:",
    ["None", "Apply Gaussian Blur", "Detect Faces", "Detect Cats", "Detect Cars"]
)

uploaded_file = st.file_uploader("📸 Upload an image (JPG or PNG)", type=["jpg", "jpeg", "png"])

# ---------- MAIN FUNCTIONALITY ----------
if uploaded_file is not None:
    bgr = read_image(uploaded_file)
    st.image(to_pil(bgr), caption="🎯 Original Image", use_container_width=True)
    st.write("---")

    if operation == "Apply Gaussian Blur":
        k = st.sidebar.slider("Blur Strength (odd number)", 1, 99, 11, step=2)
        blurred = apply_gaussian_blur(bgr, k)
        st.image(to_pil(blurred), caption="🌫️ Blurred Image", use_container_width=True)

    elif operation == "Detect Faces":
        path = "cascades/haarcascade_frontalface_default.xml"
        out, count = detect_objects(bgr, path, (0,255,0))
        st.image(to_pil(out), caption=f"🧑‍🦰 Detected {count} Face(s)", use_container_width=True)

    elif operation == "Detect Cats":
        path = "cascades/haarcascade_frontalcatface.xml"
        out, count = detect_objects(bgr, path, (255,0,0))
        st.image(to_pil(out), caption=f"🐱 Detected {count} Cat(s)", use_container_width=True)

    elif operation == "Detect Cars":
        path = "cascades/haarcascade_car.xml"
        out, count = detect_objects(bgr, path, (0,0,255))
        st.image(to_pil(out), caption=f"🚗 Detected {count} Car(s)", use_container_width=True)

    else:
        st.info("✨ Select an operation from the sidebar to begin.")
else:
    st.warning("⬆️ Please upload an image first to continue.")

# ---------- FOOTER ----------
st.markdown("<br><hr><center>💻 Developed by Maryam — Powered by Streamlit & OpenCV 🚀</center>", unsafe_allow_html=True)
