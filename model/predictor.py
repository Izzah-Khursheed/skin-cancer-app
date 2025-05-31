from transformers import AutoProcessor, AutoModelForImageClassification
from PIL import Image
import torch

# Load model and processor
model_name = "ahishamm/vit-base-16-thesis-demo-HAM10000"
model = AutoModelForImageClassification.from_pretrained(model_name)
processor = AutoProcessor.from_pretrained(model_name)

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
    image = Image.open(image_file).convert("RGB")

    # Preprocess image
    inputs = processor(images=image, return_tensors="pt")

    # Inference
    with torch.no_grad():
        outputs = model(**inputs)

    # Get probabilities
    probs = torch.nn.functional.softmax(outputs.logits, dim=1)[0]

    # Get prediction
    confidence = {model.config.id2label[i]: float(probs[i]) * 100 for i in range(len(probs))}
    predicted_class = max(confidence, key=confidence.get)
    risk_score = confidence[predicted_class]

    # ✅ Map short label (e.g. 'bcc') to full name (e.g. 'Basal Cell Carcinoma')
    full_name = label_to_name.get(predicted_class, predicted_class)

    return full_name, confidence, risk_score


# def predict_skin_cancer(image_file):
#     image = Image.open(image_file).convert("RGB")

#     # Preprocess image
#     inputs = processor(images=image, return_tensors="pt")

#     # Inference
#     with torch.no_grad():
#         outputs = model(**inputs)

#     # Get probabilities
#     probs = torch.nn.functional.softmax(outputs.logits, dim=1)[0]

#     # Get prediction
#     confidence = {model.config.id2label[i]: float(probs[i]) * 100 for i in range(len(probs))}
#     predicted_class = max(confidence, key=confidence.get)
#     risk_score = confidence[predicted_class]

#     return predicted_class, confidence, risk_score
