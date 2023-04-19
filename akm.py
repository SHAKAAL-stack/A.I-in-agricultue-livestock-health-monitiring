import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Animal Health Prediction and Prevention")
root.geometry("400x300")

# Create labels and input fields for data entry
label1 = tk.Label(root, text="Body temperature:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Heart rate:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

label3 = tk.Label(root, text="Skin color:")
label3.pack()
entry3 = tk.Entry(root)
entry3.pack()

label4 = tk.Label(root, text="Animal name:")
label4.pack()
entry4 = tk.Entry(root)
entry4.pack()

# Create a button to trigger the prediction and prevention function
def predict_prevent():
    # Retrieve the input values
    temp = float(entry1.get())
    hr = float(entry2.get())
    skin_color = entry3.get()
    animal = entry4.get()

    # Create a dictionary of pre-built healthcare information
    healthcare_info = {

        "cow": {
            "normal_temp": [38.4, 40.2],
            "normal_hr": [48, 58],
            "skin_color": ["black", "white", "brown"],
            "diseases": {
                "Mastitis": {
                    "symptoms": 
                        ["swelling of the udder", 
                        "loss of appetite", "fever"],
                    "prevention":
                        ["regular milking", 
                        "keeping the udder clean and dry"]
                },
                "Bovine Respiratory Disease": {
                    "symptoms": 
                        ["coughing", "nasal discharge", "fever"],
                    "prevention": 
                        ["vaccination", "good ventilation in barns"]
                }
            }
        },

        "sheep": {
            "normal_temp": [38.2, 40],
            "normal_hr": [70, 80],
            "skin_color": ["black", "white"],
            
            "disease": {
                "Foot rot": {
                    "prevention": 
                        "Foot trimming",
                    "symptoms": 
                        ["Limping", "Swelling and redness between the toes"]
                },
                "Scrapie": {
                    "prevention": 
                        "Genetic testing and culling",
                    "symptoms": 
                        ["Behavioral changes", "Tremors", "Itching and rubbing"]
                },
                "Pneumonia": {
                    "prevention": 
                        "Vaccination and proper ventilation",
                    "symptoms": 
                        ["Coughing", "Fever", "Nasal discharge", "Rapid breathing"]
                }
            }
        },

        "goat": {
            "normal_temp": [38.6, 40],
            "normal_hr": [70, 80],
            "skin_color": ["black", "white", "brown"],
            "diseases": {
                "Caprine Arthritis and Encephalitis": {
                    "symptoms": 
                        ["lameness", "muscle wasting", "fever"],
                    "prevention": 
                        ["testing for the virus before introducing new goats", 
                        "separating infected goats from the herd"]
                },
                "Contagious Ecthyma": {
                    "symptoms": 
                        ["sores on lips and mouth", "fever"],
                    "prevention": 
                        ["vaccination", 
                        "keeping the animals in a clean and dry environment"]
                }
            }
        },
        "buffalo": {
            "normal_temp": [39.4, 41],
            "normal_hr": [50, 60],
            "skin_color": ["black", "brown"],
            "diseases": {
                "Foot and Mouth Disease": {
                    "symptoms": 
                        ["blister-like sores on mouth, feet, and teats", 
                        "fever"],
                    "prevention": 
                        ["vaccination", 
                        "maintaining good hygiene and cleanliness"]
                },
                "Anthrax": {
                    "symptoms": 
                        ["sudden death", "bloody discharge from body openings"],
                    "prevention": 
                        ["vaccination", "proper disposal of infected animals"]
                }
            }
        },
        "pig": {
            "normal_temp": [38.4, 40],
            "normal_hr": [65, 75],
            "skin_color": ["pink", "black"],
            "diseases": {
                "Hyperthermia": {
                "prevention": 
                    "Provide cool water and shade",
                "symptoms": 
                    ["Excessive panting", 
                    "Reddened gums and moist tissues of the body", 
                    "Production of only small amounts of urine"],
                },
                "Tachycardia": {
                    "prevention": 
                        "Maintain a healthy weight and regular exercise",
                    "symptoms": 
                        ["Rapid heart rate", "Weakness", "Fainting"],
                },
                "Swine flu": {
                    "prevention": 
                        "Vaccinate the pig and maintain good hygiene",
                    "symptoms": 
                        ["Fever", "Cough", "Sore throat"],
                }
            }
        }
    }

    # Perform the prediction and prevention
    if animal.lower() not in healthcare_info:
        result_label = tk.Label(root, text="Invalid animal name")
        result_label.pack()
    else:
        animal_info = healthcare_info[animal.lower()]
        if any(temp > t for t in animal_info["normal_temp"]):
            prevention = animal_info["diseases"]
            result_label = tk.Label(root, text=f"The animal's temperature is too high. Prevention measures: \n{prevention}")
            result_label.pack()
        elif any(hr > r for r in animal_info["normal_hr"]):
            prevention = animal_info["diseases"]
            result_label = tk.Label(root, text=f"The animal's heart rate is too high. Prevention measures: \n{prevention}")
            result_label.pack()
        elif skin_color.lower() not in animal_info["skin_color"]:
            result_label = tk.Label(root, text=f"The animal's skin color is not normal for a \n{animal}.")
            result_label.pack()
        else:
            result_label = tk.Label(root, text="No matching animal health information found.")
            result_label.pack()


predict_button = tk.Button(root, text="Predict and Prevent", command=predict_prevent)
predict_button.pack()

# Start the main event loop
root.mainloop()
