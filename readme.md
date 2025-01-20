# Fraud Detection Model

This project aims to detect fraudulent transactions using machine learning techniques, with a focus on handling imbalanced datasets and selecting relevant features. The model uses Random Forest and XGBoost classifiers to predict fraudulent transactions.

# Presentation

The presentation is in Docs For presenting folder

## Conclusion

- **Recall Prioritization:** In banking, it is more critical to detect all potential fraud cases (even if it means more false positives) than to miss actual fraud cases.
- **False Positive Impact:** False positives (classifying a legitimate transaction as fraudulent) inconvenience customers (e.g., blocked cards, extra verification). Customers prefer to prevent fraud, even if it means occasional inconveniences from false positives.
- **False Negative Impact:** False negatives (missing actual fraud) result in financial loss and damage to customer trust.

## Next Steps

- Adjustments to the threshold or model parameters may be necessary to refine the results.
- Benchmark more algorithms with different hyperparameters.
- Explore more possible features and better ways to balance and select the features.
- If possible, collect more data.
- Improve EDA (Exploratory Data Analysis).
- Data related to the devices used for transactions could be a valuable area for future exploration (Device Fingerprint).
- Explore seasonality in transaction dates.
- Consider a time-series model based approach.

## Model

### Data Splitting:
- Training Set: 70%
- Validation Set: 15%
- Test Set: 15%

### Data Normalization:
StandardScaler is applied to normalize the features.

### Model Selection:
- Random Forest and XGBoost are benchmarked to select the best model.
- Evaluate models using the ROC AUC metric.
- Select XGBoost as the final model based on the best ROC AUC score.

### Feature Selection:
- Random Forest to determine the importance of each feature.
- SelectFromModel is used to select features based on their importance scores.

### Balancing the Dataset:
SMOTE (Synthetic Minority Oversampling Technique) is applied to oversample the minority class (fraudulent transactions) in the training dataset.

## Requirements

To run the project, make sure to install the following dependencies:

```bash
pip install -U imbalanced-learn
pip install scikit-learn==1.5.0
pip install --upgrade xgboost

```
## API

Run inside the folder fraud_model_api the command: **python app.py**

Example of use:

```
curl -X POST http://localhost:5001/predict \
-H "Content-Type: application/json" \
-d '{
    "mc_tx_succ_count_last_365d": 202.0,
    "mc_tx_succ_count_lifetime": 0.0,
    "mc_weeks_signup": 189.7143,
    "mc_tx_succ_count_last_30d": 0.0,
    "mc_tx_amount_succ_sum_last_30d": 0.0,
    "mc_tx_amount_fail_sum_last_14d": 0.0,
    "mcc_sum_sq_succ_30d": 9.109,
    "mc_credit_transfer_out_br_count_pep_br_last_30d": 0.0,
    "decline_ext_rate_30d": 1.0,
    "mc_pur_br_count_last_1y": 20,
    "mc_billpay_br_count_sanction_last_30d": 12.2,
    "mc_credit_transfer_in_br_sum_last_180d": 2.4311,
    "mc_credit_transfer_out_br_count_sanction_last_30d": 15.0,
    "mc_tx_cp_count_decl_ext_last_24h": 0,
    "mc_credit_transfer_in_br_count_last_30d": 3.0,
    "mc_credit_transfer_in_rounded_amounts_br_sum_last_30d": 0.0,
    "mc_credit_transfer_in_br_sum_last_60d": 10,
    "mc_tx_amount_sum_last_24h": 20
}'
```
