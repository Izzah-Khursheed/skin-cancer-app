def get_treatment_info(cancer_type):
    info_db = {
    "mel": {
        "treatment": [
            "Surgical removal (wide local excision) is the primary treatment for melanoma.",
            "In advanced or metastatic cases, treatment options include immunotherapy (e.g., checkpoint inhibitors like pembrolizumab or nivolumab).",
            "Targeted therapy (for BRAF-mutated melanoma) may be used.",
            "Chemotherapy and radiation therapy are additional options in some cases.",
            "Early detection and complete excision significantly improve prognosis."
        ],
        "precautions": [
            "Avoid direct sun exposure during peak hours (10 AM - 4 PM).",
            "Use broad-spectrum sunscreen with SPF 50+ daily.",
            "Wear protective clothing, hats, and sunglasses.",
            "Perform regular monthly skin self-examinations for new or changing moles or lesions.",
            "Schedule annual dermatological check-ups for early detection and monitoring."
        ]
    },
    "vasc": {
        "treatment": [
            "Treatment depends on severity and type of vascular lesion.",
            "Common options include laser therapy (such as pulsed dye laser) to reduce redness and remove superficial lesions.",
            "Sclerotherapy is used for larger or deeper lesions.",
            "Surgical excision may be necessary for problematic or bleeding lesions.",
            "Consult a vascular specialist or dermatologist for individualized management."
        ],
        "precautions": [
            "Avoid exposure to heat sources and sun to prevent lesion aggravation.",
            "Protect the affected area from trauma to avoid bleeding or infection.",
            "Monitor for any rapid growth, bleeding, or changes in color.",
            "Seek specialist consultation if symptoms worsen."
        ]
    },
    "akiec": {
        "treatment": [
            "Common treatments include cryotherapy (liquid nitrogen freezing).",
            "Topical chemotherapeutic agents like 5-fluorouracil (5-FU) are often used.",
            "Photodynamic therapy (PDT) is another option.",
            "Surgical excision is considered in severe or non-responsive cases.",
            "Early treatment prevents progression to invasive squamous cell carcinoma."
        ],
        "precautions": [
            "Avoid prolonged UV exposure by wearing protective clothing.",
            "Apply broad-spectrum sunscreen regularly.",
            "Attend routine skin screenings to monitor lesion changes.",
            "Avoid tanning beds.",
            "Use sun avoidance strategies especially if immunosuppressed."
        ]
    },
    "nv": {
        "treatment": [
            "Melanocytic nevi (moles) are generally benign and usually do not require treatment.",
            "Surgical removal may be considered if lesions are atypical or symptomatic.",
            "Removal may also be for cosmetic reasons.",
            "Regular monitoring is important to detect any malignant transformation early."
        ],
        "precautions": [
            "Perform regular self-exams using the ABCDE rule (Asymmetry, Border irregularity, Color variation, Diameter >6mm, Evolving).",
            "Avoid excessive sun exposure and tanning beds.",
            "Use sunscreen daily and wear protective clothing."
        ]
    },
    "df": {
        "treatment": [
            "Dermatofibromas are usually harmless and often require no treatment.",
            "Surgical excision or laser therapy can be done if lesions are painful, itchy, or cosmetically concerning.",
            "Recurrence after excision is uncommon."
        ],
        "precautions": [
            "Monitor lesions for changes in size, shape, or color.",
            "Avoid irritation or trauma to the lesion.",
            "Generally, no specific preventive measures are necessary."
        ]
    },
    "bkl": {
        "treatment": [
            "Benign keratosis-like lesions can be treated with cryotherapy, laser therapy, or shave removal.",
            "These treatments are usually for cosmetic purposes.",
            "Lesions are typically harmless but should be monitored."
        ],
        "precautions": [
            "No specific precautions are required.",
            "Monitor for unusual changes such as rapid growth, bleeding, or color changes.",
            "Maintain regular dermatological check-ups if you have a history of skin lesions."
        ]
    },
    "bcc": {
        "treatment": [
            "Basal Cell Carcinoma is typically treated with Mohs micrographic surgery or standard excision.",
            "Cryotherapy or topical medications like imiquimod or 5-FU may be used.",
            "Radiation therapy is an option for patients who cannot undergo surgery.",
            "Early treatment leads to excellent prognosis."
        ],
        "precautions": [
            "Avoid tanning beds and excessive UV exposure.",
            "Use broad-spectrum sunscreen daily and wear protective clothing.",
            "Perform regular skin self-exams.",
            "Schedule frequent dermatological evaluations, especially if you have fair skin or a history of skin cancer."
        ]
    }
    }



    
    # info_db = {
    # "mel": {
    #     "treatment": (
    #         "Surgical removal (wide local excision) is the primary treatment for melanoma. "
    #         "In advanced or metastatic cases, treatment options include immunotherapy (e.g., checkpoint inhibitors like pembrolizumab or nivolumab), "
    #         "targeted therapy (for BRAF-mutated melanoma), chemotherapy, and radiation therapy. "
    #         "Early detection and complete excision significantly improve prognosis."
    #     ),
    #     "precautions": (
    #         "Avoid direct sun exposure during peak hours (10 AM - 4 PM). Use broad-spectrum sunscreen with SPF 50+ daily. "
    #         "Wear protective clothing, hats, and sunglasses. Perform regular monthly skin self-examinations for new or changing moles or lesions. "
    #         "Schedule annual dermatological check-ups for early detection and monitoring."
    #     )
    # },
    # "vasc": {
    #     "treatment": (
    #         "Treatment depends on severity and type of vascular lesion. "
    #         "Common options include laser therapy (such as pulsed dye laser) to reduce redness and remove superficial lesions, "
    #         "sclerotherapy for larger or deeper lesions, and surgical excision for problematic or bleeding lesions. "
    #         "Consult a vascular specialist or dermatologist for individualized management."
    #     ),
    #     "precautions": (
    #         "Avoid exposure to heat sources and sun to prevent lesion aggravation. "
    #         "Protect the affected area from trauma to avoid bleeding or infection. "
    #         "Monitor for any rapid growth, bleeding, or changes in color, and seek specialist consultation if such symptoms occur."
    #     )
    # },
    # "akiec": {
    #     "treatment": (
    #         "Common treatments include cryotherapy (liquid nitrogen freezing), topical chemotherapeutic agents like 5-fluorouracil (5-FU), "
    #         "photodynamic therapy (PDT), and surgical excision in severe or non-responsive cases. "
    #         "Early treatment prevents progression to invasive squamous cell carcinoma."
    #     ),
    #     "precautions": (
    #         "Avoid prolonged UV exposure by wearing protective clothing and applying broad-spectrum sunscreen regularly. "
    #         "Attend routine skin screenings to monitor lesion changes. "
    #         "Avoid tanning beds and use sun avoidance strategies especially if immunosuppressed."
    #     )
    # },
    # "nv": {
    #     "treatment": (
    #         "Melanocytic nevi (moles) are generally benign and usually do not require treatment. "
    #         "Surgical removal may be considered if lesions are atypical, symptomatic, or for cosmetic reasons. "
    #         "Regular monitoring is important to detect any malignant transformation early."
    #     ),
    #     "precautions": (
    #         "Perform regular self-exams using the ABCDE rule: Asymmetry, Border irregularity, Color variation, Diameter >6mm, and Evolving size or shape. "
    #         "Avoid excessive sun exposure and tanning beds. Use sunscreen daily and wear protective clothing."
    #     )
    # },
    # "df": {
    #     "treatment": (
    #         "Dermatofibromas are usually harmless and often require no treatment. "
    #         "If painful, itchy, or cosmetically concerning, options include surgical excision or laser therapy. "
    #         "Recurrence after excision is uncommon."
    #     ),
    #     "precautions": (
    #         "Monitor lesions for changes in size, shape, or color. "
    #         "Avoid irritation or trauma to the lesion. "
    #         "Generally, no specific preventive measures are necessary."
    #     )
    # },
    # "bkl": {
    #     "treatment": (
    #         "Benign keratosis-like lesions can be treated with cryotherapy, laser therapy, or shave removal for cosmetic purposes. "
    #         "They are typically harmless but should be monitored to rule out malignant transformation."
    #     ),
    #     "precautions": (
    #         "No specific precautions are required. "
    #         "Monitor for unusual changes in lesions such as rapid growth, bleeding, or color changes. "
    #         "Maintain regular dermatological check-ups if you have a history of skin lesions."
    #     )
    # },
    # "bcc": {
    #     "treatment": (
    #         "Basal Cell Carcinoma is typically treated with Mohs micrographic surgery, standard excision, cryotherapy, or topical medications like imiquimod or 5-FU. "
    #         "Radiation therapy is an option for patients who cannot undergo surgery. "
    #         "Early treatment leads to excellent prognosis."
    #     ),
    #     "precautions": (
    #         "Avoid tanning beds and excessive UV exposure by using broad-spectrum sunscreen daily and wearing protective clothing. "
    #         "Perform regular skin self-exams and schedule frequent dermatological evaluations, especially if you have fair skin or a history of skin cancer."
    #     )
    # }
    # }


    # Fall back in case of unexpected labels
    entry = info_db.get(cancer_type, {
        "treatment": "Consult a board-certified dermatologist for proper diagnosis and treatment.",
        "precautions": "Follow general skin protection and health practices."
    })

   def format_as_bullets(lines):
        return '\n'.join([f"- {line}" for line in lines])
        
    treatment_formatted = format_as_bullets(entry['treatment'])
    precautions_formatted = format_as_bullets(entry['precautions'])

    return f"### 🩺 Treatment\n{treatment_formatted}\n\n### 🚧 Precautions\n{precautions_formatted}"
