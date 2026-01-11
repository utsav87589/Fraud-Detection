**Important**

- Feature dominance note

The feature Failed_Transaction_Count_7d shows a strong monotonic relationship with the target label.
While this feature is not a direct source of data leakage, it acts as a dominant proxy variable that enables tree-based models to achieve near-perfect splits with minimal depth.

As a result, the model relies almost exclusively on this feature and fails to learn from other transactional and behavioral signals.

To encourage meaningful feature learning and improve model generalization, this feature is excluded from tree-based models while retained for exploratory analysis and non-tree models.