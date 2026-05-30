```markdown
# Model Quantization — Cheatsheet

## [Core Concepts]

| Thing             | Description                                                        | Notes                          |
|-------------------|--------------------------------------------------------------------|--------------------------------|
| Model Quantization| Reducing model size and improving inference speed without loss of accuracy. | Key for deploying models on edge devices. |
| INT8 vs INT4      | INT8 uses 8 bits per weight, INT4 uses 4 bits, resulting in smaller models. | INT4 can cause more accuracy loss. |
| GGUF              | Generalized Gated Unfolding Framework for efficient model storage. | Optimizes for both speed and memory. |
| Hardware Considerations | Consider the target hardware's ability to utilize quantized models. | Check compatibility with CPUs, GPUs, and TPUs. |

## [Common Operations]

```python
import torch

# Example: Quantizing a PyTorch model
model = ...  # Your pre-trained model

# Convert to quantized model
model.qconfig = torch.quantization.get_default_qconfig('fbgemm')
torch.quantization.prepare(model, inplace=True)
# Calibrate with representative data
# e.g., model(input_data)

# Convert to quantized model
torch.quantization.convert(model, inplace=True)

# Save the quantized model
torch.save(model.state_dict(), 'quantized_model.pth')
```

## [Gotchas]

- ⚠️ INT4 quantization may lead to significant accuracy degradation, especially in complex models. Test thoroughly!
- ⚠️ Not all hardware supports INT4 operations. Always check the target device's specifications before deploying.

## [Mental model]

- **Quantization Process:**
  - **Input Model** ➔ **Calibration** ➔ **Quantized Model**
- **Bit-width Trade-off:**
  - Higher bits (e.g., INT8) = Better accuracy
  - Lower bits (e.g., INT4) = Smaller size, faster inference, potential accuracy loss
- **Hardware Compatibility:**
  - Ensure model compatibility with CPU, GPU, or TPU for optimal performance.
```