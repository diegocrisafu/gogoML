# gogoML

Welcome to **gogoML**, an educational machine‑learning playground.  This
repository provides a minimal yet opinionated structure for experimenting
with classical ML techniques using Python.  Out of the box it offers a
ready‑to‑run example that trains a simple model on the Iris flower
dataset, unit tests to validate the core logic, and continuous
integration to keep things green.

## Features

* **Structured project layout** – your code lives in the `src/` package and
  tests live in `tests/`, encouraging good separation from day one.
* **Example workflow** – run `python -m gogoML.train` to load the Iris
  dataset, train a logistic regression classifier and evaluate its
  accuracy.
* **Dependency management** – all dependencies are pinned in
  `requirements.txt` and can be installed with `pip install -r requirements.txt`.
* **Testing** – basic unit tests using `pytest` verify that the model
  training pipeline produces reasonable accuracy.
* **Continuous integration** – a GitHub Actions workflow runs `pytest` on
  every pull request and on push to the `main` branch.
* **Pre‑commit hooks** – optional support for code formatting and
  linting (via [pre‑commit](https://pre-commit.com/)) is provided in
  `.pre-commit-config.yaml`.  Install with `pre-commit install` to
  automatically format code with `black` and sort imports with `isort` on
  every commit.

## Getting started

1. **Clone the repo**:

   ```bash
   git clone https://github.com/diegocrisafu/gogoML.git
   cd gogoML
   ```

2. **Set up a virtual environment** (recommended):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the example**:

   ```bash
   python -m gogoML.train
   ```

   This will print the accuracy of a logistic regression classifier trained
   on the Iris dataset.

5. **Run tests**:

   ```bash
   pytest
   ```

6. **Enable pre‑commit hooks** (optional):

   ```bash
   pip install pre-commit
   pre-commit install
   ```

## Project structure

```
gogoML/
├── src/          # Library code
│   ├── __init__.py
│   ├── data.py   # Utilities for loading datasets
│   ├── model.py  # Model training and evaluation functions
│   └── train.py  # CLI entry point to train on the Iris dataset
├── tests/        # Unit tests
│   └── test_model.py
├── requirements.txt
├── .pre-commit-config.yaml  # Pre-commit hooks (optional)
├── .github/workflows/python-ci.yml  # CI configuration
└── README.md
```

## Contributing

Contributions are welcome!  Feel free to open an issue or pull request if
you have suggestions, bug reports or new examples.  Please make sure
CI passes (`pytest`) and format your code (`pre-commit run --all-files`) before
submitting.

## License

This project is released under the MIT License.  See the [LICENSE](LICENSE)
file for details.