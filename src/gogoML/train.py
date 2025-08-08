"""Command‑line entry point for training a model on the Iris dataset.

This module can be executed directly (`python -m gogoML.train`) to load
the Iris dataset, fit a logistic regression classifier and print the
resulting accuracy.  It demonstrates how to use the utilities provided
in the `data` and `model` modules.
"""

from __future__ import annotations

import numpy as np

from .data import load_iris_dataset
from .model import train_logistic_regression


def main() -> None:
    df = load_iris_dataset()
    X = df.drop(columns=["target"]).values
    y = df["target"].values
    result = train_logistic_regression(X, y)
    print(f"Model accuracy: {result.accuracy:.2%}")


if __name__ == "__main__":
    main()