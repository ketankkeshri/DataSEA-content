```markdown
# Model Evaluation Metrics — Cheatsheet

## Classification Metrics

| Metric          | Formula / Value                   | Notes                                        |
|-----------------|-----------------------------------|----------------------------------------------|
| Accuracy        | `(TP + TN) / (TP + TN + FP + FN)`| Overall correctness of the model            |
| Precision       | `TP / (TP + FP)`                  | True positives among predicted positives      |
| Recall          | `TP / (TP + FN)`                  | True positives among actual positives         |
| F1 Score        | `2 * (Precision * Recall) / (Precision + Recall)` | Harmonic mean of precision and recall |
| ROC AUC         | Area under ROC curve              | Measures the ability to distinguish classes   |
| Confusion Matrix|                                 | Visual representation of TP, TN, FP, FN      |

## Regression Metrics

| Metric          | Formula / Value                   | Notes                                        |
|-----------------|-----------------------------------|----------------------------------------------|
| Mean Absolute Error (MAE) | `mean(|y_true - y_pred|)` | Average absolute error between predictions and actuals |
| Mean Squared Error (MSE)  | `mean((y_true - y_pred)^2)` | Average squared error; sensitive to outliers |
| Root Mean Squared Error (RMSE) | `sqrt(MSE)`             | Error in the same units as the target variable |
| R-squared (R²)  | `1 - (SS_res / SS_tot)`          | Proportion of variance explained by the model |

## Ranking Metrics

| Metric          | Formula / Value                   | Notes                                        |
|-----------------|-----------------------------------|----------------------------------------------|
| Mean Average Precision (MAP) | Average of precision at each relevant item | Measures precision for ranked items |
| Normalized Discounted Cumulative Gain (NDCG) | `DCG / IDCG` | Evaluates ranking quality, considers position relevance |

## Calibration

| Metric          | Purpose                             | Notes                                        |
|-----------------|------------------------------------|----------------------------------------------|
| Brier Score     | Measures accuracy of probabilistic predictions | Lower is better; ranges from 0 to 1 |
| Calibration Plot| Graphical representation of predicted vs actual probabilities | Shows how well predicted probabilities match actual outcomes |

## Gotchas

- ⚠️ Precision and Recall can be misleading if classes are imbalanced; consider using F1 Score or ROC AUC.
- ⚠️ R² can be overly optimistic in non-linear models; check residual plots for model fit.

## Mental model

- **Classification**: Focus on True Positives, False Positives, and their ratios (Precision and Recall).
- **Regression**: Look at the average errors (MAE, MSE) to understand prediction accuracy.
- **Ranking**: Assess how well your model ranks items based on relevance (NDCG, MAP).
```