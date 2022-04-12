# Arkkitehtuurikuvaus

## Sovelluslogiikka

### Keskeiset luokat:
```mermaid
classDiagram
    TuningFork "1" --> "*" TfPreset
    Metronome "1" --> "*" MetrPreset
    
    class TuningFork{   
        +start()
        +stop()
        +is_active()
        +set_frequency(freq)
        +get_frequency()
    }
    
    class TfPreset{
        +id
        +freq
        +label
    }
```
### Pakkaus- ja luokkkaavio:
![Sovelluksen pakkaus- ja luokkarakenne](./kuvat/musictools_pakkaus_luokat.png)
