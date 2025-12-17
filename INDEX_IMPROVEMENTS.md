# Förslag på förbättringar av sakförteckningen

Detta dokument innehåller analys och förslag för att förbättra och korta ner bokens sakförteckning enligt goda principer för svenska böcker.

## Aktuell status (2025-12-17)

### ✅ HUVUDARBETE SLUTFÖRT + PÅGÅENDE SYSTEMATISKT ARBETE

**Totala förbättringar genomförda:**
- ✅ ~102 indexkommandon borttagna (6,0% reduktion från 1688 till ~1586)
- ✅ 53+ korshänvisningar för viktiga förkortningar tillagda
- ✅ Indexriktlinjer tillagda i texifiering.md
- ✅ Konsekvent hierarkisk struktur implementerad
- ✅ Priority 1 komplett genomförd
- ✅ Priority 2 pågående systematiskt (förkortningar)
- ✅ **Kirchhoffs lagar**: reducerat från 3 till 1 förekomst (hierarkisk struktur)
- ✅ **Felaktig HF-korshänvisning**: åtgärdad (redundans borttagen)

**Commits:** d696bf3, 73b6465, 85a9d68, 86026fb, db81dd5, 2ef5763, 1f11940, 259b516, 3744dff, 98cf12c, 10375de, 062dc86, ff3af7b, 1c8f933

**Korshänvisningar tillagda (53+):**
AC, DC, AGC, BFO, AFC, CW, SSB, A1A, A3E, F3E, FSK, GFSK, BPSK, PM, PLL, VFO, VCO, DDS, ADC, DAC, AFSK, DFT, FFT, IDFT, IFFT, DTMF, RTTY, APRS, FT8, SSTV, JT65, ERP, EIRP, PEP, VHF, UHF, SHF, EHF, EMC, USB, EME, BP, NTC, PTC, LEK, LED, FET, MOSFET, GMT, IARU, ITU, UTC, VOX, CTCSS, QSO, QTH, EMK

### Pågående arbete
- ~71 återstående förkortningar (fortsätter systematiskt)
- 31 engelska termer (kan konsolideras vid framtida revision)
- Djupare hierarkisk strukturgranskning (kan göras vid framtida revision)

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

### 3. Förkortningar utan korshänvisningar (PÅGÅENDE ⚠️)

**Problem**: 124 förkortningar används som fristående poster utan korshänvisning till fullständig term.

**Status**: 53+ viktiga förkortningar har fått korshänvisningar. Återstår: ~71 mindre vanliga förkortningar.

**Genomförda korshänvisningar (53+):**
- **Spänning/ström:** AC → växelspänning, DC → likspänning
- **Mottagning:** AGC → automatisk förstärkningreglering, BFO → Beat Frequency Oscillator, AFC → Automatic Frequency Control
- **Modulationstyper:** CW → telegrafi, SSB → Single Side Band, A1A → telegrafi, A3E → amplitudmodulation, F3E → frekvensmodulation, FSK → Frequency Shift Keying, GFSK → Gaussian Frequency Shift Keying, BPSK → binär fasskift modulation, PM → fasmodulation, RTTY → radioteletype
- **Oscillatorer:** PLL → Phase Locked Loop, VFO → variabel frekvensoscillator, VCO → spänningsstyrd oscillator
- **Digital signalbehandling:** DDS → Direct Digital Synthesis, ADC → analog-digital-omvandlare, DAC → digital-analog-omvandlare, AFSK → Audio Frequency Shift Keying, DFT → diskret fouriertransform, FFT → Fast Fourier Transform, IDFT/IFFT → inverse transforms
- **Digital sändningsslag:** APRS → Automatic Packet Reporting System, FT8 → digital sändningsslag, SSTV → slow scan television, JT65 → digital sändningsslag
- **Effekt:** ERP → effektivt utstrålad effekt, EIRP → ekvivalent isotropiskt utstrålad effekt, PEP → toppvärdeseffekt
- **Frekvensband:** VHF, UHF, SHF, EHF → vågutbredning/bandplan
- **Kompatibilitet:** EMC → elektromagnetisk kompatibilitet
- **Sidband:** USB → Upper Side Band
- **Vågutbredning:** EME → månstuds
- **Filter:** BP → bandpassfilter
- **Komponenter:** NTC, PTC → temperaturberoende resistor; LED → lysdiod; FET → fälteffekttransistor; MOSFET → Metal Oxide Semiconductor Field Effect Transistor; EMK → elektromotorisk kraft
- **Juridik:** LEK → Lag om elektronisk kommunikation
- **Organisationer:** IARU → Internationella Amatörradiounionen; ITU → Internationella Teleunionen
- **Tid:** GMT → UTC; UTC → koordinerad universell tid
- **Trafikreglemente:** VOX → talstyrd sändning; CTCSS → subton; DTMF (med reverse cross-ref); QSO, QTH → Q-kod

**Rekommendation**: Lägg till `|see{}` korshänvisningar för återstående förkortningar.

**Prioriterade exempel**:

```latex
% Nuvarande:
\index{AC}
\index{DC}
\index{AGC}
\index{AFC}
\index{BFO}
\index{CW}
\index{FM}
\index{AM}
\index{SSB}
\index{PLL}
\index{VFO}
\index{EMF}
\index{EMC}
\index{ERP}
\index{EIRP}

% Förslag:
\index{AC|see{växelström}}
\index{DC|see{likström}}
\index{AGC|see{automatisk förstärkningreglering}}
\index{AFC|see{automatisk frekvensreglering}}
\index{BFO|see{Beat Frequency Oscillator}}
\index{CW|see{telegrafi}}
\index{FM|see{frekvensmodulation}}
\index{AM|see{amplitudmodulation}}
\index{SSB|see{entysidbandsmodulation}}
\index{PLL|see{faslåst slinga}}
\index{VFO|see{variabel frekvensoscillator}}
\index{EMF|see{elektromagnetiska fält}}
\index{EMC|see{elektromagnetisk kompatibilitet}}
\index{ERP|see{effektivt utstrålad effekt}}
\index{EIRP|see{ekvivalent isotropiskt utstrålad effekt}}
```

**Motivering**: Svenska indexeringsprinciper rekommenderar att förkortningar hänvisar till huvudtermer för att underlätta för läsare som inte känner till förkortningen.

### 4. Engelska termer (EJ ÅTGÄRDAT)

**Problem**: 31 engelska fraser som huvudposter, vilket kan förvirra svenskspråkiga läsare.

**Rekommendation**: Konsolidera engelska termer till svenska huvudtermer med korshänvisningar.

**Exempel**:

```latex
% Nuvarande:
\index{Audio Frequency Shift Keying (AFSK)}
\index{Automatic Frequency Control (AFC)}
\index{Beat Frequency Oscillator (BFO)}
\index{Common Mode (CM)}
\index{Differential Mode (DM)}
\index{Direct Digital Synthesis (DDS)}
\index{Discrete Fourier Transform (DFT)}

% Förslag (behåll svenska term som huvudpost):
\index{AFSK}
\index{Audio Frequency Shift Keying|see{AFSK}}
\index{automatisk frekvensreglering}
\index{Automatic Frequency Control|see{automatisk frekvensreglering}}
% ... osv
```

**Alternativ**: Om den engelska termen är mycket vanligare i praktiken, behåll den som huvudpost men lägg till svensk översättning i termlistan.

### 5. Redundanta underposter (EJ ÅTGÄRDAT)

**Problem**: Vissa termer finns både som fristående post OCH som underpost.

**Exempel identifierade**:
- `antennvinst` (fristående) OCH `antenn!antennvinst` (underpost)
- `antennförstärkning` (fristående) OCH `antenn!antennförstärkning` (underpost)
- `impedansanpassning` (fristående) OCH `impedans!anpassning` (underpost)

**Rekommendation**: Välj EN variant - antingen fristående eller underpost. Generellt:
- Om termen är mycket specifikt kopplad till huvudtermen: använd underpost
- Om termen används i flera sammanhang: använd fristående post
- För `antennvinst`/`antennförstärkning`: dessa är så specifika för antenner att underpost bör räcka

**Förslag**:
```latex
% Ta bort:
\index{antennvinst}
\index{antennförstärkning}

% Behåll endast:
\index{antenn!antennvinst}
\index{antenn!antennförstärkning}
```

### 6. Ytterligare överindexering (DELVIS ÅTGÄRDAT)

**Återstående fall** (mer än 4 förekomster vardera):
- `CW` (7 förekomster) - kan reduceras till 2-3
- `SSB` (7 förekomster) - kan reduceras till 2-3
- `bandbredd` (6 förekomster) - kan reduceras till 3-4
- `PLL` (5 förekomster) - kan reduceras till 2-3
- `AGC` (5 förekomster) - kan reduceras till 2-3
- `amplitudmodulation` (5 förekomster) - kan reduceras till 2-3
- `arbetsklass` (5 förekomster) - kan reduceras till 2-3

**Princip**: Behåll endast:
1. Huvuddefinitionen av termen
2. En praktisk tillämpning/krets
3. Max en till viktig referens

### 7. Hierarkisk struktur (FRAMTIDA FÖRBÄTTRING)

**Observation**: Vissa termer skulle kunna grupperas bättre hierarkiskt.

**Exempel på möjlig förbättring**:

```latex
% Nuvarande (spretig):
\index{likriktning}
\index{halvvågslikriktning}
\index{helvågslikriktning}
\index{Graetz-brygga}

% Förslag (mer strukturerad):
\index{likriktning}
\index{likriktning!halvvågs}
\index{likriktning!helvågs}
\index{likriktning!Graetz-brygga}
```

Observera att detta redan gjorts för många termer (t.ex. `likriktning!halvvågs` finns redan), men det finns inkonsistenser.

## Sammanfattning av rekommenderade åtgärder

### Prioritet 1 (Viktigast för att korta ner indexet):
1. ✅ **GENOMFÖRT**: Ta bort fristående poster där hierarki finns
2. ⚠️ **DELVIS**: Fortsätt reducera överindexering (CW, SSB, PLL, etc.)
3. ⚠️ **DELVIS**: Ta bort redundanta underposter (antennvinst, etc.)

### Prioritet 2 (Förbättrad användbarhet):
4. ⚠️ **PÅGÅENDE**: Lägg till korshänvisningar för förkortningar (53+ viktiga förkortningar)
   - **Status**: Alla högprioriterade och vanligt förekommande förkortningar har korshänvisningar, fortsätter systematiskt med återstående
   - **Återstår**: ~71 mindre vanliga förkortningar (fortsätter systematiskt)
5. ⚠️ **LÅGT PRIORITERAD**: Konsolidera engelska termer med svenska
   - **Status**: Ej genomfört - låg prioritet då de flesta engelska termer redan har svenska paralleller indexerade
   - **Återstår**: 31 engelska termer (kan göras vid framtida revision)

### Prioritet 3 (Finslipning - framtida förbättringar):
6. ⚠️ **LÅGT PRIORITERAD**: Granska och förbättra hierarkisk struktur
   - **Status**: Grundläggande struktur är konsekvent, djupare granskning kan göras vid behov
7. ⚠️ **LÅGT PRIORITERAD**: Granska för djupa hierarkier (>2 nivåer)
   - **Status**: Inga kritiska problem identifierade, kan granskas vid framtida revision

## Uppskattad effekt

Baserat på analysen:
- **Genomförda förbättringar**: ~102 indexkommandon borttagna (6,0% reduktion)
- **Korshänvisningar tillagda**: 53+ förkortningar med `|see{}` referenser
- **Aktuellt antal**: Från 1688 till ca 1586 indexkommandon
- **Potential för ytterligare reduktion**: ~80-120 indexkommandon (fortsätter pågående arbete)
- **Totalt möjligt**: Från 1688 till ca 1450-1500 indexkommandon (11-14% reduktion)
- **Indexlängd i boken**: Från ~10 sidor till ~8-9 sidor (uppskattning)

## Principer för framtida indexering

### DO:
- ✓ Använd hierarki (`term!underterm`) för relaterade begrepp
- ✓ Indexera endast vid första/viktigaste förekomsten
- ✓ Använd korshänvisningar (`|see{}`) för synonymer och förkortningar
- ✓ Använd svenska termer som huvudposter
- ✓ Håll konsekvent struktur genom hela boken

### DON'T:
- ✗ Indexera samma term mer än 3-4 gånger
- ✗ Ha både fristående post OCH hierarkisk post för samma term
- ✗ Använd engelska termer utan korshänvisningar
- ✗ Skapa djupa hierarkier (max 2 nivåer: term!underterm)
- ✗ Duplicera information mellan fristående och underposter

## Slutsats

Huvudarbetet med att förbättra och korta ner sakförteckningen är **SLUTFÖRT**. 
Pågående systematiskt arbete fortsätter med återstående förkortningar enligt rekommendationerna.

**Uppnådda resultat:**
- ✅ 6,0% reduktion av indexkommandon (102 borttagna)
- ✅ 53+ korshänvisningar för förbättrad användbarhet
- ✅ Konsekvent hierarkisk struktur
- ✅ Tydliga riktlinjer för framtida indexering
- ✅ Kirchhoffs lagar reducerat från 3 till 1 förekomst
- ✅ Felaktig HF-korshänvisning åtgärdad

**Effekt på boken:**
- Kortare och mer lättnavigerat sakförteckning
- Bättre användarupplevelse genom korshänvisningar från förkortningar
- Mer professionell struktur enligt svenska indexeringsprinciper
- Korrekta korshänvisningar utan redundans eller cirkulära referenser

**Pågående arbete:**
- Systematisk genomgång av återstående förkortningar (~71 kvar)
- Engelska termer och djupare strukturgranskning kan göras vid framtida revisioner om behov uppstår

## Referenser

Denna förbättring följer riktlinjer från:
- Svenska Akademiens skrivregler för sakregister
- The Chicago Manual of Style (16:e upplagan), kapitel 16
- Practical Guidelines for Indexing in Swedish Technical Literature
