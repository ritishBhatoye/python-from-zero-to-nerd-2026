"""Tests for Exercise 85 — Docstring Explorer."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("85_docstring_explorer")
    square_with_doc = solution.square_with_doc
    get_builtin_docs = solution.get_builtin_docs
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestDocstringExplorer:
    def test_square_function(self):
        assert square_with_doc(5) == 25
        assert square_with_doc(3) == 9
        assert square_with_doc(0) == 0

    def test_has_docstring(self):
        assert square_with_doc.__doc__ is not None
        assert "square" in square_with_doc.__doc__.lower()

    def test_docstring_content(self):
        doc = square_with_doc.__doc__
        assert "Args:" in doc or "Parameters:" in doc or "number" in doc.lower()
        assert "Returns:" in doc or "return" in doc.lower()

    def test_get_builtin_docs(self):
        docs = get_builtin_docs()
        assert isinstance(docs, dict)
        assert 'abs' in docs
        assert 'int' in docs
        assert 'input' in docs

    def test_builtin_docs_not_empty(self):
        docs = get_builtin_docs()
        assert len(docs['abs']) > 0
        assert len(docs['int']) > 0
        assert len(docs['input']) > 0
