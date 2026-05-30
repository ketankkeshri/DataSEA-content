```markdown
# LLM Fine-tuning — Cheatsheet

## [Core Concepts]

| Thing       | Syntax                          | Notes                                           |
|-------------|---------------------------------|-------------------------------------------------|
| Fine-tuning | `model.fine_tune(data)`        | Adjust pre-trained models on specific datasets. |
| LoRA        | `apply_lora(model, params)`     | Low-Rank Adaptation for efficient fine-tuning.  |
| QLoRA       | `apply_qlora(model, params)`    | Quantized LoRA for reduced memory footprint.    |

## [Key Functions]

```python
# Fine-tuning a model with LoRA
from transformers import AutoModel

model = AutoModel.from_pretrained('model_name')
fine_tuned_model = model.fine_tune(training_data, lora=True)

# Evaluating model performance
results = evaluate_model(fine_tuned_model, test_data)
print(results)
```

## [Datasets]

| Dataset Type | Usage                              | Notes                                          |
|--------------|------------------------------------|------------------------------------------------|
| Training     | `train_dataset = load_data('train')` | Data used to fine-tune the model.              |
| Validation   | `val_dataset = load_data('val')`   | Used to tune hyperparameters and avoid overfitting. |
| Test         | `test_dataset = load_data('test')` | Final evaluation to assess model performance.   |

## [Evaluation Metrics]

| Metric        | Function                          | Notes                                          |
|---------------|-----------------------------------|------------------------------------------------|
| Accuracy      | `accuracy_score(y_true, y_pred)` | Measures the proportion of correct predictions. |
| F1 Score      | `f1_score(y_true, y_pred)`       | Balances precision and recall.                  |
| Loss          | `loss_fn(y_true, y_pred)`        | Quantifies how well the model is performing.    |

## [Gotchas]

- ⚠️ Ensure your dataset is balanced to avoid biased models.
- ⚠️ Monitor overfitting: use validation datasets to tune hyperparameters.
- ⚠️ Large models require substantial memory; consider quantization techniques.

## [Mental model]

- Fine-tuning adjusts model weights based on new data.
- LoRA and QLoRA optimize this process for efficiency.
- Always validate with unseen data to ensure generalization.

```