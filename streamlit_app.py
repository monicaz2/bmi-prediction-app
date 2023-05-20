import streamlit as st

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
