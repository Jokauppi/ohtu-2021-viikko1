import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_tilavuus_nollaksi(self):
        varasto = Varasto(-1, 1)

        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_ylimeneva_alku_saldo_tilavuudeksi(self):
        varasto = Varasto(5, 10)

        self.assertAlmostEqual(varasto.saldo, 5)

    def test_negatiivinen_alku_saldo_nollaksi(self):
        varasto = Varasto(5, -1)

        self.assertAlmostEqual(varasto.saldo, 0)

    def test_negatiivinen_lisays_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.lisaa_varastoon(-4)

        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_negatiivinen_otto_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(-4)

        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_ylimeneva_lisays_asettaa_saldoksi_tilavuuden(self):
        self.varasto.lisaa_varastoon(15)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ylimeneva_otto_palauttaa_vain_saldon(self):
        self.varasto.lisaa_varastoon(3)

        saatu_maara = self.varasto.ota_varastosta(6)

        self.assertAlmostEqual(saatu_maara, 3)

    def test_str_palauttaa_oikein(self):
        self.varasto.lisaa_varastoon(6)

        self.assertEqual(str(self.varasto), "saldo = 6, vielä tilaa 4")