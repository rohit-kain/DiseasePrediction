import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
diabetes_model = pickle.load(open('./models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('./models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('./models/parkinsons_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level', help='Enter your Glucose level.')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value', help='Enter your BP.')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value', help='Enter your skin thickness in mm.')

    with col2:
        Insulin = st.text_input('Insulin Level', help='Enter your insulin level.')

    with col3:
        BMI = st.text_input('BMI value', help='Enter your Body Mass Ratio.')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value', help='Enter your DiabetesPedigreeFunction.')

    with col2:
        Age = st.text_input('Age of the Person', help='Enter your age.')

    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction
    if st.button('Diabetes Test Result'):
        try:
            input_values = [float(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness),
                            float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age)]

            diab_prediction = diabetes_model.predict([input_values])

            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'

            

        except ValueError:
            st.error("Please enter valid numeric values for input features.")

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age', help='Enter your age.')

    with col2:
        # sex = st.text_input('Sex', help='Enter a numerical value.')
        sex = st.selectbox("Sex",('Male','Female'))
        if sex=='Male':
            sex=0
        else:
            sex=1

    with col3:
        #cp = st.text_input('Chest Pain types', help='Enter a numerical value.')
        cp = st.selectbox('Chest Pain Types',('asymptomatic','atypical angina','non-anginal pain','typical angina'))
        if cp == 'asymptomatic':
            cp=0
        elif cp == 'atypical angina':
            cp=1
        elif cp == 'non-aginal pain':
            cp=2
        else:
            cp=3

    with col1:
        trestbps = st.text_input('Resting Blood Pressure', help='Blood Pressure at rest.')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl', help='total cholesterol in blood.')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl', help='sugar (glucose) in your blood.')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results', help='electrical activity of the heart.')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        #exang = st.text_input('Exercise Induced Angina', help='Enter a numerical value.')
        exang = st.selectbox("Exercise Induced Angina",('yes','no'),help="do you have Angina pain")
        if exang == 'yes':
            exang = 1
        else:
            exang = 0

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise', help='Enter a numerical value.')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment', help='Enter a numerical value.')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy', help='Enter a numerical value.')

    with col1:
        #thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', help='Enter a numerical value.')
        thal =  st.selectbox("thalassemia",("none","fixed defect","normal","reversible defect"),help="A blood disorder")
        if thal == "none":
            thal = 0
        elif thal == "fixed defect":
            thal = 1
        elif thal == "normal":
            thal = 2
        else:
            thal = 3

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        try:
            input_values = [float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs),
                            float(restecg), float(thalach), float(exang), float(oldpeak), float(slope),
                            float(ca), float(thal)]

            heart_prediction = heart_disease_model.predict([input_values])

            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'

        except ValueError:
            st.error("Please enter valid numeric values for input features.")

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)', help='Enter a numerical value.')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)', help='Enter a numerical value.')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)', help='Enter a numerical value.')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)', help='Enter a numerical value.')
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)', help='Enter a numerical value.')
    with col1:
        RAP = st.text_input('MDVP:RAP', help='Enter a numerical value.')
    with col2:
        PPQ = st.text_input('MDVP:PPQ', help='Enter a numerical value.')
    with col3:
        DDP = st.text_input('Jitter:DDP', help='Enter a numerical value.')
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer', help='Enter a numerical value.')
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)', help='Enter a numerical value.')
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3', help='Enter a numerical value.')
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5', help='Enter a numerical value.')
    with col3:
        APQ = st.text_input('MDVP:APQ', help='Enter a numerical value.')
    with col4:
        DDA = st.text_input('Shimmer:DDA', help='Enter a numerical value.')
    with col5:
        NHR = st.text_input('NHR', help='Enter a numerical value.')
    with col1:
        HNR = st.text_input('HNR', help='Enter a numerical value.')
    with col2:
        RPDE = st.text_input('RPDE', help='Enter a numerical value.')
    with col3:
        DFA = st.text_input('DFA', help='Enter a numerical value.')
    with col4:
        spread1 = st.text_input('spread1', help='Enter a numerical value.')
    with col5:
        spread2 = st.text_input('spread2', help='Enter a numerical value.')
    with col1:
        D2 = st.text_input('D2', help='Enter a numerical value.')
    with col2:
        PPE = st.text_input('PPE', help='Enter a numerical value.')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction
    if st.button("Parkinson's Test Result"):
        try:
            input_values = [float(fo), float(fhi), float(flo), float(Jitter_percent), float(Jitter_Abs),
                            float(RAP), float(PPQ), float(DDP), float(Shimmer), float(Shimmer_dB),
                            float(APQ3), float(APQ5), float(APQ), float(DDA), float(NHR), float(HNR),
                            float(RPDE), float(DFA), float(spread1), float(spread2), float(D2), float(PPE)]

            parkinsons_prediction = parkinsons_model.predict([input_values])

            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease"

        except ValueError:
            st.error("Please enter valid numeric values for input features.")

    st.success(parkinsons_diagnosis)
