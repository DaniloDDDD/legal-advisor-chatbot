import streamlit as st
import requests
import uuid

API_URL = "http://localhost:8001/chat"
st.title("Legal Advisor Chatbot")

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

user_input = st.text_input("Ask a legal question:")

if st.button("Submit"):
    if not user_input.strip():
        st.warning("Please enter a legal question before submitting.")
    else:
        try:
            response = requests.post(
                API_URL,
                json={"question": user_input, "session_id": st.session_state.session_id},
                timeout = 10
            )

            if response.status_code == 200:
                data = response.json()
                st.write("**AI Response:**", data.get("answer", "No answer received."))
            else:
                st.error(f"Error fetching response: {response.status_code}")
        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")