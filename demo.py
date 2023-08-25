import streamlit as st
import joblib
import sklearn

model=joblib.load('final_model.pkl')

@st.cache()

def prediction(Hours_studied, Previous_Scores, Extracurricular_Activities,Sleep_Hours,
                Sample_Question_Papers_Practiced):
    
    if Extracurricular_Activities=='No':
        Extracurricular_Activities=0
    else:
        Extracurricular_Activities=1

    prediction = model.predict([[Hours_studied, Previous_Scores, Extracurricular_Activities,Sleep_Hours,
                Sample_Question_Papers_Practiced]])
    
    return prediction


def main():
    st.title("Student Performance Prediction")

    st.write("#### We need some information to predict the performance of the Student")

    Extracurricular_Activities = {'Yes','No'}

    Hours_studied = st.text_input('Hours of study')
    Previous_Scores = st.slider('Previous Score', 0,100,3)
    Extracurricular_Activities = st.selectbox('Extra curricular activities', Extracurricular_Activities)
    Sleep_Hours = st.text_input('sleep Hours')
    Sample_Question_Papers_Practiced = st.text_input('Sample_question_practiced')



    if st.button('Predict'):
        result=prediction(Hours_studied,Previous_Scores, Extracurricular_Activities,Sleep_Hours,Sample_Question_Papers_Practiced)
        st.success(f"Your performance score is {result[0]:.0f}")

if __name__=='__main__':
    main()