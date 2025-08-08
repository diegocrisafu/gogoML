"""Data loading utilities for gogoML.

Currently this module provides a single function to load the Iris flower
dataset from scikit‑learn as a pandas `DataFrame` for convenience.  In
future versions additional datasets and loading helpers can be added.
"""

from __future__ import annotations

import pandas as pd
from sklearn import datasets


def load_iris_dataset() -> pd.DataFrame:
    """Load the Iris dataset into a pandas DataFrame.

    Returns
    -------
    pandas.DataFrame
        A DataFrame with four feature columns and a `target` column with
        integer labels.
    """
    iris = datasets.load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df["target"] = iris.target
    return df