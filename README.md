📘 KonCEPT för amatör&shy;radio&shy;certifikat
============

[![Status för bygget av KonCEPT](https://github.com/SverigesSandareamatorer/SSA-Akademin/actions/workflows/bygg.yml/badge.svg)](https://github.com/SverigesSandareamatorer/SSA-Akademin/actions/workflows/bygg.yml)
[![Senaste releaseversionen](https://img.shields.io/github/v/release/SverigesSandareamatorer/SSA-Akademin?display_name=tag&sort=semver)](https://github.com/SverigesSandareamatorer/SSA-Akademin/releases)

Boken _KonCEPT för amatörradiocertifikat_ ges ut av
[Föreningen Sveriges Sändareamatörer](https://www.ssa.se) (SSA) i syfte att
utbilda nya radioamatörer.
Den första upplagan publicerades år&nbsp;1997 (med titeln KonCEPT för
radioamatörcertifikat) och var huvudsakligen skriven av Lennart Wiberg.
Efter 20&nbsp;år behövdes en uppdatering och att tryckas i en ny upplaga.
Detta projekt, SSA Akademin, är bland annat till för digitalisering och
uppdatering av KonCEPT som lett fram till en andra upplaga av boken.
Den tryckta boken kan köpas
[från SSA:s Hamshop](https://hamshop.ssa.se/?s=KonCEPT&post_type=product).

| :warning: **Observera** |
|:---------------------------|
| Boken och materialet som finns att läsa här är ett arbetsmaterial och ska inte användas som en färdig produkt utan endast som ett underlag för arbetet med den. |

# Ladda ner och bygg projektet

## Version

Eftersom nytt material läggs till och fel rättas allt eftersom används en
versionsnumrering som ger värdefull information åt läsaren.
Här är ett exempel på hur det kan se ut och en förklaring till vad delarna
betyder.

<pre>
koncept.2.0.0+b12345.8c04343.pdf
        │ │ │    │      └ Git commit hash
        │ │ │    └ Byggnummer
        │ │ └ Ej tryckt uppdatering
        │ └ Tryckning (med 1:a tryckning = 0)
        └ Upplaga
</pre>

## Bygg lokalt

Du kan ladda ner projektet och bygga den senaste versionen av PDF:en
själv. Byggsystemet använder Make med `pdflatex` (tillsammans med
`makeindex` och eventuell `bibtex`) för PDF och `tex4ebook` för EPUB,
och instruktioner finns i filen [BUILD.md](BUILD.md).

## Serverbyggd PDF

Lista med de senaste byggena finns i
[GitHub Actions](https://github.com/SverigesSandareamatorer/SSA-Akademin/actions/workflows/bygg.yml).


# Bidra till projektet

Det finns många olika sätt att bidra till projektet även fast man
inte vet hur man använder *[Git](https://git-scm.com)* eller skriver *LaTeX*.

**Fråga: Jag kan koda och vill bidra; vad gör jag?**<br>
Svar: Läs igenom [CONTRIBUTING.md](.github/CONTRIBUTING.md) och följ
instruktionerna.

**Fråga: Jag vet inte hur man redigerar kod?!**<br>
Svar: Det finns flera sätt att hjälpa till. Du kan läsa boken och ge
förslag på förbättringar och om du vet hur man gör så kan du lämna
en *issue* med en beskrivning av fel och om möjligt en föreslagen
förändring. Annars kan du använda dig av kontaktinformationen nedan
och skicka ett mejl till oss så hjälper vi dig att komma igång.


# Instruktioner för projektet

## Merge
Alla förändringar ska ske genom pull-requests som mergas.

Checklistan för en pull-request är till för att inga väsentligheter missas.
Grunden är att när alla saker är avcheckade på listan ska pull-requesten
kunna genomföras.

## Release
För att göra release följer man instruktionerna i [wikin](https://github.com/SverigesSandareamatorer/SSA-Akademin/wiki/Releaseinstruktion).


# Om SSA Akademin

Arbetet med denna bok är en del i en större satsning på att
uppdatera gammalt material, digitalisera material men också bredda
utbildningsmetoderna till mer än bara litteratur. Vi kallar projektet
för SSA Akademin. Vi undersöker hur och på vilka sätt utbildningen
under SSA kan moderniseras. Med modernisering syftas här utnyttjandet av
både digital teknik och dess möjligheter samt metoder som tidigare ej
använts inom SSA. Vi tar fram konkreta förslag på hur moderniseringen
ska gå till väga och genomför dem.

Vårt mål är att
-   fler ska vilja genomgå utbildningen för att bli radioamatör
-   de som examineras ska göra bättre ifrån sig på provet
-   de som deltar i utbildningen ska känna att det är en bra utbildning.

# Kontakt

-   [**Jonas "SM5PHU" Hultin**](mailto:sm5phu@gmail.com)
-   [Magnus "SA0MAD" Danielsson](mailto:magnus@rubidium.se)
-   [Philip "SA6EPH" Eriksson](mailto:philiperiksson@gmail.com)
-   [Täpp-Anders "SM5UEI" Sikvall](mailto:anders@sikvall.se)
-   [Per "SA0PHH" Hammarlund](mailto:gladbjorn@gmail.com)
