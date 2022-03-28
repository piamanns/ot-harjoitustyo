import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luotu_kassapaate_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_luodun_kassapaatteen_tila_alussa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_edullisen_lounaan_kateisosto_kasvattaa_kassaa_oikein_kun_maksu_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    
    def test_maukkaan_lounaan_kateisosto_kasvattaa_kassaa_oikein_kun_maksu_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    
    def test_edullisen_lounaan_kateisosto_vaihtoraha_oikein_kun_maksu_riittava(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(vaihtoraha, 260)
    
    def test_maukkaaan_lounaan_kateisosto_vaihtoraha_oikein_kun_maksu_riittava(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100)

    def test_edullisen_lounaan_kateisosto_kasvattaa_myytyjen_edullisten_lounaiden_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkaan_lounaan_kateisosto_kasvattaa_myytyjen_maukkaiden_lounaiden_maaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_edullisen_lounaan_kateisosto_ei_kasvata_kassaa_kun_maksu_ei_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_maukkaan_lounaan_kateisosto_ei_kasvata_kassaa_kun_maksu_ei_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_edullisen_lounaan_kateisosto_vaihtoraha_oikein_kun_maksu_ei_riittava(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(vaihtoraha, 100)

    def test_maukkaan_lounaan_kateisosto_vaihtoraha_oikein_kun_maksu_ei_riittava(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)

    def test_edullisen_lounaan_kateisosto_ei_kasvata_myytyjen_lounaiden_maaraa_kun_maksu_ei_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_maukkaan_lounaan_kateisosto_ei_kasvata_myytyjen_lounaiden_maaraa_kun_maksu_ei_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_edullisen_lounaan_korttiosto_veloittaa_kortilta_kun_saldo_riittava(self):
        maksukortti = Maksukortti(300)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 60)

    def test_maukkaan_lounaan_korttiosto_veloittaa_kortilta_kun_saldo_riittava(self):
        maksukortti = Maksukortti(500)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 100)
    
    def test_edullisen_lounaan_korttiosto_palauttaa_true_kun_saldo_riittava(self):
        maksukortti = Maksukortti(300)
        vastaus = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(vastaus, True)
    
    def test_maukkaan_lounaan_korttiosto_palauttaa_true_kun_saldo_riittava(self):
        maksukortti = Maksukortti(500)
        vastaus = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(vastaus, True)
    
    def test_edullisen_lounaan_korttiosto_kasvattaa_myytyjen_edullisten_lounaiden_maaraa(self):
        maksukortti = Maksukortti(300)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_maukkaan_lounaan_korttiosto_kasvattaa_myytyjen_edullisten_lounaiden_maaraa(self):
        maksukortti = Maksukortti(500)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_edullisen_lounaan_korttiosto_ei_veloita_kortilta_kun_saldo_ei_riittava(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 100)

    def test_maukkaan_lounaan_korttiosto_ei_veloita_kortilta_kun_saldo_ei_riittava(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 200)
    
    def test_edullisen_lounaan_korttiosto_ei_kasvata_myytyjen_lounaiden_maaraa_kun_saldo_ei_riittava(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaan_lounaan_korttiosto_ei_kasvata_myytyjen_lounaiden_maaraa_kun_saldo_ei_riittava(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_edullisen_lounaan_korttiosto_palauttaa_false_kun_saldo_ei_riittava(self):
        maksukortti = Maksukortti(100)
        vastaus = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(vastaus, False)
    
    def test_maukkaan_lounaan_korttiosto_palauttaa_false_kun_saldo_ei_riittava(self):
        maksukortti = Maksukortti(200)
        vastaus = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(vastaus, False)
    
    def test_kassan_rahamaara_ei_muutu_edullisen_lounaan_kortiostoksesta_kun_saldo_ei_riittava(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassan_rahamaara_ei_muutu_edullisen_lounaan_kortiostoksesta_kun_saldo_ei_riittava(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortin_arvo_muuttuu_oikein_saldoa_ladatessa(self):
        maksukortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 1000)
        self.assertEqual(maksukortti.saldo, 1000)
    
    def test_kassan_rahamaara_muuttuu_oikein_korttia_ladatessa(self):
        maksukortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)