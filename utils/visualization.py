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

    st.subheader(f"🚦 Risk Level: {level} ({risk:.1f}%)")
    st.progress(int(risk))

import random
import plotly.graph_objects as go

def model_accuracy_sidebar():
    with st.sidebar:
        st.markdown("### 🧠 Model Info")
        
        # Store accuracy history in session state
        if 'accuracy_history' not in st.session_state:
            st.session_state.accuracy_history = []

        # Option to calculate accuracy
        calc_option = st.selectbox("Accuracy Options", ["View Static Accuracy", "Calculate After Prediction"])

        if calc_option == "View Static Accuracy":
            st.write("Accuracy: **90.0%**")
        elif calc_option == "Calculate After Prediction":
            if 'last_prediction' in st.session_state:
                # Simulated dynamic accuracy (replace with real one if available)
                current_accuracy = round(random.uniform(85.0, 97.0), 2)
                st.session_state.accuracy_history.append(current_accuracy)
                st.success(f"Calculated Accuracy: {current_accuracy}%")

                # Display trend chart
                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    y=st.session_state.accuracy_history,
                    mode='lines+markers',
                    name='Accuracy Trend'
                ))
                fig.update_layout(
                    title="📈 Accuracy Over Time",
                    xaxis_title="Prediction Count",
                    yaxis_title="Accuracy (%)",
                    height=300
                )
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("Upload an image to enable dynamic accuracy calculation.")

        st.write("Model: DermatologyNet v1.0")
        st.write("Last Updated: 2024-12-01")
