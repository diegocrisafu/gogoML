"""Top‑level package for gogoML.

This package exposes simple utilities for loading datasets and training
models.  See the `data` and `model` modules for details.
"""

from .data import load_iris_dataset  # noqa: F401
from .model import train_logistic_regression  # noqa: F401