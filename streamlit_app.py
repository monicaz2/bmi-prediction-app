import streamlit as st

def main():
    st.title("Monica's BMI Prediction App")
    st.text("Welcome to Monica's BMI Prediction Application. It's simple to use!")
    st.text("Just upload a picture of your face and my model will predict your BMI.")
    
    if 'uploaded_file' not in st.session_state or not st.session_state.uploaded_file:
        st.session_state.uploaded_file = st.file_uploader("Upload your image here...", type=['png', 'jpeg', 'jpg'])
        print(st.session_state.uploaded_file)
    
    if 'uploaded_file' in st.session_state and st.session_state.uploaded_file:
        st.text("Input Image: ")
        st.image(st.session_state.uploaded_file)
  

if __name__ == "__main__":
  main()
