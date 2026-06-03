"""Griffe extension: fill @copydoc docstrings by reading directly from cuvis_il.

griffe uses static AST analysis when source files are present, which cannot see
docstrings assigned at runtime via the @copydoc decorator. This extension:

- For regular functions/methods: parses griffe's Decorator.value strings.
- For @property methods: uses the on_attribute_instance hook, which still has
  the original ast.FunctionDef node whose decorator_list contains @copydoc.
  (Attribute objects in griffe have no decorators field; Function does.)

In both cases the cuvis_il function name is extracted via regex, cuvis_il is
imported directly (bypassing cuvis/__init__.py and its sys.exit guard), and the
docstring is attached with an explicit sphinx parser so it renders correctly.
"""
from __future__ import annotations

import ast
import re
from typing import Any

import griffe

_IL_FN = re.compile(r"cuvis_il\.(\w+)")


class CopydocExtension(griffe.Extension):
    def __init__(self) -> None:
        self._il: Any = None

    def _load_il(self) -> Any:
        if self._il is not None:
            return self._il
        try:
            from cuvis_il import cuvis_il as _il  # package form (some installs)
            self._il = _il
        except ImportError:
            try:
                import cuvis_il as _il  # flat-module form (Linux container)
                self._il = _il
            except Exception:
                pass
        return self._il

    @staticmethod
    def _description_only(doc: str) -> str:
        """Keep only the prose description; strip sphinx field directives (:param: etc.)."""
        lines = doc.splitlines()
        out = []
        for line in lines:
            if line.strip().startswith(":"):
                break
            out.append(line)
        while out and not out[-1].strip():
            out.pop()
        return "\n".join(out).strip()

    def _doc_from_decorator_strs(self, strs: list[str]) -> str | None:
        il = self._load_il()
        if il is None:
            return None
        for s in strs:
            if "copydoc" not in s:
                continue
            m = _IL_FN.search(s)
            if m:
                fn = getattr(il, m.group(1), None)
                if fn and fn.__doc__:
                    return self._description_only(fn.__doc__)
        return None

    def on_function(self, *, func: griffe.Function, **kwargs: Any) -> None:
        try:
            if func.docstring is not None:
                return
            strs = [str(d.value) for d in func.decorators]
            doc = self._doc_from_decorator_strs(strs)
            if doc:
                func.docstring = griffe.Docstring(doc, parent=func, parser="sphinx")
        except Exception:
            pass

    def on_attribute_instance(
        self, *, node: Any, attr: griffe.Attribute, agent: Any, **kwargs: Any
    ) -> None:
        # Attribute has no decorators field; the ast.FunctionDef node does.
        # attr.labels already includes "property" when this hook fires.
        try:
            if attr.docstring is not None or "property" not in attr.labels:
                return
            strs = [ast.unparse(d) for d in getattr(node, "decorator_list", [])]
            doc = self._doc_from_decorator_strs(strs)
            if doc:
                attr.docstring = griffe.Docstring(doc, parent=attr, parser="sphinx")
        except Exception:
            pass
