"""Funzioni di manipolazione del testo."""

import re
import unicodedata

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


def titlecase(value: str) -> str:
    """Mette in maiuscolo l'iniziale di ogni parola e in minuscolo il resto."""
    # Delega a `squeeze` la politica sugli spazi, così resta una sola.
    return " ".join(parola.capitalize() for parola in squeeze(value).split(" "))


def initials(value: str) -> str:
    """Unisce in maiuscolo la prima lettera di ogni parola."""
    # Come `titlecase`, delega a `squeeze` la politica sugli spazi; lo `split`
    # senza argomenti non produce parole vuote, nemmeno sulla stringa vuota.
    return "".join(parola[0] for parola in squeeze(value).split()).upper()


def slugify(value: str) -> str:
    """Trasforma la stringa in un identificatore minuscolo con le parole unite da `-`."""
    # NFC dopo il minuscolo: ricompone i segni combinanti, che altrimenti `\W`
    # tratterebbe da separatori, e dà lo stesso slug per NFC e NFD.
    normalizzata = unicodedata.normalize("NFC", value.lower())
    return _NON_ALFANUMERICI.sub("-", normalizzata).strip("-")
