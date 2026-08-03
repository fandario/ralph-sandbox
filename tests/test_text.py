import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from toolbox.text import squeeze, truncate  # noqa: E402


class Squeeze(unittest.TestCase):
    def test_riduce_gli_spazi_multipli(self):
        self.assertEqual(squeeze("a   b"), "a b")

    def test_toglie_quelli_ai_bordi(self):
        self.assertEqual(squeeze("  a b  "), "a b")

    def test_tratta_i_tab_come_spazi(self):
        self.assertEqual(squeeze("a\t\tb"), "a b")


class Truncate(unittest.TestCase):
    def test_lascia_invariata_la_stringa_piu_corta_del_limite(self):
        self.assertEqual(truncate("ciao", 10), "ciao")

    def test_lascia_invariata_la_stringa_lunga_quanto_il_limite(self):
        self.assertEqual(truncate("ciao", 4), "ciao")

    def test_accorcia_con_ellissi_la_stringa_troppo_lunga(self):
        self.assertEqual(truncate("buongiorno", 5), "buon…")

    def test_accorcia_anche_un_solo_carattere_di_troppo(self):
        self.assertEqual(truncate("ciao!", 4), "cia…")

    def test_col_limite_a_uno_resta_solo_l_ellissi(self):
        self.assertEqual(truncate("ciao", 1), "…")

    def test_rifiuta_un_limite_minore_di_uno(self):
        with self.assertRaises(ValueError):
            truncate("buongiorno", 0)


if __name__ == "__main__":
    unittest.main()
