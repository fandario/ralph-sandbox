import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from toolbox.text import slugify, squeeze  # noqa: E402


class Squeeze(unittest.TestCase):
    def test_riduce_gli_spazi_multipli(self):
        self.assertEqual(squeeze("a   b"), "a b")

    def test_toglie_quelli_ai_bordi(self):
        self.assertEqual(squeeze("  a b  "), "a b")

    def test_tratta_i_tab_come_spazi(self):
        self.assertEqual(squeeze("a\t\tb"), "a b")


class Slugify(unittest.TestCase):
    def test_esempio_della_issue(self):
        self.assertEqual(slugify("  Ciao, Mondo!! "), "ciao-mondo")

    def test_mette_tutto_in_minuscolo(self):
        self.assertEqual(slugify("CIAO"), "ciao")

    def test_riduce_i_separatori_a_un_solo_trattino(self):
        self.assertEqual(slugify("a -_ b"), "a-b")

    def test_toglie_i_trattini_ai_bordi(self):
        self.assertEqual(slugify("--ciao--"), "ciao")

    def test_la_stringa_vuota_resta_vuota(self):
        self.assertEqual(slugify(""), "")

    def test_solo_separatori_danno_stringa_vuota(self):
        self.assertEqual(slugify(" -- ,! "), "")


if __name__ == "__main__":
    unittest.main()
