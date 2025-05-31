import streamlit as st
import plotly.express as px

# Label-to-name mapping (same as in predictor.py and app.py)
label_to_name = {
    "mel": "Melanoma",
    "nv": "Melanocytic Nevus (Mole)",
    "bcc": "Basal Cell Carcinoma",
    "akiec": "Actinic Keratoses / Bowen's Disease",
    "bkl": "Benign Keratosis-like Lesions",
    "df": "Dermatofibroma",
    "vasc": "Vascular Lesions"
}

def display_prediction_charts(confidence):
    chart_type = st.selectbox("Select Chart Type", ["Pie Chart", "Bar Chart"])

    # Replace abbreviations with full names
    labels = [label_to_name.get(label, label) for label in confidence.keys()]
    values = list(confidence.values())

    if chart_type == "Pie Chart":
        fig = px.pie(names=labels, values=values, title="Diagnosis Confidence")
    elif chart_type == "Bar Chart":
        fig = px.bar(x=labels, y=values, title="Diagnosis Confidence", labels={'x':"Type", 'y':"Confidence %"})

    st.plotly_chart(fig)

def display_risk_graph(risk):
    if risk <= 30:
        level = "Low Risk"
    elif risk <= 70:
        level = "Medium Risk"
    else:
        level = "High Risk"
    st.subheader(f"🚦 Risk Level: {level}")
    st.progress(int(risk))

def model_accuracy_sidebar():
    with st.sidebar:
        st.markdown("### 🧠 Model Info")
        st.write("Accuracy: **93.5%**")
        st.write("Model: DermatologyNet v1.0")
        st.write("Last Updated: 2024-12-01")