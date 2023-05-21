import streamlit as st
import tensorflow.keras as keras

from tensorflow.keras.models import model_from_json

model_file_path = 'model.json'
model_weights_file_path = 'model.h5'

@st.cache_resource
def load_model():
    with open('model.json', 'r') as f:
        loaded_model_json = f.read()
        loaded_model = model_from_json(loaded_model_json)
        return loaded_model.load_weights(model_weights_file_path)

def main():
    st.title("Monica's BMI Prediction App")
    st.text("Welcome to Monica's BMI Prediction Application. It's simple to use!")
    st.text("Just upload a picture of your face and my model will predict your BMI.")
    
    uploaded_file = st.file_uploader("Upload your image here...", type=['png', 'jpeg', 'jpg'])
    
    if uploaded_file is not None:
        st.text("Input image: ")
        st.image(uploaded_file)
  

if __name__ == "__main__":
  main()
