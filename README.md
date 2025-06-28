# 🧬 Skin Cancer Detection App

A user-friendly AI-powered web application for detecting different types of skin cancer using image classification, powered by a transformer-based model fine-tuned on the HAM10000 dataset. The app provides instant predictions, treatment guidelines, visual insights, and a conversational assistant to support awareness and education.

---

## ✅ Overview

Skin cancer is one of the most common types of cancer globally. Early detection is critical to improving survival rates and reducing treatment costs. This project aims to:

- Provide a reliable and accessible **AI-based tool** for classifying skin lesions.
- Support **early diagnosis** by allowing users to upload images for instant analysis.
- Educate users about potential **treatments** and **precautions**.
- Offer a **visual and conversational experience** through risk visualization and chatbot integration.

The app is deployed on **Streamlit** and integrated with **GitHub** for CI/CD. It uses a pre-trained **BEiT model** from Hugging Face for accurate skin lesion classification.

---

## 🧠 AI Model Details

- **Model Name:** `beit-large-patch16-224`
- **Pretrained Source:** Hugging Face Model
- **Architecture:** Vision Transformer (BEiT)
- **Fine-Tuned On:** HAM10000 skin lesion dataset
- **Prediction Output:** Skin lesion class and confidence score

---

## 📊 Dataset Summary

- **Dataset Name:** [HAM10000 ("Human Against Machine with 10000 training images")](https://www.kaggle.com/kmader/skin-cancer-mnist-ham10000)
- **Source:** Kaggle
- **Total Images:** 10,015 dermatoscopic images

### 🔬 Categories (7 Types):

- `mel` – Melanoma  
- `nv` – Melanocytic Nevus (Mole)  
- `bkl` – Benign Keratosis-like Lesions  
- `bcc` – Basal Cell Carcinoma  
- `akiec` – Actinic Keratoses and Intraepithelial Carcinoma  
- `vasc` – Vascular Lesions  
- `df` – Dermatofibroma  

---

## 💡 Features Description

The app consists of **four main interactive tabs**:

### 1. 📤 Upload & Predict
- Upload an image of a skin lesion in any format (`.png`, `.jpg`, `.jpeg`, etc.).
- The model classifies the lesion type and displays:
  - **Predicted class**
  - **Confidence score**

### 2. 💊 Treatment Info
- Shows tailored information for the predicted cancer type.
- Includes:
  - Recommended treatments  
  - Preventive measures  

### 3. 📈 Visualization
- Visualizes prediction results in two formats:
  - **Bar chart** for confidence scores across all classes
  - **Pie chart** for percentage-based prediction
- Displays **Risk level** of the predicted class.

### 4. 💬 Chatbot (Groq API)
- An AI-powered chatbot for answering skin cancer-related questions.
- Integrated via **Groq API** for fast and intelligent responses.

---

## 🛠️ Setup & Installation

### ✅ Requirements

Make sure you have Python 3.9+ and the following packages installed:

- `streamlit`
- `transformers`
- `matplotlib`, `seaborn`
- `PIL` (`pillow`)
- `torch`
- `numpy`
- `pandas`
- **Groq API key** (required for chatbot tab)

### 🔧 Installation Steps

```bash
# 1. Clone the repository
git clone https://github.com/your-username/skin-cancer-app.git
cd skin-cancer-app

# 2. Install required libraries
pip install -r requirements.txt

# 3. Run the Streamlit app
streamlit run app.py
