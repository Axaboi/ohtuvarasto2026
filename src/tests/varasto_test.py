import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_printtaus(self):

        self.assertAlmostEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")

    def test_uudella_varastolla_miinussaldo(self):
        self.varasto = Varasto(10, -1)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_nolla_tilavuus(self):
        self.varasto = Varasto(0)

        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_uudella_varastolla_saldo_tilavuus_sama(self):
        saldon_vertaus_varasto_ei_luotu = 10

        self.varasto = Varasto(10, saldon_vertaus_varasto_ei_luotu)

        self.assertAlmostEqual(self.varasto.saldo, saldon_vertaus_varasto_ei_luotu)

    def test_varastolla_saldo_tilaa_suurempi(self):
        self.varasto = Varasto(10, 100)

        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_varastolla_saldo_pienempi_ei_miinus(self):
        saldon_vertaus_varastoa_ei_luotu = 1

        self.varasto = Varasto(10, saldon_vertaus_varastoa_ei_luotu)

        self.assertAlmostEqual(self.varasto.saldo, saldon_vertaus_varastoa_ei_luotu)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_miinus_maara(self):
        tyhjä_arvo = self.varasto.lisaa_varastoon(-1)

        self.assertAlmostEqual(tyhjä_arvo, None)

    def test_maara_sama_tilavuus(self):
        maara = 10

        self.varasto.lisaa_varastoon(maara)

        self.assertAlmostEqual(self.varasto.saldo, maara)

    def test_maara_tilavuutta_suurempi(self):
        maara = 100

        self.varasto.lisaa_varastoon(maara)

        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_miinus_maara(self):
        maara = -1

        testi_tulos = self.varasto.ota_varastosta(maara)

        self.assertAlmostEqual(testi_tulos, 0)

    def test_ottaminen_maara_saldoa_suurempi_palauttaa_oikein(self):
        self.varasto = Varasto(10, 10)

        maara = 100

        self.varasto.ota_varastosta(maara)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
