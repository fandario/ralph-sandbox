"""Utilità di testo minimali."""

from .text import (
    initials,
    reverse_words,
    slugify,
    squeeze,
    strip_accents,
    titlecase,
    truncate,
)

__all__ = [
    "squeeze",
    "truncate",
    "slugify",
    "titlecase",
    "reverse_words",
    "initials",
    "strip_accents",
]
