import firebase_admin
from firebase_admin import credentials, auth
import streamlit as st
from apps import login

# Initialize Firebase Admin SDK if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate(r"C:\Users\hp\Downloads\serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

def app():
    st.title("Sign Up")

    # Input fields
    email = st.text_input("📧 Email", key="3")
    password = st.text_input("🔑 Password", type="password", key="4")
    confirm_password = st.text_input("🔒 Confirm Password", type="password", key="5")

    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])  # Adjust column ratios as needed

    with col1:
        if st.button("Create Account"):
            if password != confirm_password:
                st.error("❌ Passwords do not match.")
            else:
                try:
                    # Create user in Firebase
                    user = auth.create_user(email=email, password=password)
                    st.success(f"✅ Account created successfully! User ID: {user.uid}")
                        
                except Exception as e:
                    st.error(f"Error creating account: {e}")

    with col2:
        pass

    with col3:
        pass

    with col4:
        if st.button("Go to Login", icon="🔙"):
            st.session_state.current_page = "login"
            login.app()
            st.rerun()