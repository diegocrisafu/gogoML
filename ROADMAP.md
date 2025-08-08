# Roadmap – gogoML

This roadmap outlines the next steps for enhancing gogoML beyond the
initial project scaffolding delivered in Batch 1.

1. **Interactive notebooks** – Add one or more Jupyter notebooks in a
   `notebooks/` directory.  These should demonstrate loading datasets,
   training models using the utilities in `src/gogoML`, and visualising
   results.  Include instructions in the README on how to launch the
   notebooks via JupyterLab.

2. **Contribution templates** – Create templates in
   `.github/ISSUE_TEMPLATE/` for bug reports and feature requests and
   a pull request template to guide contributors on how to submit
   changes.  Link these templates from the README.

3. **Environment & packaging** – Consider adding a `pyproject.toml`
   using Poetry or Hatch to manage dependencies and packaging.  Provide
   a lock file to ensure reproducible installs.

4. **Extended tests** – Expand the test suite to cover failure cases
   (e.g. invalid input shapes) and alternative models.  Aim for at
   least 85% coverage on touched code.

5. **Continuous benchmarking** – Add a small `PERF.md` in a future
   batch to record baseline training times and memory usage for
   different models and datasets.  This will facilitate optimisation
   efforts.