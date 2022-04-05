# Musictools

Sovellus sisältää muutamia muusiikin harrastajalle hyödyllisiä työkaluja, kuten viritysäänen tuottavan digitaalisen **ääniraudan** ja **metronomin**.

## Python-versio

Sovelluksen toimivuus on testattu Python-versiolla 3.8.

## Dokumentaatio

- [Vaatimusmäärittely](/musictools/dokumentaatio/vaatimusmaarittely.md) 
- [Työaikakirjanpito](/musictools/dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](/musictools/dokumentaatio/changelog.md)

## Sovelluksen asentaminen ja käynnistäminen

1. Asenna sovelluksen riippuvuudet komentoriviltä komennolla

```bash
poetry install
```

2. Käynnistä sovellus komennolla

```bash
poetry run invoke start
```

## Muut komentorivitoiminnot

### Testaus

Suorita automaattiset testit komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Generoi testikattavuusraportti komennolla:

```bash
poetry run invoke coverage-report
```

Generoitu raportti löytyy sovelluksen juurihakemistoon syntyvästä hakemistosta _htmlcov_.
Tarkastele raporttia avamalla tiedosto _index.html_ selaimeen.

