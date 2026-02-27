import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import google.generativeai as genai

# 🔐 Configure Gemini API key securely from Streamlit secrets
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit page setup
st.set_page_config(page_title="AI Company Data Chatbot", layout="wide")

st.title("🤖 AI Company Data Chatbot (Powered by Gemini)")
st.write("Upload a dataset and ask any business-related question.")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📂 Dataset Preview")
    st.dataframe(df)

    # User question input
    question = st.text_input("Ask your question:")

    if question:
        # Build prompt safely
        prompt = f"""
        You are a data analyst.
        Here is a preview of the dataset (first 20 rows):

        {df.head(20).to_string()}

        Columns: {list(df.columns)}

        User question: {question}

        Answer clearly in simple business language.
        If calculation is needed, explain the result.
        """

        try:
            # Pass prompt as a list to avoid InvalidArgument errors
            response = model.generate_content([prompt])
            st.subheader("📊 AI Response")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error generating response: {e}")
