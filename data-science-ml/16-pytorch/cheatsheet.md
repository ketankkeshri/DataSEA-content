```markdown
# Deep Learning with PyTorch — Cheatsheet

## [Core Concepts]

| Thing              | Syntax                                       | Notes                                              |
|--------------------|----------------------------------------------|----------------------------------------------------|
| Tensor Creation     | `torch.tensor(data)`                         | Create a tensor from data.                         |
| Random Tensor       | `torch.rand(size)`                           | Create a tensor with random values.                |
| Tensor Shape        | `tensor.shape`                               | Get the shape of a tensor.                         |
| Reshape Tensor      | `tensor.view(new_shape)`                     | Change the shape of a tensor without changing data.|
| Autograd            | `tensor.requires_grad_()`                    | Track operations for gradients.                    |
| Gradient Calculation| `tensor.backward()`                          | Compute gradients.                                  |
| Zero Gradients      | `optimizer.zero_grad()`                      | Clear gradients before the next step.              |

## [Modules and Layers]

| Layer Type          | Syntax                                       | Notes                                              |
|---------------------|----------------------------------------------|----------------------------------------------------|
| Linear Layer        | `torch.nn.Linear(in_features, out_features)`| Fully connected layer.                             |
| Activation           | `torch.nn.ReLU()`                           | Rectified Linear Unit activation.                  |
| Loss Function       | `torch.nn.CrossEntropyLoss()`               | Used for multi-class classification tasks.        |

## [Training Loop]

```python
for epoch in range(num_epochs):
    model.train()  # Set model to training mode
    for inputs, labels in dataloader:
        optimizer.zero_grad()  # Zero gradients
        outputs = model(inputs)  # Forward pass
        loss = criterion(outputs, labels)  # Compute loss
        loss.backward()  # Backward pass
        optimizer.step()  # Update weights
```

## [Datasets and Loaders]

| Function            | Syntax                                       | Notes                                              |
|---------------------|----------------------------------------------|----------------------------------------------------|
| Dataset Class       | `class CustomDataset(torch.utils.data.Dataset):` | Custom dataset handling.                          |
| Get Item            | `def __getitem__(self, index):`            | Return data sample and label.                     |
| DataLoader          | `DataLoader(dataset, batch_size=32, shuffle=True)` | Loads data in batches.                         |

## [GPU Essentials]

| Command             | Syntax                                       | Notes                                              |
|---------------------|----------------------------------------------|----------------------------------------------------|
| Check GPU           | `torch.cuda.is_available()`                  | Check if CUDA is available.                        |
| Move Tensor to GPU  | `tensor.to('cuda')`                          | Transfer tensor to GPU.                           |
| Move Model to GPU   | `model.to('cuda')`                           | Transfer model to GPU.                            |

## [Gotchas]

- ⚠️ Ensure tensor types match (e.g., float vs. int) when performing operations.
- ⚠️ Don't forget to call `model.train()` before training and `model.eval()` for validation/testing.
- ⚠️ If you're using a custom dataset, ensure `__len__` is implemented.

## [Mental Model]

- **Tensors:** Basic building blocks for neural networks.
- **Layers:** Combine tensors to create models.
- **Training Loop:** Sequentially updates weights based on loss computed from predictions.
```