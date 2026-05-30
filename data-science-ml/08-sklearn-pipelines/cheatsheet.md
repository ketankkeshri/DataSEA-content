```markdown
# Scikit-Learn Pipelines — Cheatsheet

## [Core syntax]

| Thing                    | Syntax                                          | Notes                                              |
|--------------------------|-------------------------------------------------|----------------------------------------------------|
| Creating a Pipeline      | `pipeline = Pipeline(steps=[('name', estimator)])` | Use to chain multiple transformers and estimators. |
| Fitting a Pipeline       | `pipeline.fit(X, y)`                           | Fits the entire pipeline on the input data.       |
| Predicting with a Pipeline| `pipeline.predict(X)`                        | Generates predictions using the fitted pipeline.   |
| Cross-Validation         | `cross_val_score(pipeline, X, y, cv=k)`       | Evaluates the model using k-fold cross-validation. |
| Grid Search              | `GridSearchCV(pipeline, param_grid)`          | Searches for the best hyperparameters for the pipeline. |

## [Common operations]

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, GridSearchCV

# Create a pipeline
pipeline = Pipeline(steps=[
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier())
])

# Fit the pipeline
pipeline.fit(X_train, y_train)

# Predict with the pipeline
predictions = pipeline.predict(X_test)

# Cross-validation
scores = cross_val_score(pipeline, X, y, cv=5)

# Hyperparameter tuning with Grid Search
param_grid = {
    'classifier__n_estimators': [50, 100],
    'classifier__max_depth': [None, 10, 20]
}
grid_search = GridSearchCV(pipeline, param_grid, cv=5)
grid_search.fit(X_train, y_train)
best_params = grid_search.best_params_
```

## [Gotchas]

- ⚠️ Ensure that all transformers in the pipeline are compatible with the input data types.
- ⚠️ When using `GridSearchCV`, specify hyperparameters with double underscores (e.g., `classifier__n_estimators`).

## [Mental model]

1. **Pipeline Structure**: Each step is a transformation or model, processed in sequence.
2. **Data Flow**: Input data → Step 1 (transform) → Step 2 (transform) → Final Estimator (predict).
3. **Parameter Tuning**: Use `GridSearchCV` to optimize parameters across the entire pipeline.
```