"""Unit tests for gogoML model utilities."""

from __future__ import annotations

import numpy as np

from gogoML.data import load_iris_dataset
from gogoML.model import train_logistic_regression


def test_train_logistic_regression_accuracy() -> None:
    """Ensure that the logistic regression achieves a reasonable accuracy."""
    df = load_iris_dataset()
    X = df.drop(columns=["target"]).values
    y = df["target"].values
    result = train_logistic_regression(X, y, test_size=0.3, random_state=123)
    # The iris dataset is well behaved; logistic regression should be >90% accurate
    assert result.accuracy >= 0.9