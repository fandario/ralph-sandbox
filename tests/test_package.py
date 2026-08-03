import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import toolbox.text  # noqa: E402
from toolbox import slugify, squeeze, truncate  # noqa: E402


class InterfacciaDelPackage(unittest.TestCase):
    def test_espone_le_tre_funzioni_di_testo(self):
        self.assertIs(squeeze, toolbox.text.squeeze)
        self.assertIs(truncate, toolbox.text.truncate)
        self.assertIs(slugify, toolbox.text.slugify)

    def test_dichiara_i_tre_nomi_in_all(self):
        self.assertEqual(sorted(toolbox.__all__), ["slugify", "squeeze", "truncate"])


if __name__ == "__main__":
    unittest.main()
