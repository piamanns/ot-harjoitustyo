```mermaid
classDiagram
    Monopoli "1" -- "1" Pelilauta
    Monopoli "1" -- "2..8" Pelaaja
    Pelaaja "1" -- "1" Pelinappula 
    Monopoli "1" -- "2" Noppa
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu
    Pelinappula "2..8" -- "1" Ruutu
```
