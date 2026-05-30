```markdown
# Recommender Systems — Cheatsheet

## [Core Concepts]

| Type               | Description                                                                                         | Use Case                              |
|--------------------|-----------------------------------------------------------------------------------------------------|---------------------------------------|
| Collaborative Filtering | Makes recommendations based on user-item interactions. Utilizes user or item similarities.        | User recommendations based on similar users. |
| Content-Based      | Recommends items similar to those the user has liked before, based on item features.               | Movie recommendations based on genres or actors. |
| Hybrid             | Combines collaborative and content-based filtering to improve accuracy.                             | Platforms like Netflix or Amazon.     |
| Neural Recommenders | Uses neural networks to model complex patterns in user-item interactions.                          | Advanced recommendation systems.      |

## [Common Operations]

```python
# Collaborative Filtering Example
from surprise import Dataset, Reader
from surprise import SVD, accuracy
from surprise.model_selection import train_test_split

data = Dataset.load_from_file('data.csv', Reader('line_format', sep=','))
trainset, testset = train_test_split(data, test_size=0.2)
model = SVD()
model.fit(trainset)
predictions = model.test(testset)
accuracy.rmse(predictions)

# Content-Based Filtering Example
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample item data
df = pd.DataFrame({
    'item_id': [1, 2, 3],
    'description': ["Action movie", "Romantic comedy", "Sci-fi adventure"]
})

# Compute TF-IDF matrix
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(df['description'])

# Compute similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Hybrid Example (combining scores from CF and CBF)
def hybrid_recommendation(cf_scores, cbf_scores):
    return (0.5 * cf_scores) + (0.5 * cbf_scores)

# Neural Recommender Example (using Keras)
import numpy as np
from keras.models import Model
from keras.layers import Input, Embedding, Flatten, Dot

# Define input layers
user_input = Input(shape=(1,))
item_input = Input(shape=(1,))

# Define embedding layers
user_embedding = Embedding(input_dim=num_users, output_dim=10)(user_input)
item_embedding = Embedding(input_dim=num_items, output_dim=10)(item_input)

# Dot product for similarity
dot_product = Dot(axes=1)([user_embedding, item_embedding])
model = Model(inputs=[user_input, item_input], outputs=dot_product)
model.compile(optimizer='adam', loss='mean_squared_error')
```

## [Gotchas]

- ⚠️ Collaborative filtering can suffer from the "cold start" problem when new users/items are introduced.
- ⚠️ Content-based methods may lead to over-specialization, where users only see items similar to their past preferences.

## [Mental Model]

- **Collaborative Filtering:** User-User / Item-Item similarity → Recommendations
- **Content-Based:** User preferences based on item features → Recommendations
- **Hybrid Model:** Combines strengths of CF and content-based → Better recommendations
```