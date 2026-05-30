# Eval

Evaluating the performance of fine-tuned models is crucial for ensuring their effectiveness in real-world applications. It helps you understand how well your model generalizes to unseen data and whether it's ready for deployment.

## Understanding Evaluation Metrics

Evaluation metrics provide insights into how well your fine-tuned model performs. Here are some common metrics used for different tasks:

- **Classification Tasks:**
  - **Accuracy:** The ratio of correctly predicted instances to the total instances.
  - **Precision:** The ratio of true positive predictions to the total predicted positives.
  - **Recall (Sensitivity):** The ratio of true positive predictions to the actual positives.
  - **F1 Score:** The harmonic mean of precision and recall, useful for imbalanced classes.

- **Regression Tasks:**
  - **Mean Absolute Error (MAE):** The average of absolute differences between predicted and actual values.
  - **Mean Squared Error (MSE):** The average of squared differences between predicted and actual values.
  - **R-squared:** A statistical measure that indicates how well the model explains the variability of the data.

### Implementing Evaluation in Code

Let’s see how to implement these metrics using Python with the popular library `scikit-learn`. Assume we have a fine-tuned model ready to make predictions on a validation dataset.

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, mean_absolute_error, mean_squared_error, r2_score

# Sample data
y_true_class = [1, 0, 1, 1, 0, 1, 0, 1]  # Ground truth
y_pred_class = [1, 0, 1, 0, 0, 1, 1, 0]  # Model predictions

# Classification metrics
accuracy = accuracy_score(y_true_class, y_pred_class)
precision = precision_score(y_true_class, y_pred_class)
recall = recall_score(y_true_class, y_pred_class)
f1 = f1_score(y_true_class, y_pred_class)

print("Classification Metrics:")
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1 Score: {f1:.2f}")

# Sample data for regression
y_true_reg = [3.0, -0.5, 2.0, 7.0]  # Ground truth
y_pred_reg = [2.5, 0.0, 2.0, 8.0]    # Model predictions

# Regression metrics
mae = mean_absolute_error(y_true_reg, y_pred_reg)
mse = mean_squared_error(y_true_reg, y_pred_reg)
r2 = r2_score(y_true_reg, y_pred_reg)

print("\nRegression Metrics:")
print(f"Mean Absolute Error: {mae:.2f}")
print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared: {r2:.2f}")
```

## Common pitfalls

- **Ignoring Class Imbalance:** In classification tasks, failing to account for class imbalance can yield misleading accuracy scores. Use precision, recall, and F1 scores instead.
- **Overfitting to Validation Data:** Constantly tuning your model based on validation performance can lead to overfitting. Keep a separate test set for final evaluation.
- **Neglecting Real-World Conditions:** Metrics may look good on the validation dataset but fail in production. Always test against realistic scenarios.

## In a nutshell

- Use appropriate evaluation metrics based on your task (classification vs. regression).
- Implement metrics using libraries like `scikit-learn` for quick insights.
- Watch out for common pitfalls to ensure your model performs well in the real world.