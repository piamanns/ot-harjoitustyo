# Työaikakirjanpito

| Pvm | Tunteja | Mitä tein |
| :-----: | :-------: | :--------- |
| 29.3. | 2 | Vaatimusmäärittelyn kirjoittaminen |
| 3.4.  | 9 | Pyaudio- ja python-sounddevice-kirjastoihin tutustumista. Tkinterin opiskelua. Yksinkertaisen testisovelluksen toteutus (siniaaltoa tuottava oskillaattori, jonka voi käynnistää ja pysäyttää käyttöliittymän kautta).|
| 4.4. | 8 |  Muutoksia siniaalloon tuottamiseen. Käyttöliittymän laajentaminen: viritysäänen voi asettaa syöttämällä frekvenssin tekstikenttään tai preset-nappeja painamalla. Sovelluksen testaamista virtuaalityöasemalla. Ensimmäinen yksikkötesti.|
| 6.4. | 1 | Pylintin asennus ja pylint-virheiden korjausta.|
| 8.4. | 2 | Ui-näkymien refaktorointia. Ääniraudan asetusten tallennuksen suunnittelua.| 
| 9.4. | 5 | Sovelluslogiikan eriyttäminen käyttöliittymästä. Ympäristömuuttujat käyttöön. Toteutus ääniraudan asetusten lukemiselle/tallentamiselle, toistaiseksi csv-tiedoston avulla.
| 10.4. | 6 | Toteutus ääniraudan tallennettujen asetuksien poistamiselle. Alustava käyttöliittymä ääniraudan asetusten hallinnoimiselle. 
| 11.4. | 6 | Ääniraudan käyttöliittymän refaktorointia ja viilausta virtuaalityöasemalla. Syötetyn taajuuden validointi ja virheilmoituksen näyttäminen.|
| 12.4. | 1 | Yksikkötestauksen laajentaminen koskemaan myös tallennettujen asetusten lukemista ja tallentamista. Lisätestejä ääniraudalle. |
| 14.4. | 1 | Metronomin eri toteutusvaihtojen tutkimista.|
| 15.4. | 8 | Metronomin proof of concept (useamman epätarkasti tikittävän vaihtoehdon kokeilu ja hylkääminen, kunnes hyväksyttävä toteutustapa löytyi).|
| 16.4. | 1 | Yksinkertainen käyttöliittymä Metronomi-POC:lle. Toimivuuden testaus virtuaalityöasemalla.|
| 17.4. | 4 | Toteutus metronomin bpm-arvon asettamiselle. Graafisen käyttöliittymän viilausta. Yksikkötestejä metronomille.|
| 18.4. | 4 | Ääniraudalle ja metronomille syötettyjen arvojen validoinnin siirtäminen ääniraudan ja metronomin omille luokille. Virheilmoitus myös metronomille. Refaktoroinnin aiheuttamien bugien korjausta.|
| 19.4. | 2 | Ensimmäinen GitHub Release. Yksikkötestien kirjoittamista.
| 20.4. | 2 | Maksimi- ja minimiarvot ääniraudan ja metronomin asetuksille ympäristömuuttujiksi. Metronomille mahdollisuus asettaa iskujen määrä tahdissa, jolloin metronomi painottaa tahdin ensimmäistä iskua erilaisella klikki-äänellä.
| 23.4. | 3 | Ui-luokkien refaktorointia, jotta sekä äänirauta että metronomi voivat käyttää samaa presets-näkymää. Työkalunäkymille yhteinen yliluokka.
| 24.4. | 2 | Toteutus metronomin esiasetusten tallentamiselle, lataamiselle ja poistamiselle.
| 25.4 | 3 | SQLite-tietokannan käyttöönotto ääniraudan ja metronomin esiasetusten tallentamiseen.
| 1.5 | 2 | POC-toteutus sävelnimen laskemiselle annetun frekvenssin perusteella.
| 2.5 | 4 | Sävelnimen generoimisesta vastaavan NoteAnalyzer-luokan toteutus ja liittäminen sovellukseen. Yksikkötestit uudelle luokalle.
| 6.5 | 1 | Lisätty myös beats per bar-arvo tallentumaan mukaan metronomin esiasetuksiin.
| 7.5 | 5 | Esiasetusnäkymän nappi-alueet vieritettäviksi vierityspalkin avulla. (Tähän meni suhteettoman paljon aikaa.)
| 8.5 | 5 | Tallennetut esiasetukset muokattaviksi. Tallennusnappeja on nyt kaksi: Save as new ja Update, joista jälkimmäinen päivitää aktiivisen esiasetuksen.
| 10.5 | 1 | Iskuyksikön poistaminen metronomin parametrien joukosta (tarpeeton metronoin nykytoteutuksessa).
| 11.5 | 4 | Parempi toteutus esiasetusnapin aktiivisuustilan asettamiselle (päivittäminen tuhoamisen ja uudelleenluomisen sijaan aiheuttaa vähemmän vilkkumista). Pientä metronomin ja käyttöliittymän viilausta.
| 12.5 | 2 | Pylint-virheiden korjausta, mikä myös johti metronomin callback-funktion pilkkomiseen pienempiin osiin.
| 13.5 | 1 | Puuttuvan docstring-dokumentaation kirjoittamista.
| 14.5 | 4 | Viimeiset yksikkötestit. Pieniä toiminnallisuuksien viilauksia. Dokumentaatiodokumenttien päivittämistä.
| 15.5 | 2 | Viime tingan muutos esiasetusnapin valituksi merkitsemisessä (edellinen versio ei toiminutkaan odotetusti Linux-ympäristössä.) Dokumentaation viimeistely.
| yht | 98 | |
