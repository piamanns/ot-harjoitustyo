```mermaid
classDiagram
    Monopoli "1" -- "2" Noppa
    Monopoli "1" -- "2..8" Pelaaja
    Pelaaja "1" -- "*" Raha
    Monopoli "1" -- "1" Pelilauta
    Monopoli "1" -- "1" Aloitus
    Monopoli "1" -- "1" Vankila
    Pelilauta "1" -- "1" Aloitus
    Pelilauta "1" -- "1" Vankila
    Pelilauta "1" -- "3" Sattuma
    Pelilauta "1" -- "3" Yhteismaa
    Pelilauta "1" -- "4" Asema
    Pelilauta "1" -- "2" Laitos
    Pelilauta "1" -- "22" Katu
    Ruutu "1" -- "1" Ruutu
    Ruutu "1" -- "2..8" Pelinappula
    Pelaaja "1" -- "1" Pelinappula
    Aloitus --|> Ruutu
    Vankila --|> Ruutu
    Sattuma --|> Ruutu
    Yhteismaa --|> Ruutu
    Asema --|> Ruutu
    Laitos --|> Ruutu
    Katu --|> Ruutu
    Sattuma ..> Kortti
    Yhteismaa ..> Kortti
    Kortti "*" -- "1" Toiminto
    Ruutu "*" -- "1" Toiminto
    Pelaaja "1" -- "*" Asema
    Pelaaja "1" -- "*" Laitos
    Pelaaja "1" -- "*" Katu 
  
  class Katu {
      nimi
  }  
 ```
