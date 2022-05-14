# Changelog

## Viikko 3

- Lisätty ensimmäinen versio ääniraudasta, joka tuottaa viritysäänen siniaallon avulla.
- Toteutettu ääniraudalle yksinkertainen graafinen käyttöliittymä, jossa viritysäänen taajuden voi asettaa joko tekstikentään syöttämällä tai esiasetettuja nappeja painamalla.
- Testattu, että ääniraudan viritysäänen taajuuden muuttaminen toimii.

## Viikko 4
- Lisätty käyttäjälle mahdollisuus tallentaa ja poistaa esiasetettuja viritysääniä.
- Kun sovellus käynnistyy, tallennetut viritysäänet näkyvät nappeina käyttöliittymässä.
- Esiasetuksille luotu oma TfPresets-luokka. 
- Asetusten tallennus toistaiseksi CSV-tiedostoon.
- Sovelluslogiikka eriytetty MusictoolsServices-luokkaan.
- Graafista käyttöliittymää refaktoroitu ja laajennettu. 
- Jos käyttäjä syöttää taajuden virheellisessä muodossa, käyttöliittymässä näytetään virheviesti. 
- Lisätty useita testejä ääniraudalle sekä tallennettujen asetusten lukemisesta ja kirjoittamisesta vastaavalle TfPresetRepository-luokalle.

## Viikko 5
- Sovellukseen lisätty metronomi.
- Käyttäjä voi asettaa metronomille bpm-arvon. Jos syöte on virheellinen, käyttöliittymässä näytetään virheviesti.
- Metronomin bpm-arvoja voi tallentaa. Kun sovellus käynnistyy, tallennetut bpm-arvot näkyvät nappeina käyttöliittymässä. 
- Käyttäjä voi poistaa metronomin esisasetettuja bpm-arvoja.
- Otettu käyttöön SQLite-tietokanta ääniraudan ja metronomin esiasetusten tallentamiseen. 
- Syötteiden validointi siirretty pois käyttöliittymäluokista, äänirauta- ja metronomiluokkiin. Työkalujen maksimi- ja minimiarvot siirretty ympäristömuuttujiksi.
- UI-näkymien laaja refaktorointi. Lisätty yliluokka ToolView työkaluille. Äänirauta ja metronomi hyödyntävät nyt samaa esiasetusnäkymäluokkaa PresetsView.
- Ääniraudalle ja metronomille omat konfiguroitavat ikonit
- Lisätty yksikkötestejä metronomille sekä tallennettujen asetusten lukemisesta ja kirjoittamisesta vastaavalle MetrPresetRepository-luokalle.

## Viikko 6
- Ääniraudalle lisätty ominaisuus, joka osaa laskea ja generoida sävelnimen, joka vastaa syötettyä frekvenssiä.
- Sävelnimen generoimisesta vastaa uusi NoteAnalyzer-luokka.
- Sävelnimi näytetään äänirauta-ikonin alla frekvenssin yhteydessä.
- Sävelnimi tallennetaan myös automaattisesti frekvenssi-esiasetuksen label-tekstiksi, joka näytetään osana esiasetusnapin tekstiä.
- NoteAnalyzerin käyttämän referenssi-A:n frekvenssi on asetettavissa ympäristömuuttujan avulla.
- Lisätty NoteAnalyzerin toimintaa testaavia yksikkötestejä.

## Viikko 7
- Sovellukseen on lisätty mahdollisuus muokata ja päivittää tallennettuja esiasetuksia. Klikattuaan esiasetusnappia käyttäjä voi joko tallentaa työkalun asetuksiin tämän jälkeen tehdyt muutokset uutena esiasetuksena (Save as new) tai päivittää aktiivisen esiasetuksen (Update).
- Ääniraudan ja metronomin esiasetusnäkymille toteutettu vierityspalkilla vieritettävät alueet, jotka luodaan uuden ScrollableArea-apuluokan avulla.
- Metronomista ja sen esiasetuksista poistettu iskuyksikkö-parametri (beat unit), joka osoittautui tarpeettomaksi (sovelluksessa ei tehdä varsinaista tahtilajin valintaa).
- Lisätty yksikkötestejä tallennettujen asetusten muokkaamiselle.
