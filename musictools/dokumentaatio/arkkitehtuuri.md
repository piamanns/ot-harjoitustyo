# Arkkitehtuurikuvaus

## Sovelluslogiikka

### Keskeiset luokat:
```mermaid
classDiagram
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
    class Metronome{
    }
    class MetrPreset{
    }    
```
### Pakkaus- ja luokkkaavio:
![Sovelluksen pakkaus- ja luokkarakenne](./kuvat/musictools_pakkaus_luokat.png)


## Päätoiminnallisuudet:

### Viritysäänen asettaminen:
```mermaid
sequenceDiagram
    actor User
    participant UI
    participant MusictoolsService
    User->>UI: enter frequency and click "Set"-button
    UI->>MusictoolsService: tfork_set_freq(440.0)
    MusictoolsService->>TuningFork: set_frequency(440.0)
```

### Viritysäänen tallentaminen:
```mermaid
sequenceDiagram
    actor User
    participant UI
    participant MusictoolsService
    participant TfPresetRepository
    participant preset
    User->>UI: enter frequency and click "Save"-button
    UI->>MusictoolsService: tfork_save_preset(440.0, "A")
    MusictoolsService->>preset: TfPreset(440.0, "A")
    MusictoolsService->>TfPresetRepository: save(preset):
    UI->>MusictoolsService: tfork_get_presets()
    MusictoolsService->>TfPresetRepository: get_all()
    TfPresetRepository-->>MusictoolsService: presets
    MusictoolsService-->>UI: presets
    UI->>UI: update_preset_views()
```
