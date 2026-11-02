# 🏥 Medical Insurance Cost Prediction

An end-to-end Data Science project predicting individual medical insurance costs based on demographic and lifestyle features using **Linear Regression** and an interactive **Streamlit** web application.

---

## 📊 Dataset Overview

The dataset contains **1,338 records** of beneficiary health profile metrics:

| Column | Data Type | Description |
| :--- | :--- | :--- |
| **age** | Numerical | Primary beneficiary age (18 to 64 years) |
| **sex** | Categorical | Insurance contractor gender (`male`, `female`) |
| **bmi** | Numerical | Body mass index ($kg/m^2$) |
| **children** | Numerical | Number of children covered by health insurance |
| **smoker** | Categorical | Smoking status (`yes`, `no`) |
| **region** | Categorical | Residential area in the US |
| **charges** | Numerical | Individual medical costs billed by health insurance |

---

## 💡 Key Data Insights

* **Smoking Impact:** Smoking is the strongest single factor influencing medical charges.
  * **Smokers Mean Charges:** ~$32,050
  * **Non-Smokers Mean Charges:** ~$8,434
* **BMI Interaction:** High BMI significantly exacerbates medical costs for smokers compared to non-smokers.

---

## ⚙️ Machine Learning Model Performance

Model trained using **Linear Regression** (80/20 train-test split):

| Metric | Value |
| :--- | :--- |
| **$R^2$ Score** | **0.7811** (78.1% variance explained) |
| **Mean Absolute Error (MAE)** | **$4,213.48** |
| **Root Mean Squared Error (RMSE)** | **$5,829.17** |

---

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/medical-cost-prediction.git](https://github.com/YOUR_USERNAME/medical-cost-prediction.git)
cd medical-cost-prediction