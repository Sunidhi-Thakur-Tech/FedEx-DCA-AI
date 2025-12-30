---
# FedEx DCA Recovery Prioritization System 🚚📊

An AI-powered proof-of-concept to intelligently prioritize overdue customer accounts handled by Debt Collection Agencies (DCAs).

---

## 📌 Problem Statement
FedEx manages a large number of overdue customer accounts through external Debt Collection Agencies.  
The existing process is highly manual, relying on spreadsheets and emails, which leads to:
- Delayed recoveries  
- Poor visibility into case status  
- Weak accountability and governance  

---

## 🎯 Objective
- Predict the likelihood of recovery for overdue accounts  
- Automatically classify cases into **High / Medium / Low priority**  
- Help DCA teams focus on the most critical cases first  
- Demonstrate a scalable, AI-driven approach through a working prototype  

---

## 🧠 Solution Overview
We built an **end-to-end AI-based prioritization system** that:
- Uses Machine Learning to predict recovery probability  
- Applies business rules to assign priority levels  
- Provides a simple Streamlit-based UI for demonstration  

---

## 📊 Dataset

* **Type:** Synthetic (dummy) dataset created for hackathon use
* **Reason:** Real FedEx data is confidential
* **Training Size:** ~500 records
* **Testing:** Multiple scenario-based CSV files (low-risk, high-risk, mixed, edge cases)

### Features Used

* `amount_due` – Outstanding amount
* `ageing_days` – Days overdue
* `past_payment_history` – Previous payment behavior (0/1)
* `contact_attempts` – Number of follow-ups
* `customer_risk_score` – Customer risk level (1–3)

### Target Variable

* `recovered` (1 = recovered, 0 = not recovered)

---

## 🤖 Machine Learning Model

* **Algorithm:** Logistic Regression
* **Implementation:** Scikit-learn Pipeline

### Why Logistic Regression?

* Highly interpretable
* Business-friendly
* Outputs recovery **probability**, not just yes/no

### Enhancements

* Feature scaling using `StandardScaler`
* Class balancing to handle recovery imbalance

### Performance

* Accuracy: ~81–82%
* Stable precision and recall
* Consistent behavior across all test scenarios

---

## 🚦 Priority Logic

Cases are prioritized using recovery probability and ageing:

* **High Priority:**
  Low recovery probability + high ageing

* **Medium Priority:**
  Moderate recovery probability

* **Low Priority:**
  High recovery probability

This ensures DCAs act first on accounts needing urgent attention.

---

## 🖥️ User Interface (Streamlit)

* Upload CSV files
* View recovery probability per account
* Automatic priority classification
* Summary of High / Medium / Low priority cases

### UI Preview (GIF)

![Demo GIF](assets/demo.gif)

---

## 🔄 End-to-End Workflow

```text
Upload CSV
   ↓
ML Model predicts recovery probability
   ↓
Business logic assigns priority
   ↓
Results displayed in UI
   ↓
DCA teams take action
```

---

## 📁 Project Structure

```
FedEx-DCA-AI/
│
├── app.py
├── recovery_model_pipeline.pkl
├── dca_recovery_dataset.csv
├── test_low_risk.csv
├── test_high_risk.csv
├── test_mixed_cases.csv
├── test_edge_cases.csv
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
```

---

## 🏆 Key Outcomes

* Clear prioritization of overdue accounts
* Faster escalation of high-risk cases
* Reduced manual effort
* Explainable and scalable AI solution

---

## 🔮 Future Scope

* Integration with real-time FedEx systems
* DCA performance scoring dashboards
* SLA tracking and automated alerts
* GenAI-powered negotiation assistants
* Cloud deployment for enterprise scale

---

## 📌 Conclusion

This project demonstrates how **AI-driven recovery prioritization** can significantly improve debt collection efficiency while maintaining transparency, explainability, and business relevance.

---