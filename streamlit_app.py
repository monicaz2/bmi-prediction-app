import io
import numpy as np
import streamlit as st
import tensorflow.keras as keras
import time

from PIL import Image
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing import image

model_file_path = 'model.json'
model_weights_file_path = 'model.h5'

@st.cache_resource
def load_model():
    with open('model.json', 'r') as f:
        loaded_model_json = f.read()
        loaded_model = model_from_json(loaded_model_json)
        return loaded_model.load_weights(model_weights_file_path)
    
def get_PIL_instance(byteImage):
    bytes_io_image = io.BytesIO(byteImage)
    image = Image.open(bytes_io_image)
    return image.resize((224, 224))

def get_image_tensor(pil_instance_image):
    img_tensor = image.img_to_array(pil_instance_image)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor /= 255.
    return img_tensor

def main():
    st.title("Monica's BMI Prediction App")
    st.text("Welcome to Monica's BMI Prediction Application. It's simple to use!")
    st.text("Just upload a picture of your face and my model will predict your BMI.")
    
    uploaded_file = st.file_uploader("Upload your image here...", type=['png', 'jpeg', 'jpg'])
    
    if uploaded_file is not None:
        file = uploaded_file.read()
        pil_image = get_PIL_instance(file)
        tensor_image = get_image_tensor(pil_image)
        
        st.text("Input image: ")
        st.image(pil_image)
        
        with st.spinner("Prediction in Progress..."):
            time.sleep(3)
        st.success("Done")
  

if __name__ == "__main__":
  main()
