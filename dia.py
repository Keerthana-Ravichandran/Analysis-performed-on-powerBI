import pickle
import streamlit as st
import numpy as np
from streamlit_option_menu import option_menu



diabetes_model = pickle.load(open('C:/Users/DELL/Desktop/disease prediction/saved models/diabetes_predictionmodel.sav', 'rb'))


with st.sidebar:
    
    selected = option_menu(' Diabetes Disease Prediction using Machine Learning',
                          
                          ['About Diabetes','Diabetes Disease Prediction','Symptoms','Diabetes risk factors','How to control Diabetes Disease'],
                          icons=['person','heart','activity'],
                          default_index=0)
    
    
if (selected == 'About Diabetes'):
        
        # page title
        st.title('Diabetes Disease')  
         
        st.header('TO KNOW MORE...')
        
        re=st.button('CLICK HERE')
        
        st.write(":smile:")
        
        
        if re:
            st.text(' Diabetes is a condition that happens when your blood sugar (glucose) is too high.')
            st.text(' It develops when your pancreas doesn’t make enough insulin .')
            st.text(' Diabetes affects people of all ages. ')
            st.text('Most forms of diabetes are chronic  and all forms are manageable with medications.')
            
       

if (selected == 'Diabetes Disease Prediction'):

# page title
    st.title('Diabetes Prediction using ML')
    
    



# getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
         Pregnancies = st.text_input('Number of Pregnancies')
    
    with col2:
         Glucose = st.text_input('Glucose Level')

    with col3:
          BloodPressure = st.text_input('Blood Pressure value')

    with col1:
          SkinThickness = st.text_input('Skin Thickness value')

    with col2:
           Insulin = st.text_input('Insulin Level')

    with col3:
         BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
         Age = st.text_input('Age of the Person')

    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        print(diab_prediction)
        if (diab_prediction[0] == 0):
          diab_diagnosis = 'The person is  not diabetic'
        else:
          diab_diagnosis = 'The person is  diabetic'
        
    st.success(diab_diagnosis)
    
    
    
if (selected == 'Symptoms'):
        st.title('Symptoms of diabetes')
        st.text('Diabetes symptoms are caused by rising blood sugar.')
        st.subheader('General symptoms') 
        st.text('The symptoms of type 1,type 2,and type 1.5 are the same,but they occur in a shorter period than types 2 & 1.5.')
        st.text('In type 2, the onset tends to be slower. Tingling nerves and slow-healing sores are more common in type 2')
        st.subheader('symptoms of diabetes include:')
        st.write(" - Increased hunger", text_align='center')
        st.write(" - Increased thirst", text_align='center')
        st.write(" - Weight loss ", text_align='center')
        st.write(" - Frequent urination", text_align='center')
        st.write(" - Blurry vision", text_align='center')
        st.write(" - Extreme fatigue", text_align='center')
        st.write(" - Sores that don’t heal", text_align='center')

        st.subheader('Symptoms in men')
        st.text('In addition to the general symptoms of diabetes, men with diabetes may have:')
        st.write(" - A decreased sex drive", text_align='center')
        st.write(" - erectile dysfunction", text_align='center')
        st.write(" - poor muscle strength", text_align='center')


        st.subheader('Symptoms in women')
        st.text('Women with diabetes can have symptoms such as:')
        st.write(" - Vaginal dryness", text_align='center')
        st.write(" - Urinary tract infections", text_align='center')
        st.write(" - Dry, itchy skin", text_align='center')
        
        
        
        st.subheader('Symptoms of Diabetes Complications')
        st.text('Have you already been diagnosed with diabetes but are concerned about symptoms')
        st.text(' that may be the result of complications related to diabetes?')
                
        rs=st.button('FIND OUT MORE')
        
        if rs:
            st.text('Complications associated with diabetes include:')
            st.write(" - Heart disease", text_align='center')
            st.write(" - Heart attack and stroke", text_align='center')
            st.write(" - Neuropathy", text_align='center')
            st.write(" - Nephropathy", text_align='center')
            st.write(" - Neuropathy", text_align='center')
            st.write(" - Retinopathy and vision loss", text_align='center')
            st.write(" - Hearing loss", text_align='center')
            st.write(" - Foot damage, such as infections and sores that don’t heal", text_align='center')
            st.write(" - Skin conditions, such as bacterial and fungal infections", text_align='center')
            st.write(" - Depression and dementia", text_align='center')
            







            
        
           
        
      
if (selected == 'Diabetes risk factors'):  
        st.title('Diabetes risk factors')
        st.text('Certain factors increase your risk for diabetes.')
        st.subheader('Type 1 Diabetes')
        st.text('Type 1 diabetes is thought to be caused by an immune reaction (the body attacks itself by mistake).')
        st.text('Risk factors for type 1 diabetes are not as clear as for prediabetes and type 2 diabetes.') 
        st.subheader('Known risk factors include:')
        st.write(" - Family history:", text_align='center')
        st.text('    Having a parent, brother, or sister with type 1 diabetes.')
        st.write(" - Age:", text_align='center')
        st.text('    You can get type 1 diabetes at any age, but it usually develops in children, teens, or young adults.')
        st.subheader('Type 2 Diabetes')
        st.text('Your risk for type 2 diabetes increases if you:')
        st.write(" - Are overweight", text_align='center')
        st.write(" - age 45 or older", text_align='center')
        st.write(" - Have a parent or sibling with the condition", text_align='center')
        st.write(" - Aren’t physically active", text_align='center')
        st.write(" - Have had gestational diabetes", text_align='center')
        st.write(" - Have prediabetes", text_align='center')
        st.write(" - Have high blood pressure, high cholesterol, or high triglycerides", text_align='center')
        st.subheader('Type 1.5 diabetes')
        st.text('Type 1.5 diabetes is found in adults over 30 and is often mistaken for type 2.')
        st.text('But people with this condition are not necessarily ')
        st.write(" - Are overweight", text_align='center')
        st.write(" - oral medications", text_align='center')
        st.write(" - Lifestyle changes have no effect.", text_align='center')





        
       

if (selected == 'How to control Diabetes Disease'):
    st.title('Coronary Artery Disease Risk factors')
    st.write('Coronary artery disease risk factors include:')
     
        
        
        