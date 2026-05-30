```markdown
# RAG Pipelines — Cheatsheet

## [Section 1: Core concepts]

| Concept       | Description                                             | Notes                                   |
|---------------|---------------------------------------------------------|-----------------------------------------|
| RAG           | Retrieval-Augmented Generation combines retrieval with generation. | Enhances model responses with precise data. |
| Chunking      | Process of breaking down documents into smaller pieces. | Improves retrieval efficiency.          |
| Embeddings    | Vector representations of data points for similarity comparisons. | Choose wisely based on task.           |
| Hybrid Search | Combines traditional search and semantic search methods. | Leverages strengths of both approaches. |
| Reranking     | Adjusting result order based on relevance feedback.    | Fine-tunes results after initial retrieval. |
| Evaluation    | Assessing performance of the RAG pipeline.             | Use metrics like precision, recall, F1. |

## [Common operations]

```python
# Example of chunking text
from nltk import sent_tokenize, word_tokenize

def chunk_text(text):
    sentences = sent_tokenize(text)
    return [word_tokenize(sentence) for sentence in sentences]

# Embedding choices using Hugging Face Transformers
from transformers import AutoTokenizer, AutoModel
import torch

model_name = "sentence-transformers/all-MiniLM-L6-v2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

def get_embeddings(text):
    inputs = tokenizer(text, return_tensors='pt')
    with torch.no_grad():
        embeddings = model(**inputs).last_hidden_state
    return embeddings

# Example of a reranking function
def rerank_results(results, feedback):
    # Simple rerank example based on feedback scores
    return sorted(results, key=lambda x: feedback[x['id']], reverse=True)
```

## [Gotchas]

- ⚠️ Ensure chunk sizes are optimal; too small may lose context, too large may slow retrieval.
- ⚠️ Embedding choices can significantly impact performance; experiment with different models.
- ⚠️ Reranking strategies need to be tailored to specific data sets for best results.

## [Mental model]

- RAG Pipeline:
  - **Input:** Raw text or query
  - **Process:**
    - Chunking → Embedding → Retrieval → Reranking
  - **Output:** Augmented response
```