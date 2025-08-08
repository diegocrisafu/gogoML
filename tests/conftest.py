"""Pytest configuration file for gogoML tests.

This file modifies the Python path at runtime so that the `src/` directory
is discoverable by the test runner without requiring an editable install.
"""

import sys
from pathlib import Path

# Compute the absolute path to the repository root and the src directory
REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = REPO_ROOT / "src"

# Insert src/ at the beginning of sys.path if not already present
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))