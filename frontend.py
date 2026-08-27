import streamlit as st
import requests

API_URL='http://127.0.0.1:8000/predict'

st.title("Insurance premium Category Prediction")

st.markdown("Enter you details below:")


# input fields

age=st.number_input("Age",max_value=119)
weight=st.number_input("Weight (kgs)",min_value=1.0)
height=st.number_input("Height (m)",min_value=0.5, max_value=2.5)
income_lpa=st.number_input("Income in LPA",min_value=0.1)
city=st.text_input("Enter your city",value='Mumbai')
smoker=st.selectbox("Are you a smoker?",options=['True','False'])
occupation=st.selectbox("Occupation",['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'])



if st.button('Predict premum category'):
    input_data={
      "age":age,
      "weight":weight,
      "height": height,
      "income_lpa": income_lpa,
      "smoker": smoker,
      "city": city,
      "occupation":occupation
   }


    try: 
        response=requests.post(API_URL,json=input_data)
        print(response.status_code)
        if response.status_code==200:
            print("execution 1")
            result=response.json()
            print("execution 2")
            st.success(f"Predicted Insurance premium category:**{result['predicted_category']}**")
            print("execution 3")
        else:
            print("execution 4")
            st.error(f'PI Error{response.status_code}-{response.text}')
            print("execution 5")

    except requests.exceptions.ConnectionError:
        st.error("Could not connect to FastAPI server. Make sure its running on port 8000")
        print("execution 6")