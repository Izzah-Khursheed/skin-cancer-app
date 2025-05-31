import streamlit as st
from PIL import Image
from model.predictor import predict_skin_cancer
from utils.treatment_info import get_treatment_info
from utils.visualization import display_prediction_charts, display_risk_graph, model_accuracy_sidebar
from chatbot.groq_chatbot import groq_chatbot

# Mapping of labels to full names
label_to_name = {
    "mel": "Melanoma",
    "nv": "Melanocytic Nevus (Mole)",
    "bcc": "Basal Cell Carcinoma",
    "akiec": "Actinic Keratoses and Intraepithelial Carcinoma (Bowen's Disease)",
    "bkl": "Benign Keratosis-like Lesions",
    "df": "Dermatofibroma",
    "vasc": "Vascular Lesions"
}

st.set_page_config(page_title="Skin Cancer AI", layout="wide")
st.sidebar.title("🧠 AI Skin Cancer Assistant")
model_accuracy_sidebar()

st.title("🧬 AI-Powered Skin Cancer Detection & Help Desk")

tabs = st.tabs(["📁 Upload & Predict", "📘 Treatment Info", "📊 Visualization", "💬 Chatbot"])

# Tab 1: Upload & Predict
with tabs[0]:
    st.header("📁 Upload a Skin Image for Prediction")

    with st.expander("📂 View Sample Images"):
        cols = st.columns(3)
        sample_images = [
            ("melanoma_sample.jpg", "Melanoma"),
            ("bcc_sample.jpg", "Basal Cell Carcinoma"),
            ("nevus_sample.jpg", "Melanocytic Nevus (Mole)"),
            ("akiec_sample.jpg", "Actinic Keratoses and Intraepithelial Carcinoma (Bowen's Disease)"),
            ("bkl_sample.jpg", "Benign Keratosis-like Lesions"),
            ("df_sample.jpg", "Dermatofibroma"),
            ("vasc_sample.jpg", "Vascular Lesions")
        ]
        for i, (img_file, label) in enumerate(sample_images):
            with cols[i % 3]:
                st.image(f"assets/example_images/{img_file}", caption=label, use_container_width=True)

    uploaded_file = st.file_uploader("Upload a skin image (jpg/png)", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded Image", use_container_width=True)
        st.write("🔍 Making prediction...")

        # Run prediction
        prediction, confidences, risk_score = predict_skin_cancer(uploaded_file)

        # Display full name but store short label
        full_prediction_name = label_to_name.get(prediction, prediction)

        st.success(f"Predicted: {full_prediction_name}")
        st.write("Confidence Scores:", {
            label_to_name.get(k, k): round(v, 2) for k, v in confidences.items()
        })

        # Store ORIGINAL prediction key
        st.session_state['last_prediction'] = prediction
        st.session_state['last_confidences'] = confidences
        st.session_state['last_risk'] = risk_score

# Tab 2: Treatment Info
with tabs[1]:
    st.header("📘 Treatment & Precautions")
    if 'last_prediction' in st.session_state:
        info = get_treatment_info(st.session_state['last_prediction'])
        st.markdown(info)  # FIXED: Use markdown to render Markdown properly
    else:
        st.warning("Please upload an image first to get treatment suggestions.")

# Tab 3: Visualization
with tabs[2]:
    st.header("📊 Prediction Breakdown")
    if 'last_confidences' in st.session_state:
        display_prediction_charts(st.session_state['last_confidences'])
        display_risk_graph(st.session_state['last_risk'])
    else:
        st.info("Please upload an image to view visualizations.")

# Tab 4: Chatbot
with tabs[3]:
    st.header("💬 Skin Health Chatbot")
    user_input = st.text_input(
        "Ask a question related to skin diseases...",
        placeholder="E.g., What are the early signs of Melanoma?"
    )
    if user_input:
        response = groq_chatbot(user_input)
        st.markdown(f"**🤖 Answer:**<br>{response}", unsafe_allow_html=True)
