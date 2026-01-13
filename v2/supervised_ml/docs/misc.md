**Important**

- Feature dominance note

- The feature Failed_Transaction_Count_7d shows a strong monotonic relationship with the target label.
While this feature is not a direct source of data leakage, it acts as a dominant proxy variable that enables tree-based models to achieve near-perfect splits with minimal depth.

- As a result, the model relies almost exclusively on this feature and fails to learn from other transactional and behavioral signals.

- To encourage meaningful feature learning and improve model generalization, this feature is excluded from tree-based models while retained for exploratory analysis and non-tree models.

- For tree-based models, a specific feature produced near-perfect splits, dominating the decision process. While not a source of data leakage, this feature acted as a strong proxy and reduced model robustness. To ensure stable and interpretable tree behavior, the feature was excluded only during model training and prediction for tree-based models. The original dataset was kept unchanged to avoid pipeline noise and unintended side effects.