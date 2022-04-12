# Changelog

## Viikko 3

- Lisätty ensimmäinen versio ääniraudasta, joka tuottaa viritysäänen siniaallon avulla.
- Toteutettu ääniraudalle yksinkertainen graafinen käyttöliittymä, jossa viritysäänen taajuden voi asettaa joko tekstikentään syöttämällä tai esiasetettuja nappeja painamalla.
- Testattu, että ääniraudan viritysäänen taajuuden muuttaminen toimii.

## Viikko 3
- Lisätty käyttäjälle mahdollisuus tallentaa ja poistaa esiasetettuja viritysääniä.
- Kun sovellus käynnistyy, tallennetut viritysäänet näkyvät nappeina käyttöliittymässä.
- Esiasetuksille luotu oma TfPresets-luokka. 
- Asetukset tallenneetaan toistaiseksi CSV-tiedostoon.
- Sovelluslogiikka eriytetty MusictoolsServices-luokkaan.
- Graafista käyttöliittymää refaktoroitu ja laajennettu. 
- Jos käyttäjä syöttää taajuden virheellisessä muodossa, käyttöliittymässä näytetään virheviesti. 
