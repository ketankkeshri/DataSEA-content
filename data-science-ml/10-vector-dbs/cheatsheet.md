```markdown
# Vector Databases — Cheatsheet

## [Core Concepts]

| Thing               | Syntax                          | Notes                                     |
|---------------------|---------------------------------|-------------------------------------------|
| Embedding Vector    | `vector = [0.1, 0.2, ...]`     | A numerical representation of data points. |
| Similarity Score    | `similarity_score(vec1, vec2)` | Measures how alike two vectors are.       |
| Distance Metric     | `euclidean_distance(vec1, vec2)`| Commonly used to measure distance.        |

## [Common Operations]

```python
# Create embeddings using OpenAI's API
import openai

response = openai.Embedding.create(
    input="Your text here",
    model="text-embedding-ada-002"
)
embedding = response['data'][0]['embedding']
```

```python
# Insert vectors into ChromaDB
from chromadb import Client

client = Client()
collection = client.create_collection("my_collection")
collection.add(embedding=[embedding], metadatas=[{"id": "1"}])
```

```python
# Querying with FAISS
import faiss
import numpy as np

index = faiss.IndexFlatL2(embedding_dimension)
index.add(np.array([embedding]).astype('float32'))
D, I = index.search(np.array([query_embedding]).astype('float32'), k=5)
```

```python
# Using Pinecone for vector storage
import pinecone

pinecone.init(api_key="YOUR_API_KEY", environment="us-west1-gcp")
index = pinecone.Index("my-index")
index.upsert([(id, embedding)])
```

## [Similarity Metrics]

| Metric            | Function                           | Notes                                      |
|-------------------|------------------------------------|--------------------------------------------|
| Euclidean         | `euclidean_distance(vec1, vec2)` | Straight-line distance in Euclidean space. |
| Cosine Similarity | `1 - spatial.distance.cosine(vec1, vec2)` | Measures angle between vectors.            |
| Dot Product       | `np.dot(vec1, vec2)`              | Measures similarity based on vector alignment. |

## [Gotchas]

- ⚠️ Ensure embeddings have the same dimensionality when comparing.
- ⚠️ Different distance metrics can yield different results; choose based on your data.

## [Mental model]

- **Embedding**: Represents data in high-dimensional space.
- **Querying**: Find nearest neighbors using similarity metrics.
- **Storage**: Use vector databases like ChromaDB, FAISS, or Pinecone for efficient retrieval.

```