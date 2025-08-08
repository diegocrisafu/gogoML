"""Model training utilities for gogoML.

This module contains simple functions to train and evaluate machine
learning models.  Currently it includes a helper for fitting a logistic
regression classifier on a tabular dataset.  Models are returned so
callers can perform further predictions or evaluations.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


@dataclass
class ModelResult:
    """Encapsulates a trained model and its evaluation metrics."""

    model: LogisticRegression
    accuracy: float


def train_logistic_regression(
    X: np.ndarray, y: np.ndarray, test_size: float = 0.2, random_state: int | None = 42
) -> ModelResult:
    """Train a logistic regression classifier.

    Parameters
    ----------
    X : np.ndarray
        Feature matrix of shape (n_samples, n_features).
    y : np.ndarray
        Label array of shape (n_samples,).
    test_size : float, optional
        Fraction of the data to allocate to the test split (default is 0.2).
    random_state : int | None, optional
        Random seed for splitting the data (default is 42).

    Returns
    -------
    ModelResult
        Object containing the trained model and its accuracy on the test set.
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    clf = LogisticRegression(max_iter=200)
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    acc = accuracy_score(y_test, preds)
    return ModelResult(model=clf, accuracy=acc)