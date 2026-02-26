import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Company Data Chatbot", layout="wide")

st.title("📊 AI Company Data Chatbot")
st.write("Ask questions about your company sales data.")

uploaded_file = st.file_uploader("Upload your Company CSV File", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df.columns = df.columns.str.strip()

    st.subheader("Dataset Preview")
    st.dataframe(df)

    question = st.text_input("Ask your question:")

    if question:
        question = question.lower()

        if "total" in question and "sales" in question:
            total = df["Sales"].sum()
            st.success(f"💰 Total Sales: {total}")

        elif "average" in question and "sales" in question:
            avg = df["Sales"].mean()
            st.success(f"📈 Average Sales: {avg}")

        elif "top" in question:
            top_products = df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(5)

            st.subheader("🏆 Top 5 Products")
            st.write(top_products)

            fig, ax = plt.subplots()
            top_products.plot(kind="bar", ax=ax)
            plt.xticks(rotation=45)
            st.pyplot(fig)

        elif "region" in question:
            region_sales = df.groupby("Region")["Sales"].sum()

            st.subheader("🌍 Sales by Region")
            st.write(region_sales)

            fig, ax = plt.subplots()
            region_sales.plot(kind="bar", ax=ax)
            plt.xticks(rotation=45)
            st.pyplot(fig)

        else:
            st.warning("❌ I don't understand that question yet. Try asking about total, average, top products, or region sales.")