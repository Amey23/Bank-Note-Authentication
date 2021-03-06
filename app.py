import numpy as np
import pickle
import pandas as pd
import streamlit as st 

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

def predict_note_authentication(variance,skewness,curtosis,entropy):
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction

def main():
    st.title("Streamlit Bank Authenticator ML App ")
    
    #st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("Variance")
    skewness = st.text_input("skewness")
    curtosis = st.text_input("curtosis")
    entropy = st.text_input("entropy")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(variance,skewness,curtosis,entropy)
    st.success('The output is {}'.format(result))

if __name__=='__main__':
    main()
    
    
    
