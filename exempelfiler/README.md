# Exempelfiler för KonCEPT

Detta är en samling exempel- och övningsfiler som kan användas tillsammans med boken KonCEPT för amatörradiocertifikat.

## GNU Radio-exempel

GNU Radio är en gratis programvara för att simulera och experimentera med radiosystem.
Läs mer på [gnuradio.org](https://gnuradio.org).

### Filerna

- `am_modulation.grc` - Exempel på amplitudmodulation (AM)
- `fm_modulation.grc` - Exempel på frekvensmodulation (FM)

### Hur man använder

1. Installera GNU Radio på din dator (finns för Linux, Windows och macOS)
2. Öppna en `.grc`-fil i GNU Radio Companion
3. Klicka på "Run" för att starta simuleringen
4. Experimentera genom att ändra parametrar som:
   - Modulationsfrekvens
   - Bärvågsfrekvens
   - Modulationsdjup (för AM)
   - Frekvensdeviation (för FM)

## SPICE-exempel

SPICE är en standard för kretssimuleringar som används av många program, t.ex.:
- LTspice (gratis från Analog Devices)
- ngspice (öppen källkod)
- iCircuit (iOS/Android-app)

### Filerna

- `voltage_divider.cir` - Enkel spänningsdelare som demonstrerar Ohms lag
- `rc_lowpass_filter.cir` - RC-lågpassfilter
- `lc_resonant_circuit.cir` - Parallell LC-resonanskrets

### Hur man använder

1. Installera ett SPICE-kompatibelt program (t.ex. LTspice eller ngspice)
2. Öppna en `.cir`-fil i programmet
3. Kör simuleringen för att se resultaten
4. Experimentera genom att ändra komponentvärden

## Licens

Alla exempel är licensierade under Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0), samma som huvudboken.

## Bidrag

Om du har skapat egna exempel som du vill dela med andra, är du välkommen att bidra till projektet genom att skapa en pull request på [GitHub](https://github.com/SverigesSandareamatorer/SSA-Akademin).
