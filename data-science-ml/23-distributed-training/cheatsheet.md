```markdown
# Distributed Training — Cheatsheet

## [Core Concepts]

| Concept         | Description                                                  |
|-----------------|--------------------------------------------------------------|
| Data-Parallel   | Splits data across multiple devices, each training a copy of the model. |
| Model-Parallel  | Splits the model across multiple devices, each handling a part of the model. |
| DeepSpeed       | A library that enables efficient training of large models with reduced memory footprint. |
| Fully Sharded Data Parallel (FSDP) | Distributes both model and optimizer states across devices, optimizing memory usage. |

## [Data-Parallel Training]

```python
import torch
import torchvision.models as models
from torch.nn import DataParallel

model = models.resnet50()
model = DataParallel(model)  # Wrap the model for data-parallel training
```

## [Model-Parallel Training]

```python
import torch
import torchvision.models as models

model = models.resnet50()
# Move different layers to different devices
model.layer1.to('cuda:0')
model.layer2.to('cuda:1')
```

## [DeepSpeed Example]

```python
import deepspeed

model = models.resnet50()
model_engine, optimizer, _, _ = deepspeed.initialize(model=model, 
                                                      model_parameters=model.parameters())
```

## [FSDP Example]

```python
from torch.distributed.fsdp import FullyShardedDataParallel as FSDP

model = models.resnet50()
fsdp_model = FSDP(model)  # Wrap the model for FSDP
```

## [Gotchas]

- ⚠️ Ensure consistent batch sizes across devices for data-parallel training.
- ⚠️ Monitor GPU memory usage to avoid out-of-memory errors with model-parallel training.
- ⚠️ DeepSpeed may require specific configurations; check compatibility with your model.
- ⚠️ FSDP can introduce overhead; benchmark performance against standard training.

## [Mental model]

- **Data-Parallel:** Think of each GPU as an identical worker processing chunks of data.
- **Model-Parallel:** Each GPU specializes in a different part of a complex model.
- **DeepSpeed & FSDP:** Tools to streamline and optimize training for massive models.
```