import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import toolbox.text  # noqa: E402
from toolbox import (  # noqa: E402
    initials,
    reverse_words,
    slugify,
    squeeze,
    titlecase,
    truncate,
)


class InterfacciaDelPackage(unittest.TestCase):
    def test_espone_le_sei_funzioni_di_testo(self):
        self.assertIs(squeeze, toolbox.text.squeeze)
        self.assertIs(truncate, toolbox.text.truncate)
        self.assertIs(slugify, toolbox.text.slugify)
        self.assertIs(titlecase, toolbox.text.titlecase)
        self.assertIs(reverse_words, toolbox.text.reverse_words)
        self.assertIs(initials, toolbox.text.initials)

    def test_dichiara_i_sei_nomi_in_all(self):
        self.assertEqual(
            sorted(toolbox.__all__),
            ["initials", "reverse_words", "slugify", "squeeze", "titlecase", "truncate"],
        )


if __name__ == "__main__":
    unittest.main()
