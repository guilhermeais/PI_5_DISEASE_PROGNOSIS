ALL_POSSIBLE_SYMPTOMS = [
    "itching", "skin_rash", "nodal_skin_eruptions", "continuous_sneezing", "shivering", "chills",
    "joint_pain", "stomach_pain", "acidity", "ulcers_on_tongue", "muscle_wasting", "vomiting",
    "burning_micturition", "spotting_ urination", "fatigue", "weight_gain", "anxiety",
    "cold_hands_and_feets", "mood_swings", "weight_loss", "restlessness", "lethargy",
    "patches_in_throat", "irregular_sugar_level", "cough", "high_fever", "sunken_eyes",
    "breathlessness", "sweating", "dehydration", "indigestion", "headache", "yellowish_skin",
    "dark_urine", "nausea", "loss_of_appetite", "pain_behind_the_eyes", "back_pain", "constipation",
    "abdominal_pain", "diarrhoea", "mild_fever", "yellow_urine", "yellowing_of_eyes",
    "acute_liver_failure", "fluid_overload", "swelling_of_stomach", "swelled_lymph_nodes", "malaise",
    "blurred_and_distorted_vision", "phlegm", "throat_irritation", "redness_of_eyes", "sinus_pressure",
    "runny_nose", "congestion", "chest_pain", "weakness_in_limbs", "fast_heart_rate",
    "pain_during_bowel_movements", "pain_in_anal_region", "bloody_stool", "irritation_in_anus",
    "neck_pain", "dizziness", "cramps", "bruising", "obesity", "swollen_legs", "swollen_blood_vessels",
    "puffy_face_and_eyes", "enlarged_thyroid", "brittle_nails", "swollen_extremeties", "excessive_hunger",
    "extra_marital_contacts", "drying_and_tingling_lips", "slurred_speech", "knee_pain",
    "hip_joint_pain", "muscle_weakness", "stiff_neck", "swelling_joints", "movement_stiffness",
    "spinning_movements", "loss_of_balance", "unsteadiness", "weakness_of_one_body_side",
    "loss_of_smell", "bladder_discomfort", "foul_smell_of urine", "continuous_feel_of_urine",
    "passage_of_gases", "internal_itching", "toxic_look_(typhos)", "depression", "irritability",
    "muscle_pain", "altered_sensorium", "red_spots_over_body", "belly_pain", "abnormal_menstruation",
    "dischromic _patches", "watering_from_eyes", "increased_appetite", "polyuria", "family_history",
    "mucoid_sputum", "rusty_sputum", "lack_of_concentration", "visual_disturbances",
    "receiving_blood_transfusion", "receiving_unsterile_injections", "coma", "stomach_bleeding",
    "distention_of_abdomen", "history_of_alcohol_consumption", "fluid_overload.1", "blood_in_sputum",
    "prominent_veins_on_calf", "palpitations", "painful_walking", "pus_filled_pimples", "blackheads",
    "scurring", "skin_peeling", "silver_like_dusting", "small_dents_in_nails", "inflammatory_nails",
    "blister", "red_sore_around_nose", "yellow_crust_ooze"
]

ALL_POSSIBLE_SYMPTOMS_PT_BR = {
  "General Symptoms": {
    "itching": "coceira",
    "skin_rash": "erupção cutânea",
    "nodal_skin_eruptions": "erupções cutâneas nodais",
    "continuous_sneezing": "espirros contínuos",
    "shivering": "arrepios",
    "chills": "calafrios",
    "joint_pain": "dor nas articulações",
    "muscle_wasting": "atrofia muscular",
    "fatigue": "fadiga",
    "weight_gain": "ganho de peso",
    "weight_loss": "perda de peso",
    "restlessness": "inquietação",
    "lethargy": "letargia",
    "fever": "febre",
    "mild_fever": "febre leve",
    "high_fever": "febre alta"
  },
  "Digestive Symptoms": {
    "stomach_pain": "dor de estômago",
    "acidity": "acidez",
    "ulcers_on_tongue": "úlceras na língua",
    "vomiting": "vômito",
    "burning_micturition": "micção ardente",
    "spotting_urination": "urinação com manchas",
    "indigestion": "indigestão",
    "abdominal_pain": "dor abdominal",
    "diarrhoea": "diarreia",
    "constipation": "constipação",
    "nausea": "náusea",
    "loss_of_appetite": "perda de apetite",
    "pain_behind_the_eyes": "dor atrás dos olhos",
    "back_pain": "dor nas costas"
  },
  "Respiratory Symptoms": {
    "cough": "tosse",
    "breathlessness": "falta de ar",
    "sweating": "suor",
    "dehydration": "desidratação",
    "high_fever": "febre alta",
    "sunken_eyes": "olhos fundos",
    "throat_irritation": "irritação na garganta",
    "redness_of_eyes": "vermelhidão nos olhos",
    "sinus_pressure": "pressão nos seios da face",
    "runny_nose": "nariz escorrendo",
    "congestion": "congestão",
    "chest_pain": "dor no peito"
  },
  "Urinary Symptoms": {
    "burning_micturition": "micção ardente",
    "spotting_urination": "urinação com manchas",
    "yellow_urine": "urina amarela",
    "yellowing_of_eyes": "amarelamento dos olhos",
    "foul_smell_of urine": "cheiro desagradável da urina",
    "continuous_feel_of_urine": "sensação contínua de urina"
  },
  "Neurological Symptoms": {
    "headache": "dor de cabeça",
    "dizziness": "tontura",
    "loss_of_balance": "perda de equilíbrio",
    "unsteadiness": "instabilidade",
    "weakness_of_one_body_side": "fraqueza de um lado do corpo",
    "altered_sensorium": "sensorium alterado",
    "movement_stiffness": "rigidez nos movimentos",
    "spinning_movements": "movimentos giratórios",
    "loss_of_smell": "perda de olfato",
    "coma": "coma"
  },
  "Dermatological Symptoms": {
    "patches_in_throat": "manchas na garganta",
    "yellowish_skin": "pele amarelada",
    "dark_urine": "urina escura",
    "red_spots_over_body": "manchas vermelhas no corpo",
    "belly_pain": "dor abdominal",
    "abnormal_menstruation": "menstruação anormal",
    "dischromic_patches": "manchas discrômicas",
    "watering_from_eyes": "olhos lacrimejantes",
    "increased_appetite": "aumento do apetite",
    "blackheads": "cravos",
    "scurrying": "escamação",
    "skin_peeling": "descamação da pele",
    "silver_like_dusting": "resíduo prateado",
    "small_dents_in_nails": "pequenos entalhes nas unhas",
    "inflammatory_nails": "unhas inflamadas",
    "blister": "bolha",
    "red_sore_around_nose": "vermelhidão ao redor do nariz",
    "yellow_crust_ooze": "crosta amarela"
  },
  "Cardiovascular Symptoms": {
    "cold_hands_and_feets": "mãos e pés frios",
    "fast_heart_rate": "ritmo cardíaco acelerado",
    "palpitations": "palpitações"
  },
  "Muscular and Articular Symptoms": {
    "muscle_weakness": "fraqueza muscular",
    "stiff_neck": "pescoço rígido",
    "swelling_joints": "inchaço nas articulações",
    "muscle_pain": "dor muscular",
    "knee_pain": "dor no joelho",
    "hip_joint_pain": "dor na articulação do quadril",
    "cramps": "câimbras",
    "bruising": "contusões"
  },
  "Psychological and Emotional Symptoms": {
    "anxiety": "ansiedade",
    "mood_swings": "oscilações de humor",
    "depression": "depressão",
    "irritability": "irritabilidade",
    "lack_of_concentration": "falta de concentração"
  },
  "Other Symptoms": {
    "patches_in_throat": "manchas na garganta",
    "irregular_sugar_level": "níveis irregulares de açúcar",
    "phlegm": "catarro",
    "runny_nose": "nariz escorrendo",
    "toxic_look_(typhos)": "aparência tóxica (tifo)",
    "family_history": "histórico familiar",
    "mucoid_sputum": "escarro mucoso",
    "rusty_sputum": "escarro enferrujado",
    "visual_disturbances": "distúrbios visuais",
    "receiving_blood_transfusion": "recebendo transfusão de sangue",
    "receiving_unsterile_injections": "recebendo injeções não estéreis",
    "stomach_bleeding": "hemorragia estomacal",
    "distention_of_abdomen": "distensão do abdômen",
    "history_of_alcohol_consumption": "histórico de consumo de álcool",
    "fluid_overload.1": "sobrecarga de fluido",
    "blood_in_sputum": "sangue no escarro",
    "prominent_veins_on_calf": "veias proeminentes na panturrilha",
    "painful_walking": "caminhada dolorosa",
    "pus_filled_pimples": "espinhas cheias de pus"
  }
}