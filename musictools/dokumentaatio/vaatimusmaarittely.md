# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus sisältää muutamia musiikin harrastajalle tarpeellisia työkaluja: ääniraudan, metronomin, ja ajan salliessa, mahdollisuuden pienten musikaalisten muistiinpanojen tallentamiseen.

## Käyttöliittymäluonnos

Sovellus avautuu näkymään, jossa työkalujen peruskäyttöliittymänäkymät ovat esillä rinnakkain.  
Tallennettujen työkalukohtaisten esiasetusten hallinnointiin liittyvät näkymät avautuvat nappia painamalla.

![Sovelluksen aloitusnäkymän alustava hahmotelma](./kuvat/musictools_ui_sketch.png)

## Perusversion toiminnallisuus

### Elektroninen äänirauta

- Käyttäjä voi valita viritysäänen. Viritysääni asetetaan kirjoittamalla haluttu taajuus syötekenttään tai painamalla esiasetusnappia. 
- Käyttäjä voi käynnistää ja pysäyttää viritysäänen.
- Käyttäjä voi tallentaa ja ladata ääniraudan esiasetuksia.
- Käyttäjä voi myös muokata tai kokonaan poistaa tallennettuja esiasetuksia.

### Metronomi

- Käyttäjä voi asettaa tempon kirjoittamalla bpm-arvon syötekenttään tai painamalla esiasetusnappia.
- Käyttäjä voi asettaa iskujen määrän tahdissa. Metronomi painottaa tahtien ykkösiskuja toisenlaisella tikitysäänellä.
- Käyttäjä voi käynnistää ja pysäyttää metronomin.
- Käyttäjä voi tallentaa ja ladata metronomin esiasetuksia. 
- Käyttäjä voi myös muokata tai kokonaan poistaa tallennettuja esiasetuksia.

## Jatkokehitysideoita

Ajan salliessa perusversiota voidaan laajentaa esimerkiksi seuraavilla toiminnallisuuksilla:

### Kaikki työkalut

- Sovellus muistaa tilan, johon työkalut jätettiin, kun sovellus suljettiin. Kun sovellus käynnistetään uudestaan, työkalut avautuvat samaan tilaan.

### Elektroninen äänirauta

- Käyttäjä voi asettaa viritysäänen soimisajan
- Käyttäjä voi muokata ääniraudan ääntä mieleisekseen
- Käyttäjä voi muokata sovelluksen esiasetukselle automaattisesti luomaa nimeä

### Metronomi

- Metronomi laskee bpm-arvon käyttäjän naputtaman tahdin perusteella
- Metronomin visualisonti, joka auttaa hahmottamaan tahtia myös silloin, kun metronomia ei oman soiton takia kuule
- Käyttäjä voi valita, kuinka monta tahtia metronomi tikittää
- Käyttäjä voi asettaa metronomille halutun pituisen intron, joka eroaa äänensävyltään varsinaisesta metronomiäänestä
- Käyttäjä voi vaihtaa metronomin tikitysääntä
- Käyttäjä voi muokata sovelluksen esiasetukselle automaattisesti luomaa nimeä
- Käyttäjä voi asettaa pulssiyksikön ja/tai valita tahtilajin

### Musikaalinen muistiinpano

- Käyttäjä voi helposti nauhoittaa ja tallentaa lyhyen musikaalisen idean 

