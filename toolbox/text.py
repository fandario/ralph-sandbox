"""Funzioni di manipolazione del testo."""


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
