"""Funzioni di manipolazione del testo."""

import re

_SEPARATORI = re.compile(r"[\W_]+")


def squeeze(value: str) -> str:
    """Riduce ogni sequenza di spazi bianchi a un singolo spazio."""
    return " ".join(value.split())


def slugify(value: str) -> str:
    """Trasforma un testo in uno slug minuscolo con i gruppi alfanumerici uniti da trattini."""
    return _SEPARATORI.sub("-", value.lower()).strip("-")
