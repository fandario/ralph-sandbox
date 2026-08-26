import sys
import unicodedata
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from toolbox.text import (  # noqa: E402
    initials,
    reverse_words,
    slugify,
    squeeze,
    strip_accents,
    titlecase,
    truncate,
)


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


class Slugify(unittest.TestCase):
    def test_trasforma_un_titolo_in_un_identificatore(self):
        self.assertEqual(slugify("  Ciao, Mondo!! "), "ciao-mondo")

    def test_tiene_le_lettere_accentate_che_sono_alfanumeriche(self):
        self.assertEqual(slugify("Città di Milano"), "città-di-milano")

    def test_tratta_il_trattino_basso_come_separatore(self):
        self.assertEqual(slugify("ciao_mondo"), "ciao-mondo")

    def test_mette_tutto_in_minuscolo(self):
        self.assertEqual(slugify("CIAO"), "ciao")

    def test_riduce_una_sequenza_di_separatori_a_un_solo_trattino(self):
        self.assertEqual(slugify("ciao -- , mondo"), "ciao-mondo")

    def test_toglie_i_trattini_ai_bordi(self):
        self.assertEqual(slugify("!!ciao mondo!!"), "ciao-mondo")

    def test_lascia_vuota_la_stringa_vuota(self):
        self.assertEqual(slugify(""), "")

    def test_lascia_vuota_una_stringa_di_soli_separatori(self):
        self.assertEqual(slugify("  --,, "), "")

    def test_tiene_le_cifre(self):
        self.assertEqual(slugify("Report 2024"), "report-2024")

    def test_lascia_invariato_uno_slug_gia_formato(self):
        self.assertEqual(slugify("già-fatto"), "già-fatto")

    def test_da_lo_stesso_slug_per_le_due_forme_unicode(self):
        parola = "città di Milano"
        self.assertEqual(
            slugify(unicodedata.normalize("NFD", parola)),
            slugify(unicodedata.normalize("NFC", parola)),
        )
        self.assertEqual(slugify(unicodedata.normalize("NFD", parola)), "città-di-milano")


class Titlecase(unittest.TestCase):
    def test_mette_in_maiuscolo_l_iniziale_di_ogni_parola(self):
        self.assertEqual(titlecase("ciao mondo"), "Ciao Mondo")

    def test_mette_in_minuscolo_il_resto_della_parola(self):
        self.assertEqual(titlecase("cIAO MONDO"), "Ciao Mondo")

    def test_normalizza_gli_spazi_come_squeeze(self):
        grezza = "  ciao   MONDO "
        self.assertEqual(titlecase(grezza), "Ciao Mondo")
        # Parità con `squeeze`: se la sua politica sugli spazi cambia, qui si vede.
        self.assertEqual(titlecase(grezza).lower(), squeeze(grezza).lower())

    def test_tratta_i_tab_come_spazi(self):
        self.assertEqual(titlecase("ciao\t\tmondo"), "Ciao Mondo")

    def test_lascia_vuota_la_stringa_vuota(self):
        self.assertEqual(titlecase(""), "")

    def test_lascia_vuota_una_stringa_di_soli_spazi(self):
        self.assertEqual(titlecase("   "), "")

    def test_mette_in_maiuscolo_anche_le_lettere_accentate(self):
        self.assertEqual(titlecase("èlia di milano"), "Èlia Di Milano")


class ReverseWords(unittest.TestCase):
    def test_inverte_l_ordine_delle_parole(self):
        self.assertEqual(reverse_words("ciao mondo bello"), "bello mondo ciao")

    def test_non_inverte_i_caratteri_delle_parole(self):
        self.assertEqual(reverse_words("abc def"), "def abc")

    def test_normalizza_gli_spazi_come_squeeze(self):
        grezza = "  ciao   mondo bello "
        self.assertEqual(reverse_words(grezza), "bello mondo ciao")

    def test_tratta_i_tab_come_spazi(self):
        self.assertEqual(reverse_words("ciao\t\tmondo"), "mondo ciao")

    def test_lascia_vuota_la_stringa_vuota(self):
        self.assertEqual(reverse_words(""), "")

    def test_lascia_vuota_una_stringa_di_soli_spazi(self):
        self.assertEqual(reverse_words("   "), "")

    def test_lascia_invariata_una_sola_parola(self):
        self.assertEqual(reverse_words("  ciao "), "ciao")


class Initials(unittest.TestCase):
    def test_prende_l_iniziale_di_ogni_parola(self):
        self.assertEqual(initials("mario rossi"), "MR")

    def test_non_conta_gli_spazi_multipli(self):
        self.assertEqual(initials("mario  rossi"), "MR")

    def test_ignora_gli_spazi_ai_bordi(self):
        self.assertEqual(initials("  mario rossi  "), "MR")

    def test_tratta_i_tab_come_spazi(self):
        self.assertEqual(initials("mario\t\trossi"), "MR")

    def test_mette_in_maiuscolo_le_iniziali_gia_maiuscole(self):
        self.assertEqual(initials("Mario Rossi"), "MR")

    def test_unisce_le_iniziali_senza_separatori(self):
        self.assertEqual(initials("anna maria luisa rossi"), "AMLR")

    def test_prende_una_sola_lettera_da_una_parola_di_un_carattere(self):
        self.assertEqual(initials("a b"), "AB")

    def test_lascia_vuota_la_stringa_vuota(self):
        self.assertEqual(initials(""), "")

    def test_lascia_vuota_una_stringa_di_soli_spazi(self):
        self.assertEqual(initials("   "), "")

    def test_mette_in_maiuscolo_anche_le_lettere_accentate(self):
        self.assertEqual(initials("èlia òrsi"), "ÈÒ")

    def test_da_le_stesse_iniziali_per_le_due_forme_unicode(self):
        nome = "èlia òrsi"
        self.assertEqual(
            initials(unicodedata.normalize("NFD", nome)),
            initials(unicodedata.normalize("NFC", nome)),
        )
        self.assertEqual(initials(unicodedata.normalize("NFD", nome)), "ÈÒ")


class StripAccents(unittest.TestCase):
    def test_toglie_l_accento_tenendo_la_lettera(self):
        self.assertEqual(strip_accents("perché"), "perche")

    def test_toglie_l_accento_grave(self):
        self.assertEqual(strip_accents("città"), "citta")

    def test_lascia_invariati_i_caratteri_senza_accento(self):
        self.assertEqual(strip_accents("ciao mondo"), "ciao mondo")

    def test_lascia_vuota_la_stringa_vuota(self):
        self.assertEqual(strip_accents(""), "")

    def test_tiene_le_maiuscole(self):
        self.assertEqual(strip_accents("Èlia"), "Elia")

    def test_lascia_invariati_spazi_e_punteggiatura(self):
        self.assertEqual(strip_accents("  perché, però!  "), "  perche, pero!  ")

    def test_da_lo_stesso_risultato_per_le_due_forme_unicode(self):
        parola = "città"
        self.assertEqual(
            strip_accents(unicodedata.normalize("NFD", parola)),
            strip_accents(unicodedata.normalize("NFC", parola)),
        )
        self.assertEqual(strip_accents(unicodedata.normalize("NFD", parola)), "citta")

    def test_lascia_intatti_i_caratteri_scomponibili_che_non_sono_accenti(self):
        # "한" si scompone in jamo che non sono segni diacritici: non c'è
        # nessun accento da togliere, quindi deve uscire com'è entrato.
        self.assertEqual(strip_accents("한"), "한")

    def test_tiene_i_segni_che_non_stanno_su_una_lettera(self):
        # "≠" si scompone in "=" più U+0338: scartare il segno combinante
        # direbbe il contrario dell'ingresso.
        self.assertEqual(strip_accents("a ≠ b"), "a ≠ b")
        self.assertEqual(strip_accents("x ∉ S"), "x ∉ S")
        self.assertEqual(strip_accents("1 ≮ 2"), "1 ≮ 2")

    def test_non_rinormalizza_i_caratteri_che_non_tocca(self):
        # Decomposizioni singleton: normalizzare l'uscita li sostituirebbe con
        # un altro codepoint pur non essendoci accenti da togliere.
        for carattere in ("Ω", "K"):
            with self.subTest(carattere=carattere):
                self.assertEqual(strip_accents(carattere), carattere)

    def test_tiene_un_segno_combinante_senza_carattere_di_base(self):
        # Accento acuto combinante da solo: non c'è nessuna lettera sotto.
        self.assertEqual(strip_accents("́"), "́")


if __name__ == "__main__":
    unittest.main()
