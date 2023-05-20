import streamlit as st

uploaded_file = None

def main():
    st.title("Monica's BMI Prediction App")
    st.text("Welcome to Monica's BMI Prediction Application. It's simple to use!")
    st.text("Just upload a picture of your face and my model will predict your BMI.")
    
    if 'is_file_uploaded' not in st.session_state or not st.session_state.is_file_uploaded:
        uploaded_file = st.file_uploader("Upload your image here...", type=['png', 'jpeg', 'jpg'])
        
    if uploaded_file is not None:
        st.image(uploaded_file)
        st.session_state.is_file_uploaded = 1
  

if __name__ == "__main__":
  main()
