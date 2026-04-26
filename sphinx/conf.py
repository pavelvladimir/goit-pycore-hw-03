"""Sphinx configuration for Python API documentation."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

project = "goit-pycore-hw-03"
copyright = "2026, Pavel Travnicek"
author = "Pavel Travnicek"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
exclude_patterns = ["_build"]

autodoc_member_order = "bysource"
autodoc_typehints = "description"

html_theme = "alabaster"
html_static_path: list[str] = []
