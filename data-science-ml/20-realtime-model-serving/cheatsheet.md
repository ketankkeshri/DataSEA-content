```markdown
# Real-time Model Serving — Cheatsheet

## [Core Concepts]

| Concept                  | Description                                             |
|-------------------------|---------------------------------------------------------|
| Real-time Serving       | Deploying models to make predictions on live data inputs. |
| Batching                | Grouping multiple requests for efficiency and throughput.  |
| GPU Optimization        | Techniques to leverage GPU resources for faster inference.  |
| VLLM-TGI                | Using Very Large Language Models with TensorFlow for inference. |

## [Core Syntax]

| Operation               | Syntax                                | Notes                                       |
|------------------------|---------------------------------------|---------------------------------------------|
| Load Model             | `model = load_model('model_path')`   | Load a pre-trained model for inference.    |
| Predict                | `predictions = model.predict(data)`  | Run predictions on input data.             |
| Batch Requests         | `batch_predictions = model.predict(batch)` | Use a batch of data for predictions.      |
| Optimize GPU           | `tf.config.experimental.set_memory_growth(gpu_device, True)` | Allows dynamic memory allocation on GPUs. |

## [Common Operations]

```python
import tensorflow as tf

# Load a model
model = tf.keras.models.load_model('path/to/model')

# Real-time inference example
def real_time_inference(data):
    predictions = model.predict(data)
    return predictions

# Batch processing
def batch_inference(batch_data):
    return model.predict(batch_data)

# GPU optimization
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
    except RuntimeError as e:
        print(e)

# Example of VLLM-TGI usage
from vllm import VLLM
vllm_model = VLLM(model_name="large_model_name")
vllm_predictions = vllm_model.predict("input text")
```

## [Gotchas]

- ⚠️ Always check GPU memory usage to avoid OOM errors.
- ⚠️ Batch sizes that are too large can lead to increased latency.
- ⚠️ Ensure input data types match the model's expected input shape.

## [Mental Model]

- Real-time inference is about speed and efficiency.
- Batching increases throughput but may add latency.
- Optimizing GPU usage is crucial for handling large models and datasets.
```