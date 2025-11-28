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
        st.error(f"File not found: {cascade_path}")
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
st.set_page_config(page_title="Image Processing App", layout="centered")
st.title("🖼️ Image Operations using Streamlit + OpenCV")
st.write("Upload an image and choose an operation to apply!")

uploaded_file = st.file_uploader("Upload an image (JPG or PNG)", type=["jpg", "jpeg", "png"])

operation = st.selectbox(
    "Choose an operation:",
    ["None", "Apply Gaussian Blur", "Detect Faces", "Detect Cats", "Detect Cars"]
)

if uploaded_file is not None:
    bgr = read_image(uploaded_file)
    st.image(to_pil(bgr), caption="Original Image", use_column_width=True)

    if operation == "Apply Gaussian Blur":
        k = st.slider("Blur Strength (odd number)", 1, 99, 11, step=2)
        blurred = apply_gaussian_blur(bgr, k)
        st.image(to_pil(blurred), caption="Blurred Image", use_column_width=True)

    elif operation == "Detect Faces":
        path = "cascades/haarcascade_frontalface_default.xml"
        out, count = detect_objects(bgr, path, (0,255,0))
        st.image(to_pil(out), caption=f"Detected {count} Faces", use_column_width=True)

    elif operation == "Detect Cats":
        path = "cascades/haarcascade_frontalcatface.xml"
        out, count = detect_objects(bgr, path, (255,0,0))
        st.image(to_pil(out), caption=f"Detected {count} Cat Faces", use_column_width=True)

    elif operation == "Detect Cars":
        path = "cascades/haarcascade_car.xml"
        out, count = detect_objects(bgr, path, (0,0,255))
        st.image(to_pil(out), caption=f"Detected {count} Cars", use_column_width=True)

    else:
        st.info("Select an operation to process the image.")
else:
    st.warning("Please upload an image first.")
