# Ranking Metrics

Ranking metrics are crucial for evaluating models in scenarios where the order of predictions matters, such as recommendation systems and search engines. Understanding how to use these metrics can help you make better decisions when optimizing your models for real-world applications.

## What are Ranking Metrics?

Ranking metrics assess how well your model ranks items based on predicted relevance or scores. Unlike traditional metrics that focus on overall accuracy, ranking metrics evaluate how well the top predictions match the ground truth. Common ranking metrics include:

- **Mean Average Precision (MAP)**: Measures the average precision across multiple queries, giving more weight to higher-ranked items.
- **Normalized Discounted Cumulative Gain (NDCG)**: Accounts for the position of correct predictions, emphasizing that higher-ranked items are more important.
- **Precision at K (P@K)**: Measures the proportion of relevant items in the top K predictions.

### Mean Average Precision (MAP)

MAP is particularly useful when dealing with multiple queries. It averages the precision scores at each relevant item across all queries. Here’s how to calculate it:

1. For each query, sort the predicted items based on their scores.
2. Calculate precision at each relevant item.
3. Average these precision scores for the final MAP.

Here’s a simple example in Python:

```python
import numpy as np

def average_precision(y_true, y_scores):
    sorted_indices = np.argsort(-y_scores)  # Sort scores in descending order
    sorted_true = y_true[sorted_indices]
    
    precision_at_k = []
    relevant_count = 0
    
    for i, val in enumerate(sorted_true):
        if val == 1:  # Relevant item
            relevant_count += 1
            precision_at_k.append(relevant_count / (i + 1))

    return np.mean(precision_at_k) if precision_at_k else 0.0

# Example usage
y_true = np.array([0, 1, 0, 1, 1])  # Ground truth: 1=Relevant, 0=Not Relevant
y_scores = np.array([0.2, 0.9, 0.4, 0.6, 0.8])  # Predicted scores

map_score = average_precision(y_true, y_scores)
print(f'Mean Average Precision: {map_score:.2f}')
```

### Normalized Discounted Cumulative Gain (NDCG)

NDCG helps prioritize relevant results based on their rank. The idea is to give higher relevance scores to items that appear earlier in the ranking. The formula for NDCG is:

\[ \text{NDCG} = \frac{DCG}{IDCG} \]

Where:
- **DCG** is the Discounted Cumulative Gain.
- **IDCG** is the Ideal Discounted Cumulative Gain.

Here's how to implement it:

```python
def dcg(y_true, k):
    return sum((2 ** y_true[i] - 1) / np.log2(i + 2) for i in range(min(k, len(y_true))))

def ndcg(y_true, k):
    ideal = sorted(y_true, reverse=True)  # Ideal ranking
    return dcg(y_true, k) / dcg(ideal, k)

# Example usage
y_true = np.array([0, 1, 0, 1, 1])  # Ground truth
ndcg_score = ndcg(y_true, k=3)  # Calculate NDCG for top 3
print(f'NDCG: {ndcg_score:.2f}')
```

## Common pitfalls

- **Ignoring the rank**: Using metrics like accuracy without considering the ranking can mislead you, especially in scenarios where the position of predictions matters.
- **Overfitting to top K**: Focusing solely on top K precision can neglect the performance across the entire ranking, leading to a model that performs well on one metric but poorly elsewhere.
- **Not normalizing scores**: Failing to normalize metrics like NDCG can lead to skewed results, particularly when comparing across different datasets or queries.

## In a nutshell

- Ranking metrics evaluate how well your model orders predictions based on relevance.
- Key metrics include Mean Average Precision (MAP) and Normalized Discounted Cumulative Gain (NDCG).
- Use ranking metrics to optimize models for applications where order matters, like search engines and recommendations.
- Common pitfalls include ignoring the rank, overfitting to top K, and failing to normalize scores.