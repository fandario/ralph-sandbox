"""Funzioni di manipolazione del testo."""


def squeeze(value: str) -> str:
    """Riduce ogni sequenza di spazi bianchi a un singolo spazio."""
    return " ".join(value.split())
