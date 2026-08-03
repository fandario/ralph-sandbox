import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from toolbox.text import squeeze  # noqa: E402


class Squeeze(unittest.TestCase):
    def test_riduce_gli_spazi_multipli(self):
        self.assertEqual(squeeze("a   b"), "a b")

    def test_toglie_quelli_ai_bordi(self):
        self.assertEqual(squeeze("  a b  "), "a b")

    def test_tratta_i_tab_come_spazi(self):
        self.assertEqual(squeeze("a\t\tb"), "a b")


if __name__ == "__main__":
    unittest.main()
