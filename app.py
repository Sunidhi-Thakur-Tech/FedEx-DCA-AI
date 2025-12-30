import streamlit as st
import pandas as pd
import joblib

# Page config
st.set_page_config(page_title="FedEx DCA Recovery System", layout="wide")

st.title("📦 FedEx DCA Recovery Prioritization System")
st.write("Upload overdue account data to predict recovery probability and priority.")

# Load trained model
model = joblib.load("recovery_model_pipeline.pkl")

# Priority logic
def assign_priority(prob, ageing):
    if prob < 0.4 and ageing > 60:
        return "High"
    elif prob < 0.7:
        return "Medium"
    else:
        return "Low"

# File uploader
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Uploaded Data")
    st.dataframe(df.head())

    # Predict recovery probability
    probs = model.predict_proba(df)[:, 1]

    df["recovery_probability"] = probs
    df["priority"] = df.apply(
        lambda row: assign_priority(row["recovery_probability"], row["ageing_days"]),
        axis=1
    )

    st.subheader("📊 Prediction Results")
    st.dataframe(df)

    # Summary metrics
    st.subheader("📈 Summary")
    col1, col2, col3 = st.columns(3)

    col1.metric("High Priority Cases", (df["priority"] == "High").sum())
    col2.metric("Medium Priority Cases", (df["priority"] == "Medium").sum())
    col3.metric("Low Priority Cases", (df["priority"] == "Low").sum())

else:
    st.info("Please upload a CSV file to get predictions.")

# venv\Scripts\activate
# streamlit run app.py