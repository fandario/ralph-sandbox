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


def reverse_words(value: str) -> str:
    """Inverte l'ordine delle parole della stringa, non i loro caratteri."""
    # Delega a `squeeze` la politica sugli spazi, così resta una sola.
    return " ".join(reversed(squeeze(value).split(" ")))


def initials(value: str) -> str:
    """Unisce in maiuscolo la prima lettera di ogni parola."""
    # NFC come in `slugify`: ricompone i segni combinanti, altrimenti l'iniziale
    # di una lettera accentata in NFD sarebbe la lettera nuda senza accento.
    # Lo `split` senza argomenti divide su qualunque sequenza di spazi bianchi,
    # bordi compresi, e non produce parole vuote nemmeno sulla stringa vuota.
    normalizzata = unicodedata.normalize("NFC", value)
    return "".join(parola[0] for parola in normalizzata.split()).upper()


def strip_accents(value: str) -> str:
    """Toglie gli accenti dalle lettere lasciando invariato il resto della stringa."""
    # Si lavora un gruppo per volta — un carattere con i segni che lo seguono —
    # perché quello da cui non si toglie niente va restituito tale e quale:
    # normalizzare tutta la stringa in uscita cambierebbe anche caratteri senza
    # accento (U+2126 OHM SIGN diventerebbe l'omega greca).
    gruppi: list[str] = []
    for carattere in value:
        if gruppi and unicodedata.category(carattere).startswith("M"):
            gruppi[-1] += carattere
        else:
            gruppi.append(carattere)

    pezzi = []
    for gruppo in gruppi:
        # NFD separa la lettera dal suo segno diacritico, che ha categoria "Mn"
        # (mark, nonspacing). Si scartano solo i segni che stanno su una lettera:
        # su altro portano il significato del carattere e toglierli lo ribalta —
        # `≠` si scompone in `=` più U+0338 e diventerebbe `=`.
        # Restano fuori i diacritici incorporati nel codepoint, che NFD non
        # scompone: `ø ł đ` e simili passano interi, per loro servirebbe una
        # tabella di mappatura esplicita.
        decomposto = unicodedata.normalize("NFD", gruppo)
        su_una_lettera = unicodedata.category(decomposto[0]).startswith("L")
        senza_segni = "".join(
            c
            for c in decomposto
            if not (su_una_lettera and unicodedata.category(c) == "Mn")
        )
        if senza_segni == decomposto:
            pezzi.append(gruppo)
        else:
            # NFC solo su ciò che si è toccato: la lettera nuda torna a essere
            # un singolo codepoint anche se l'ingresso era già scomposto.
            pezzi.append(unicodedata.normalize("NFC", senza_segni))
    return "".join(pezzi)


def slugify(value: str) -> str:
    """Trasforma la stringa in un identificatore minuscolo con le parole unite da `-`."""
    # NFC dopo il minuscolo: ricompone i segni combinanti, che altrimenti `\W`
    # tratterebbe da separatori, e dà lo stesso slug per NFC e NFD.
    normalizzata = unicodedata.normalize("NFC", value.lower())
    return _NON_ALFANUMERICI.sub("-", normalizzata).strip("-")
