from transformers import AutoImageProcessor, BeitForImageClassification
from PIL import Image
import torch

# # Load model and processor
model_name = "ALM-AHME/beit-large-patch16-224-finetuned-Lesion-Classification-HAM10000-AH-60-20-20"
model = BeitForImageClassification.from_pretrained(model_name)
processor = AutoImageProcessor.from_pretrained(model_name)

# Optional mapping for full names (same as in app.py)
label_to_name = {
    "mel": "Melanoma",
    "nv": "Melanocytic Nevus (Mole)",
    "bcc": "Basal Cell Carcinoma",
    "akiec": "Actinic Keratoses and Intraepithelial Carcinoma (Bowen's Disease)",
    "bkl": "Benign Keratosis-like Lesions",
    "df": "Dermatofibroma",
    "vasc": "Vascular Lesions"
}


def predict_skin_cancer(image_file):
    try:
        image = Image.open(image_file).convert("RGB")
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None, {}, 0

    # Preprocess image
    inputs = processor(images=image, return_tensors="pt")

    # Inference
    with torch.no_grad():
        outputs = model(**inputs)

    # Get probabilities
    probs = torch.nn.functional.softmax(outputs.logits, dim=1)[0]

    # Convert to dict of confidences
    confidence = {model.config.id2label[i]: float(probs[i]) * 100 for i in range(len(probs))}
    predicted_class = max(confidence, key=confidence.get)
    predicted_confidence = confidence[predicted_class]

    # Define medical risk levels per class
    medical_risk_weight = {
        "mel": 1.0,    # Melanoma - highest risk
        "akiec": 0.9,  # Pre-cancerous
        "bcc": 0.8,    # Carcinoma
        "bkl": 0.3,    # Benign
        "df": 0.2,     # Benign
        "nv": 0.1,     # Mole
        "vasc": 0.1    # Benign
    }

    # Compute risk score
    risk_score = predicted_confidence * medical_risk_weight.get(predicted_class, 0.1)

    return predicted_class, confidence, risk_score
