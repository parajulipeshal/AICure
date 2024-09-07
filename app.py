import streamlit as st

# Unique name for the app
APP_NAME = "AICure"

# Function to analyze symptoms and determine the disease
def analyze_symptoms(symptoms):
    # Example symptoms list for malaria
    malaria_symptoms = [
        "fever", "chills", "sweats", "headache", "muscle pain",
        "joint pain", "fatigue", "weakness", "nausea", "vomiting",
        "abdominal pain", "diarrhea", "anemia", "jaundice"
    ]
    
    # Check if any of the input symptoms match the list of malaria symptoms
    if any(symptom in malaria_symptoms for symptom in symptoms):
        return "Malaria"
    return "Unknown disease"

# Function to show precautions and medication for malaria
def show_precautions_and_medication():
    precautions = """
    - Avoid mosquito bites by using insect repellent.
    - Wear long sleeves and pants.
    - Sleep under a mosquito net.
    - Use mosquito screens on windows and doors.
    """
    
    medication = """
    - Antimalarial drugs such as chloroquine, artemisinin-based combination therapies (ACTs), or others prescribed by a healthcare provider.
    - It's important to follow the full course of medication as prescribed.
    """
    
    st.subheader("Precautions")
    st.write(precautions)
    
    st.subheader("Medication")
    st.write(medication)

# Streamlit app layout with background image
page_bg_img = '''
<style>
.stApp {
    background-image: url("background.jpeg");
    background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title(f"{APP_NAME} Navigation")
option = st.sidebar.radio("Choose an option", ["Home", "Diagnose", "About"])

if option == "Home":
    st.title(f"Welcome to {APP_NAME}")
    
    st.subheader(f"What is {APP_NAME}?")
    st.write(f"{APP_NAME} is a simple, user-friendly disease diagnosis app designed to help people in rural and underserved areas identify possible diseases based on their symptoms. It offers a preliminary guide before consulting a healthcare professional.")
    
    st.subheader(f"Why {APP_NAME}?")
    st.write(f"{APP_NAME} serves as a bridge for healthcare access in remote areas, providing AI-driven symptom analysis and guiding users with advice on next steps. It empowers communities with limited healthcare facilities.")
    
    st.subheader(f"How is {APP_NAME} Developed?")
    st.write(f"{APP_NAME} is developed using **Python** and the **Streamlit** framework. The app leverages AI to match common symptoms with possible diseases, starting with basic analysis and scalable to integrate more advanced AI/ML models for better diagnosis in the future.")

elif option == "Diagnose":
    st.title(f"Diagnose with {APP_NAME}")
    
    # User input
    symptoms_input = st.text_input("Enter your symptoms separated by commas:")
    
    # Store the analysis result and button states
    if "disease_name" not in st.session_state:
        st.session_state.disease_name = None
    if "show_precautions" not in st.session_state:
        st.session_state.show_precautions = False
    
    if st.button("Analyze Output"):
        if symptoms_input:
            symptoms_list = [symptom.strip().lower() for symptom in symptoms_input.split(',')]
            st.session_state.disease_name = analyze_symptoms(symptoms_list)
        else:
            st.write("Please enter your symptoms.")
    
    if st.session_state.disease_name:
        st.write(f"**Disease Name:** {st.session_state.disease_name}")
        
        if st.session_state.disease_name == "Malaria":
            st.session_state.show_precautions = st.button("Show Precautions and Medication")
            
            if st.session_state.show_precautions:
                show_precautions_and_medication()

elif option == "About":
    st.title("About Me")
    st.image("profile.jpg", width=200)
    st.write("**Peshal Parajuli**")
    st.write("Social Media:")
    st.write("[LinkedIn](https://www.linkedin.com/in/peshal-parajuli-7b401926b/)")
    st.write("[Facebook](https://www.facebook.com/krishalparajuli18)")
    st.write("[GitHub](https://www.github.com/parajulipeshal)")
