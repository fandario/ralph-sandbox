# Convenzioni

- Python 3, solo standard library.
- Ogni funzione pubblica ha una docstring di una riga che dice *cosa* fa.
- Ogni funzione nuova ha test in `tests/`, con `unittest`.
- I test si lanciano con `python3 -m unittest discover -s tests`.
- Niente dipendenze esterne, niente file di configurazione aggiuntivi.
