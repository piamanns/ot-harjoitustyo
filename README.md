# Musictools

Sovellus sisältää kaksi muusiikin harrastajalle hyödyllistä työkalua: viritysäänen tuottavan digitaalisen **ääniraudan** ja **metronomin**.

[Viikon 5 GitHub Release](https://github.com/piamanns/ot-harjoitustyo/releases)

## Python-versio

Sovelluksen toimivuus on testattu Python-versiolla 3.8.

## Dokumentaatio

- [Vaatimusmäärittely](/musictools/dokumentaatio/vaatimusmaarittely.md) 
- [Arkkitehtuurikuvaus](musictools/dokumentaatio/arkkitehtuuri.md)
- [Työaikakirjanpito](/musictools/dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](/musictools/dokumentaatio/changelog.md)

## Sovelluksen asentaminen ja käynnistäminen

1. Siirry kansioon musictools:

```bash
cd musictools
```

2. Asenna sovelluksen riippuvuudet komentoriviltä komennolla

```bash
poetry install
```

2. Käynnistä sovellus komennolla

```bash
poetry run invoke start
```

## Muut komentorivitoiminnot

### Testaus

Suorita automaattiset testit komennolla

```bash
poetry run invoke test
```

### Testikattavuus

Generoi testikattavuusraportti komennolla

```bash
poetry run invoke coverage-report
```

Generoitu raportti löytyy sovelluksen juurihakemistoon syntyvästä hakemistosta _htmlcov_.  
Tarkastele raporttia avamalla tiedosto _index.html_ selaimeen.

### Pylint

Suorita koodin laatutarkistus kommennolla

```bash
poetry run invoke lint
```

Tehtävät tarkistukset on määritelty tiedostossa [.pylintrc](./musictools/.pylintrc)

## Ulkoiset kirjastot

Sovelluksen käyttöliitymä on toteutettu Tkinterillä.

Äänien toistamiseen sovellus käyttää modulia [sounddevice](https://python-sounddevice.readthedocs.io/en/0.4.4/index.html). Myös viritysääni generoidaan sounddevicen avulla.

Metronomin klikkiääni luetaan äänitedostosta [SoundFile-kirjaston](https://python-soundfile.readthedocs.io/en/0.10.3post1/) avulla.

## Ikonit

[Metronome](https://icons8.com/icon/ZWdlYSmKyyg3/metronome) and [Tuning Fork](https://icons8.com/icon/9gdSTst8LEgu/tuning-fork) icons by [Icons8](https://icons8.com)

