import streamlit as st

def is_file_uploaded_state_update(updated_value):
    st.session_state.is_file_uploaded = updated_value

def main():
    st.title("Monica's BMI Prediction App")
    st.text("Welcome to Monica's BMI Prediction Application. It's simple to use!")
    st.text("Just upload a picture of your face and my model will predict your BMI.")
    
    if 'is_file_uploaded' not in st.session_state or not st.session_state.is_file_uploaded:
        st.session_state.uploaded_file = st.file_uploader("Upload your image here...", type=['png', 'jpeg', 'jpg'], on_change=is_file_uploaded_state_update(1))
    else:
        st.text("Input Image: ")
        st.image(st.session_state.uploaded_file)
  

if __name__ == "__main__":
  main()
