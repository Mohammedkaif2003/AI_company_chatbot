import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import google.generativeai as genai

# 🔐 Add your Gemini API key here
genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="AI Company Data Chatbot", layout="wide")

st.title("🤖 AI Company Data Chatbot (Powered by Gemini)")
st.write("Ask any question about your company dataset.")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Dataset Preview")
    st.dataframe(df)

    question = st.text_input("Ask your question:")

    if question:
        prompt = f"""
        You are a data analyst.
        Here is the dataset:

        {df.head(20).to_string()}

        Columns: {list(df.columns)}

        User question: {question}

        Answer clearly in simple business language.
        If calculation is needed, explain the result.
        """

        response = model.generate_content(prompt)

        st.subheader("📊 AI Response")
        st.write(response.text)
