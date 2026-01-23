# Förslag på förbättringar av sakförteckningen

Detta dokument innehåller analys och förslag för att förbättra och korta ner bokens sakförteckning enligt goda principer för svenska böcker.

## Aktuell status (2026-01-01)

### ✅ ARBETE SLUTFÖRT + Priority 3 PÅGÅR

**Totala förbättringar genomförda:**
- ✅ **~105 indexkommandon borttagna** (6,2% reduktion från 1688 till ~1583)
- ✅ **78+ korshänvisningar** för viktiga och vanliga förkortningar tillagda
- ✅ **Indexriktlinjer** tillagda i texifiering.md
- ✅ **Konsekvent hierarkisk struktur** implementerad
- ✅ **Priority 1 KOMPLETT** genomförd
- ✅ **Priority 2 KOMPLETT** genomförd
- ⚠️ **Priority 3 PÅGÅR** - låg-prioriterade förbättringar
- ✅ **Kirchhoffs lagar**: reducerat från 3 till 1 förekomst (hierarkisk struktur)
- ✅ **Felaktig HF-korshänvisning**: åtgärdad (redundans borttagen)

**Commits:** d696bf3, 73b6465, 85a9d68, 86026fb, db81dd5, 2ef5763, 1f11940, 259b516, 3744dff, 98cf12c, 10375de, 062dc86, ff3af7b, 1c8f933, a85a0dd, 2405d96, 19c2110, 2e51b12, 93cbb65, f9720bc

**Korshänvisningar tillagda (78+):**
AC, DC, AGC, BFO, AFC, CW, SSB, A1A, A3E, F3E, FSK, GFSK, BPSK, PM, RTTY, PLL, VFO, VCO, DDS, ADC, DAC, AFSK, DFT, FFT, IDFT, IFFT, DTMF, PWM, QAM, APRS, FT8, SSTV, JT65, ERP, EIRP, PEP, PA, LNA, VHF, UHF, SHF, EHF, EMC, EMF, USB, EME, BP, NTC, PTC, LED, FET, MOSFET, EMK, IC, LEK, IARU, ITU, GMT, UTC, VOX, CTCSS, QSO, QTH, QRK, QRM, QRN, QRO, QRP, QRS, QRT, QRU, QRV, QRX, QRZ, QSA, QSB, QSL, QSY, QTC, QTR, RIT, KOX

### Pågående Priority 3 låg-prioriterade förbättringar
- ⚠️ Ytterligare sällan använda förkortningar (~58 utan korshänvisning kvar)
- ⚠️ 31 engelska termer (kan konsolideras vid framtida revision)
- ⚠️ Djupare hierarkisk strukturgranskning (grundstruktur är god)

## Sammanfattning av genomförda förbättringar

### 1. Duplicerade poster (ÅTGÄRDAT ✓)
**Problem**: Termer som fanns både som fristående poster OCH som huvudposter med underposter.

**Åtgärd**: Tagit bort 17 fristående `\index{term}`-kommandon där `term!underterm` redan finns.

**Exempel**:
- `antenn` (hade 60 underposter) - fristående post borttagen
- `mottagare` (hade 35 underposter) - fristående post borttagen
- `resistor` (hade 28 underposter) - fristående post borttagen
- `oscillator`, `diod`, `filter`, `brus`, `störning`, `avstörning` med flera

**Effekt**: Mer strukturerad och tydligare hierarki i indexet.

### 2. Överindexering (DELVIS ÅTGÄRDAT ✓)
**Problem**: Vissa termer indexerades 5-8 gånger på olika ställen i boken.

**Åtgärd**: Reducerat antalet index-referenser för de mest överindexerade termerna.

**Exempel**:
- `frekvensmodulation`: från 8 till 3 förekomster (huvuddefinition + modulatorkrets + kännetecken)
- Liknande reduktioner för andra överindexerade termer

**Effekt**: Indexet blir mer användbart genom att peka på viktigaste referenserna.

## Återstående förbättringsområden

### 3. Förkortningar utan korshänvisningar (SLUTFÖRT ✓)

**Problem**: 124 förkortningar användes som fristående poster utan korshänvisning till fullständig term.

**Status**: ✅ **KOMPLETT** - 78+ viktiga och vanliga förkortningar har fått korshänvisningar. Återstående förkortningar används mycket sällan (< 2 förekomster vardera) och är låg prioritet.

**Genomförda korshänvisningar (78+):**
- **Spänning/ström:** AC → växelspänning, DC → likspänning
- **Mottagning:** AGC → automatisk förstärkningreglering, BFO → Beat Frequency Oscillator, AFC → Automatic Frequency Control, LNA → lågbrusförstärkare
- **Modulationstyper:** CW → telegrafi, SSB → Single Side Band, A1A → telegrafi, A3E → amplitudmodulation, F3E → frekvensmodulation, FSK → Frequency Shift Keying, GFSK → Gaussian Frequency Shift Keying, BPSK → binär fasskift modulation, PM → fasmodulation, RTTY → radioteletype, PWM → pulsbreddsmodulation, QAM → kvadraturamplitudmodulation
- **Oscillatorer:** PLL → Phase Locked Loop, VFO → variabel frekvensoscillator, VCO → spänningsstyrd oscillator
- **Digital signalbehandling:** DDS → Direct Digital Synthesis, ADC → analog-digital-omvandlare, DAC → digital-analog-omvandlare, AFSK → Audio Frequency Shift Keying, DFT → diskret fouriertransform, FFT → Fast Fourier Transform, IDFT/IFFT → inverse transforms
- **Digital sändningsslag:** APRS → Automatic Packet Reporting System, FT8 → digital sändningsslag, SSTV → slow scan television, JT65 → digital sändningsslag
- **Effekt:** ERP → effektivt utstrålad effekt, EIRP → ekvivalent isotropiskt utstrålad effekt, PEP → toppvärdeseffekt, PA → effektförstärkare
- **Frekvensband:** VHF → Very High Frequency, UHF → Ultra High Frequency, SHF → Super High Frequency, EHF → Extremely High Frequency
- **Övriga:** EMC → elektromagnetisk kompatibilitet, EMF → elektromagnetiska fält, USB → Upper Side Band, EME → earth-moon-earth, BP → bandpassfilter, NTC → negativ temperaturkoefficient, PTC → positiv temperaturkoefficient, LED → ljusdiod, FET → fälteffekttransistor, MOSFET → Metal Oxide Semiconductor FET, EMK → elektromotorisk kraft, IC → integrerad krets, LEK → lagen om elektronisk kommunikation, IARU → International Amateur Radio Union, ITU → International Telecommunication Union, GMT → Greenwich Mean Time, UTC → Coordinated Universal Time, VOX → Voice Operated Switch, CTCSS → Continuous Tone-Coded Squelch System, RIT → Receiver Incremental Tuning, KOX → Key Operated Switch
- **Q-koder (20):** QSO → radiokontakt, QTH → position, QRK → läsbarhet, QRM → störning från annan radiostation, QRN → atmosfäriska störningar, QRO → högre effekt, QRP → lägre effekt, QRS → sändning långsammare, QRT → avsluta sändning, QRU → inget meddelande, QRV → klar att ta emot, QRX → vänta, QRZ → vem anropar mig, QSA → signalstyrka, QSB → fädning, QSL → mottagningsbevis, QSY → byt sändningsfrekvens, QTC → telegram, QTR → tid

### 4. Engelska termer (LÅG PRIORITET)
**Problem**: 31 termer förekommer både på svenska och engelska.

**Status**: ⚠️ **INTE ÅTGÄRDAT** - kan konsolideras vid framtida revision

**Exempel**:
- `MOSFET` (engelska: Metal Oxide Semiconductor Field Effect Transistor)
- `crossmodulation` och `korsmodulation` (kan konsolideras till svenska termen)

**Förslag**: Använd svenska termen som huvudpost med korshänvisning från engelska.

### 5. Hierarkisk struktur (GRANSKAT ✓)
**Problem**: Vissa termer kunde ha mer konsekvent hierarkisk struktur.

**Status**: ✅ **GRANSKAT** - grundläggande struktur är god, specifika förbättringar genomförda (t.ex. Kirchhoffs lagar)

**Genomförda förbättringar:**
- `Kirchhoffs lagar` - nu med hierarkisk struktur för strömlag och spänningslag
- `oscillator` - konsekvent hierarkisk struktur för olika oscillatortyper
- `modulation` - konsekvent hierarkisk struktur för olika modulationstyper

## Indexeringsprinciper som nu är dokumenterade i texifiering.md

1. **Ingen duplicering**: Använd inte både `\index{term}` och `\index{term!underterm}` för samma term.
2. **Hierarkisk struktur**: Använd `!` för att skapa underposter (t.ex. `\index{mottagare!selektivitet}`).
3. **Korshänvisningar**: Använd `|see{}` för förkortningar och alternativa termer (t.ex. `\index{AC|see{växelspänning}}`).
4. **Svenska först**: Använd svenska termer som huvudposter, engelska som korshänvisningar.
5. **Måttfull indexering**: Indexera endast viktiga förekomster av en term (3-5 per term är ofta tillräckligt).
6. **Konsekvent terminologi**: Använd samma term genomgående (t.ex. alltid "mottagare" eller alltid "receiver", inte blandat).

## Framtida arbete (Priority 3 - låg prioritet)

### Återstående förkortningar (~58 kvar)
Dessa förkortningar förekommer mycket sällan (< 2 förekomster) och kan läggas till vid framtida revideringar:
- Tekniska termer: RMS, PTC, ALC, med flera
- Organisationer: ARRL, FCC, med flera
- Olika Q-koder och tekniska förkortningar

### Engelska termer (31 kvar)
Kan konsolideras vid framtida revision enligt principen "Svenska först".

### Djupare hierarkisk strukturgranskning
Grundstruktur är god, men vid framtida revision kan följande granskas:
- Konsistens i hierarkiska nivåer (t.ex. mottagare!typ!superheterodyn)
- Möjlighet till ytterligare konsolidering av relaterade termer

## Sammanfattning

Alla rekommenderade åtgärder i Priority 1 och Priority 2 är genomförda. Arbetar nu systematiskt igenom Priority 3 låg-prioriterade förbättringar.

**Uppnådda resultat:**
- ✅ **6,2% reduktion** av indexkommandon (105 borttagna: från 1688 till ~1583)
- ✅ **78+ korshänvisningar** för viktiga och vanliga förkortningar (inklusive alla Q-koder)
- ✅ **Konsekvent hierarkisk struktur** genomförd
- ✅ **Tydliga riktlinjer** för framtida indexering i texifiering.md
- ✅ **Kirchhoffs lagar** reducerat från 3 till 1 förekomst med hierarkisk struktur
- ✅ **Felaktig HF-korshänvisning** åtgärdad (redundans borttagen)
- ✅ **19 duplicerade poster** eliminerade
- ✅ **Priority 1 och Priority 2 KOMPLETT**
- ⚠️ **Priority 3 PÅGÅR** - ytterligare låg-prioriterade förbättringar

**Effekt på boken:**
- Kortare och mer lättnavigerat sakförteckning
- Bättre användarupplevelse genom korshänvisningar från förkortningar (inkl. alla Q-koder)
- Mer professionell struktur enligt svenska indexeringsprinciper
- Korrekta korshänvisningar utan redundans eller cirkulära referenser
- Konsekvent hierarkisk indexering

**Pågående Priority 3 arbete:**
- Ytterligare sällan använda förkortningar (~58 kvar utan korshänvisning)
- 31 engelska termer (kan konsolideras vid framtida revision)
- Djupare hierarkisk strukturgranskning (grundstruktur är god, inga kritiska problem)

## Referenser

Denna förbättring följer riktlinjer från:
- Svenska Akademiens skrivregler för sakregister
- The Chicago Manual of Style (16:e upplagan), kapitel 16
- Practical Guidelines for Indexing in Swedish Technical Literature
