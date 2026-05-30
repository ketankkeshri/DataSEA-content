```markdown
# Transformer Architectures — Cheatsheet

## [Attention Mechanism]

| Thing                | Syntax                          | Notes                                      |
|---------------------|---------------------------------|--------------------------------------------|
| Scaled Dot-Product   | `Attention(Q, K, V) = softmax(QK^T / √d_k)V` | Computes attention scores using queries (Q), keys (K), and values (V). |
| Multi-Head Attention | `MultiHead(Q, K, V) = concat(head_1, ..., head_h)W_o` | Combines multiple attention heads for richer representation. |

## [Encoder-Decoder Architecture]

| Component           | Syntax                          | Notes                                      |
|---------------------|---------------------------------|--------------------------------------------|
| Encoder             | `Encoder(x) = LayerNorm(FFN(SelfAttention(x)))` | Processes input data through self-attention and feed-forward networks. |
| Decoder             | `Decoder(y, context) = LayerNorm(FFN(SelfAttention(y), context))` | Uses previous outputs and encoder output context for generating sequences. |

## [Positional Encoding]

```python
import numpy as np

def positional_encoding(seq_len, d_model):
    pos = np.arange(seq_len)[:, np.newaxis]
    div_term = np.exp(np.arange(0, d_model, 2) * -(np.log(10000.0) / d_model))
    pe = np.zeros((seq_len, d_model))
    pe[:, 0::2] = np.sin(pos * div_term)
    pe[:, 1::2] = np.cos(pos * div_term)
    return pe
```

## [Scaling Laws]

| Law                        | Description                                    |
|----------------------------|------------------------------------------------|
| Data Scaling               | More data generally leads to better performance. |
| Model Scaling              | Larger models (more parameters) tend to perform better. |
| Training Time Scaling      | Longer training times yield better results, but with diminishing returns. |

## [Gotchas]

- ⚠️ Ensure properly adjusted learning rate when scaling models; too high can destabilize training.
- ⚠️ Be cautious with attention heads; too many can lead to overfitting and increased compute costs.

## [Mental model]

- **Attention** helps the model focus on relevant parts of the input.
- **Encoder-Decoder** structure separates input processing from output generation.
- **Positional Encoding** adds information about token positions, crucial for sequence tasks.
```