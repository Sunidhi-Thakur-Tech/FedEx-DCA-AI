# FedEx DCA Recovery Prioritization System

## 📌 Problem Statement
FedEx manages thousands of overdue customer accounts through external Debt Collection Agencies (DCAs).  
The current process relies heavily on spreadsheets and manual follow-ups, leading to delayed recoveries, limited visibility, and weak accountability.

This project aims to build a **digital and AI-driven system** to intelligently prioritize overdue accounts based on recovery probability and business risk.

---

## 🎯 Objective
- Predict the likelihood of recovery for overdue accounts
- Automatically classify cases into **High / Medium / Low priority**
- Enable faster decision-making for DCA operations
- Provide a simple, interactive UI for demonstration

---

## 🧠 Solution Overview
We built an **end-to-end AI-powered prioritization system** that:
- Uses a Machine Learning model to predict recovery probability
- Applies business logic to assign priority levels
- Provides a Streamlit-based UI for real-time analysis

---

## 📊 Dataset
- **Type:** Synthetic (dummy) dataset created for hackathon use
- **Reason:** Real FedEx data is confidential
- **Size:** ~500 records (training), multiple CSVs for testing

### Features Used:
- `amount_due`
- `ageing_days`
- `past_payment_history`
- `contact_attempts`
- `customer_risk_score`

### Target:
- `recovered` (1 = recovered, 0 = not recovered)

---

## 🤖 Machine Learning Model
- **Algorithm:** Logistic Regression
- **Why Logistic Regression?**
  - Interpretable
  - Business-friendly
  - Suitable for probability-based decisions

### Model Enhancements:
- Feature scaling using `StandardScaler`
- Class balancing to handle recovery imbalance
- Implemented using a Scikit-learn Pipeline

### Performance:
- Accuracy: ~81–82%
- Balanced precision and recall
- Stable across low-risk, high-risk, mixed, and edge cases

---

## 🚦 Priority Logic
Priority is assigned using recovery probability and ageing:

- **High Priority:** Low recovery probability and high ageing
- **Medium Priority:** Moderate recovery probability
- **Low Priority:** High recovery probability

This ensures DCAs focus first on accounts needing urgent action.

---

## 🖥️ User Interface
- Built using **Streamlit**
- Upload CSV files
- View recovery probability and priority for each account
- Summary of High / Medium / Low priority cases

---

## 📁 Project Structure
```

FedEx-DCA-AI/
│
├── app.py
├── recovery_model_pipeline.pkl
├── dca_recovery_dataset.csv
├── requirements.txt
└── README.md

````

---

## ▶️ How to Run the Project
1. Create and activate virtual environment
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run Streamlit app:

   ```bash
   streamlit run app.py
   ```

---

## 🏆 Key Outcomes

* Reduced ambiguity in DCA prioritization
* Faster escalation of high-risk cases
* Explainable and scalable AI solution
* Hackathon-ready proof of concept

---

## 🔮 Future Scope

* Integration with live FedEx systems
* DCA performance scoring
* SLA monitoring and alerts
* GenAI-powered negotiation assistants
* Deployment on cloud platforms