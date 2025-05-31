def get_treatment_info(cancer_type):
    info_db = {
        "Melanoma": {
            "treatment": "Surgical removal is the most common treatment. In advanced cases, Immunotherapy (like checkpoint inhibitors), Targeted therapy, and Chemotherapy may be used.",
            "precautions": "Avoid sun exposure, use SPF 50+ sunscreen, perform regular skin self-exams, and schedule annual dermatological check-ups."
        },
        "Vascular Lesions": {
            "treatment": "Laser therapy (e.g., pulsed dye laser), sclerotherapy, or surgical excision depending on severity.",
            "precautions": "Avoid heat and sun exposure, and consult a specialist if there’s bleeding or rapid growth."
        },
        "Actinic Keratoses and Intraepithelial Carcinoma (Bowen's Disease)": {
            "treatment": "Cryotherapy, topical chemotherapy (5-FU), photodynamic therapy, or surgical excision.",
            "precautions": "Avoid UV exposure, wear protective clothing, and undergo routine screenings."
        },
        "Melanocytic Nevus (Mole)": {
            "treatment": "Generally benign; surgical removal if atypical or cosmetically concerning.",
            "precautions": "Monitor for changes in size, shape, or color (ABCDE rule). Avoid excessive sun exposure."
        },
        "Dermatofibroma": {
            "treatment": "Usually no treatment needed. Surgical excision or laser therapy if painful or bothersome.",
            "precautions": "Monitor for irritation or bleeding. No specific preventive measures required."
        },
        "Benign Keratosis-like Lesions": {
            "treatment": "Cryotherapy, laser therapy, or shave removal for cosmetic reasons. Typically harmless.",
            "precautions": "No specific precautions. Monitor for unusual changes to rule out malignancy."
        },
        "Basal Cell Carcinoma": {
            "treatment": "Mohs surgery, excision, cryotherapy, or topical medications (e.g., imiquimod).",
            "precautions": "Avoid tanning beds, use broad-spectrum sunscreen, and schedule regular skin exams."
        }
    }

    # Fall back in case of unexpected labels
    entry = info_db.get(cancer_type, {
        "treatment": "Consult a board-certified dermatologist for proper diagnosis and treatment.",
        "precautions": "Follow general skin protection and health practices."
    })

    return f"### 🩺 Treatment\n{entry['treatment']}\n\n### 🚧 Precautions\n{entry['precautions']}"
