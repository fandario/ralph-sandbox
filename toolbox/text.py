"""Funzioni di manipolazione del testo."""

import re

_NON_ALFANUMERICI = re.compile(r"[\W_]+")


def squeeze(value: str) -> str:
    """Riduce ogni sequenza di spazi bianchi a un singolo spazio."""
    return " ".join(value.split())


def truncate(value: str, limit: int) -> str:
    """Accorcia la stringa a `limit` caratteri segnalando il taglio con un'ellissi."""
    if limit < 1:
        raise ValueError("limit deve essere almeno 1")
    if len(value) <= limit:
        return value
    return value[: limit - 1] + "…"


def slugify(value: str) -> str:
    """Trasforma la stringa in un identificatore minuscolo con le parole unite da `-`."""
    return _NON_ALFANUMERICI.sub("-", value.lower()).strip("-")
