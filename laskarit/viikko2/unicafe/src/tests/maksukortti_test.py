import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_kortille_voi_ladata_rahaa(self):
        self.maksukortti.lataa_rahaa(200)
        self.assertEqual(str(self.maksukortti), "saldo: 2.1")
    
    def test_kortin_saldo_vahenee_oikein_kun_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")
    
    def test_kortin_saldo_ei_muutu_jos_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
        
    def test_ota_rahaa_palauttaa_true_jos_saldoa_riittavasti(self):
        vastaus = self.maksukortti.ota_rahaa(5)
        self.assertEqual(vastaus, True)

    def test_ota_rahaa_palauttaa_false_jos_saldoa_ei_riittavasti(self):
        vastaus = self.maksukortti.ota_rahaa(50)
        self.assertEqual(vastaus, False)  