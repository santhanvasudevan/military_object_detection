# import streamlit as st
# from ultralytics import YOLO
# from PIL import Image
# import tempfile
# import os

# # Load YOLO model
# model = YOLO("yolov8_model.pt")  # replace with your trained model path

# st.set_page_config(page_title="Object Detection App", layout="wide")
# st.title("🚀 Military Object Detection - YOLOv8")

# uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# if uploaded_file:
#     # Display original image
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.subheader("Uploaded Image")
#         image = Image.open(uploaded_file).convert("RGB")
#         st.image(image, use_container_width=True)

#     # Save to a temporary file
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:
#         image.save(temp.name)
#         temp_path = temp.name

#     # Run YOLO inference
#     results = model(temp_path, conf=0.10)

#     # Save result image
#     result_img_path = os.path.splitext(temp_path)[0] + "_result.jpg"
#     results[0].save(filename=result_img_path)

#     # Show detected image
#     with col2:
#         st.subheader("Detected Image")
#         st.image(result_img_path, use_container_width=True)

#     # Optional: show detected objects' labels
#     st.markdown("### Detected Objects")
#     for box in results[0].boxes:
#         cls = int(box.cls[0])
#         conf = float(box.conf[0])
#         label = model.names[cls]
#         st.write(f"- **{label}**: {conf:.2f}")


import streamlit as st
from PIL import Image
from ultralytics import YOLO
import tempfile
import os

# Load the model
model = YOLO("yolov8_model.pt")

# Tabs
tab1, tab2, tab3 = st.tabs(["📸 Detect Objects", "📊 About Model", "📈Model Performace report"])

# --- TAB 1: Object Detection ---
with tab1:
    st.title("YOLOv8 Object Detection")

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        # Display original image
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Uploaded Image")
            image = Image.open(uploaded_file).convert("RGB")
            st.image(image, use_container_width=True)

        # Save to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:
            image.save(temp.name)
            temp_path = temp.name

        # Run YOLO inference
        results = model(temp_path, conf=0.10)

        # Save result image
        result_img_path = os.path.splitext(temp_path)[0] + "_result.jpg"
        results[0].save(filename=result_img_path)

        # Show detected image
        with col2:
            st.subheader("Detected Image")
            st.image(result_img_path, use_container_width=True)

with tab2:
    st.title("📚 About the Model")

    st.header("📦 What is Object Detection?")
    st.markdown("""
    Object detection is a computer vision task that involves identifying and localizing multiple objects in an image.

    The model returns:
    - **Class Labels** (e.g., 'tank', 'soldier')
    - **Bounding Boxes** around detected objects
    - **Confidence Scores** indicating how sure the model is
    """)

    st.header("🔍 What is YOLO?")
    st.markdown("""
    **YOLO** (You Only Look Once) is a real-time object detection algorithm.
    It detects objects in a single forward pass through a neural network.
    Unlike traditional models that propose regions and classify them later, YOLO processes the entire image once, making it extremely fast and efficient.
    """)


# --- TAB 2: Model Insights ---
with tab3:
    st.title("Model Performance Metrics")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🧮 Confusion Matrix")
        st.markdown("""
        A **confusion matrix** shows how well the model performs per class.

        - Rows: Actual classes
        - Columns: Predicted classes
        - Diagonal: Correct predictions (higher is better)
        - Boxes out of diagonal: wrong predictions

        It helps in identifying classes the model often confuses.
        """)
        st.image("confusion_matrix_normalized.png", use_container_width=True)

    with col2:

        st.subheader("Precision-Recall curve")
        st.markdown("""
        - **🎯Precision**: Of all objects the model *predicted*, how many were correct? --> **High precision = fewer false positives.**
        
        - **🔁Recall**: Of all the *actual* objects present, how many did the model detect? --> **High recall = fewer false negatives.**
        
        > In object detection, ↑sing recall may ↓se precision and vice versa. It's a trade-off.
        """)
        st.image("PR_curve.png", use_container_width=True)

