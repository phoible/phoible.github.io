---
layout: default
title:  "PHOIBLE notational conventions"
---

In order to preserve distinctions both within and across language descriptions, additions to the approved International Phonetic Alphabet (IPA) glyph set were needed; wherever possible these were drawn from the [extIPA symbols for disordered speech](https://www.internationalphoneticassociation.org/sites/default/files/extIPAChart2008.pdf). This page also describes any idiosyncracies in our interpretation and usage of approved IPA glyphs, and conventions regarding glyph ordering. The terms "official IPA", "approved IPA glyphs", or just "IPA" we are referring to [the 2005 update of the full chart](https://www.internationalphoneticassociation.org/content/full-ipa-chart) unless otherwise indicated.

# Similar-looking glyphs
There are a number of IPA symbols that resemble ordinary keyboard glyphs. In all cases the data in PHOIBLE use the codepoints for the official glyphs. The most common of these are summarized here:


| Keyboard letter                   | Representation in PHOIBLE                     | Meaning in IPA       |
|:----------------------------------|:----------------------------------------------|:---------------------|
| `g` ==0067 LATIN SMALL LETTER G== | `ɡ` ==0261 LATIN SMALL LETTER SCRIPT G==      | voiced velar stop    |
| `!` ==0021 EXCLAMATION POINT==    | `ǃ` ==01C3 LATIN LETTER RETROFLEX CLICK==     | (post)alveolar click |
| <code>&#124;</code> ==007C VERTICAL LINE==        | `ǀ` ==01C0 LATIN LETTER DENTAL CLICK==        | dental click         |
| `'` ==0027 APOSTROPHE==           | `ʼ` ==02BC MODIFIER LETTER APOSTROPHE==       | ejective             |
| `:` ==003A COLON==                | `ː` ==02D0 MODIFIER LETTER TRIANGULAR COLON== | long                 |


# Additions to the IPA
## Fortis / Lenis
Languages described as having a fortis/plain/lenis distinction that corresponds poorly with the traditional voiced/voiceless-unaspirated/voiceless-aspirated continuum are marked using the voiceless glyph for the “plain” phoneme, and either ~~`͈`~~ (==0348 COMBINING DOUBLE VERTICAL LINE BELOW==) to mark the fortis articulation, and/or ~~`͉`~~ (==0349 COMBINING LEFT ANGLE BELOW==) for the lenis articulation.

## Frictionalized sounds
The frictionalized diacritic ~~`͓`~~ (==0353 COMBINING X BELOW==) is used in PHOIBLE to represent three types of sounds:
- Click consonants where the release of the anterior closure involves an ingressive "sucking" sound similar to a fricative. In such cases the diacritic is placed on the click glyph, not on the glyph indicating the posterior closure location. Example: `kǃ͓ʰ`
- "Frictionalized" vowels (sounds that are phonologically vocalic, but with sufficiently close closures to create buzzing).
- Fricative sounds at places of articulation that do not have dedicated fricative glyphs (e.g., sounds with voiceless velar lateral frication: `ʟ̥͓`, `ɬʟ̥͓`, `kʟ̥͓ʼ`).

## Non-sibilant fricatives
Languages described as having a sibilant/non-sibilant distinction among coronal fricatives and affricates are handled using ~~`͇`~~ (==0347 COMBINING EQUALS SIGN BELOW==) to mark the non-sibilant phoneme.

## Retroflex clicks
Retroflex clicks are represented by `‼` (==203C DOUBLE EXCLAMATION MARK==). Note that `ǃ` (==01C3==, the symbol representing (post)alveolar clicks in the IPA) is confusingly referred to as ==LATIN LETTER RETROFLEX CLICK== in the Unicode standard.

## Glottalization
Sounds described as “glottalized” are marked with `ˀ` (==02C0 MODIFIER LETTER GLOTTAL STOP==), unless it is clear from context that either “ejective” or “creaky voicing” are the intended meaning. See the section on [Glottalization, laryngealization, and creaky voicing](#glottalization-laryngealization-and-creaky-voicing) for more details.

## Summary table of PHOIBLE symbols not in the IPA

| Glyph | Codepoint  | Description                              | Meaning in PHOIBLE   |
|:-----:|:----------:|:-----------------------------------------|:---------------------|
| ~~`͈`~~  | ==0348==   | ==COMBINING DOUBLE VERTICAL LINE BELOW== | Fortis               |
| ~~`͉`~~  | ==0349==   | ==COMBINING LEFT ANGLE BELOW==           | Lenis                |
| ~~`͓`~~  | ==0353==   | ==COMBINING X BELOW==                    | Frictionalized       |
| ~~`͇`~~  | ==0347==   | ==COMBINING EQUALS SIGN BELOW==          | Non-sibilant         |
| `‼`    | ==203C==   | ==DOUBLE EXCLAMATION MARK==              | Retroflex click      |
| `ˀ`     | ==02C0==   | ==MODIFIER LETTER GLOTTAL STOP==         | (Pre-)glottalization |
| `ʱ`     | ==02B1==   | ==MODIFIER LETTER SMALL H WITH HOOK==    | Pre-aspirated voiced |

# Idiosyncratic usages
## Place matching
In PHOIBLE, all affricates, prenasalized stops, and pre-stopped nasals adhere to strict place-matching. For example, although it is common to use `t` or `d` to designate the stop portion of all coronal affricates, in PHOIBLE a palatal affricate will always be represented as `cç` (not `tç`). A similar constraint holds for dental affricates `t̪s̪` and `t̪θ`, post-alveolar affricates `t̠ʃ`, and retroflex affricates `ʈʂ`. Note that `tɕ` is considered simultaneously (lamino-)alveolar and palatal, so no retraction diacritic is used on the `t`.

## Labialization, velarization and pharyngealization
In PHOIBLE we do not use ~~`̴`~~ (==0334 COMBINING TILDE OVERLAY==), which the IPA defines as a “velarized or pharyngealized” diacritic. For velarized articulations we use `ˠ` (==02E0 MODIFIER LETTER SMALL GAMMA==), for pharyngealized articulations we use `ˤ` (==02E4 MODIFIER LETTER REVERSED GLOTTAL STOP==).

The diacritic `ʷ` (==02B7 MODIFIER LETTER SMALL W==) is strictly used to mark *labialization* and not *labio-velarization*. If a source describes a sound as “labio-velarized” we use modifier letters `ʷ` and `ˠ` together.

## Aspiration, murmur, and breathy voicing
Voiceless aspirated sounds are marked with the standard `ʰ` (==02B0 MODIFIER LETTER SMALL H==). Voiceless sounds that are described as “pre-aspirated” are marked with the diacritic to the left of the base glyph: `ʰt`. Voiced sounds described as either “aspirated”, “breathy”, or “murmured” are marked with ~~`̤`~~ (==0324 COMBINING DIARESIS BELOW==). Voiced sounds described as “pre-aspirated” are marked with `ʱ` (==02B1 MODIFIER LETTER SMALL H WITH HOOK==) to the left of the base glyph: `ʱd`.

## Glottalization, laryngealization, and creaky voicing
Voiced sounds described as creaky or laryngealized are marked with ~~`̰`~~ (==0330 COMBINING TILDE BELOW==). Sounds described as “glottalized” are marked with `ˀ` (==02C0 MODIFIER LETTER GLOTTAL STOP==), unless the sound is voiceless and it is evident from the surrounding description that what is meant is that the consonant is ejective, in which case we use `ʼ` (==02BC MODIFIER LETTER APOSTROPHE==). Sounds described as “pre-glottalized” are marked with `ˀ` to the left of the base glyphː `ˀt`.

## Lowered fricatives and raised approximants
PHOIBLE somewhat grudgingly follows common practice in the literature in using the “uptack” and “downtack” to convert between fricative and approximant manners of articulation, when no suitable single glyph is available. For example, the Stanford Phonology Archive includes sounds described as “z-approximant” and “ɻ-fricative”, which we represent as `z̞` and `ɻ̝`, respectively. The raised diacritic is also used with the pharyngeal fricative to indicate a voiced pharyngeal plosive `ʕ̝`

## Low vowels
As with all representations in PHOIBLE, we privilege the textual description of the original authors over their choice of symbols. Consequently, sounds described as “low back unrounded vowels” are represented as `ɑ` (==0251 LATIN SMALL LETTER ALPHA==), even if the author used the keyboard `a` in his or her charts.

## Diphthongs
The glyphs `j`, `ɰ`, `ɥ`, `w` are used only for glide consonants, and never occur as on- or off-glides in diphthongs and triphthongs. Instead, polyphthong on- and off-glides use vowel symbols `i`, `ɯ`, `y`, and `u`. If necessary, the non-syllabic diacritic ~~`̯`~~ (==032F COMBINING INVERTED BREVE BELOW==) is used to disambiguate nucleus from glide portion (when such is indicated in the language description).

## Clicks
Clicks are always represented in PHOIBLE as a combination of anterior and posterior articulations. The posterior articulation is given first, and indicates both place (velar or uvular) and phonation during the click. Posterior click glyphs thus comprise the set `k` `q` `ɡ` `ɢ` `ŋ` `ɴ`. Laryngeal/phonatory modifiers are placed on the posterior glyph: `ŋ̊ǃ`. The anterior place and manner of the click are then indicated with the usual IPA click symbols `ʘ` `ǀ` `ǁ` `ǃ` `ǂ` and the PHOIBLE symbol for retroflex clicks `‼`. Note also that alveolar and post-alveolar clicks are distinguished in PHOIBLE by the use of the retraction diacritic: `kǃ` for alveolar, `kǃ̠` for post-alveolar. See also the section on [frictionalized sounds](#frictionalized-sounds) for notation of frictionalized clicks.

## Epilaryngeal phonation
There are some rare articulations that make use of an epilaryngeal phonation mechanism (e.g., the “sphincteric vowels” of !Xóõ). To represent these vowels, we use `ᴱ` (==1D31 MODIFIER LETTER CAPITAL E==) to denote sphincteric phonation.

## Double articulations / tie bars
The representations of speech sounds in PHOIBLE do not make use of the tie bar (==0361 COMBINING DOUBLE INVERTED BREVE== or ==035C COMBINING DOUBLE BREVE BELOW==). The reasons for this choice are (1) it aids legibility when there are other diacritics, and (2) since the data are limited to single phonemes (i.e., there are no transcriptions of words or longer passages), there is no need to distinguish single phonemes from sequences. Put another way, every phoneme in PHOIBLE that is represented as a digraph has an implicit tiebar.

# Ordering of diacritics and modifier letters
*This section makes a distinction between “combining characters” and “spacing modifier letters”, which most linguists would group together under one term “diacritics”. Briefly, combining characters are diacritics that sit above or below the glyph they modify, or are superimposed on it (e.g., the tilde above a nasalized vowel ~~`̃`~~ is a combining character, encoded as ==0303== in the Unicode standard). Spacing modifier letters are diacritics that sit next to the glyph they modify (e.g., the superscript `ʰ` used to indicate aspiration is a modifier letter, encoded as ==02B0==).*

Each segment type that is composed of more than one character is first normalized into a canonical decomposition form that adheres to the [Unicode Normalization Form D (NFD)](http://unicode.org/reports/tr15/). However, the NFD algorithm does not define a prescribed order for all possible pairs of combining characters. For example, ==0301== (combining acute accent) and ==0308== (combining diaresis) are not re-ordered with respect to one another by the NFD algorithm, regardless of which order they occurred in the input string. PHOIBLE imposes an ordering that is consistent with NFD, but sets an explicit order for all combining characters used in the database. A ridid ordering for spacing modifier letters is also enforced. The chosen ordering is guided by the linguistic literature and typographical concerns, since to the best of our knowledge the IPA does not provide a recommended ordering for diacritics.

The ordering conventions used in PHOIBLE are as follows:

1. **Place features:** linguolabial ~~`̼`~~, dental ~~`̪`~~, apical ~~`̺`~~, laminal ~~`̻`~~, advanced ~~`̟`~~, retracted ~~`̠`~~
2. **Manner features:** raised ~~`̝`~~, lowered ~~`̞`~~, advanced tongue root ~~`̘`~~, retracted tongue root ~~`̙`~~, frictionalized ~~`͓`~~
3. **Secondary articulations:** more round ~~`̹`~~, less round ~~`̜`~~, derhoticized ~~`̮`~~
4. **Laryngeal settings:** creaky ~~`̰`~~, breathy ~~`̤`~~, voiced ~~`̬`~~, devoiced (below) ~~`̥`~~, devoiced (above) ~~`̊`~~
5. **Syllabicity:** syllabic ~~`̩`~~ and non-syllabic markers ~~`̯`~~
6. **Vowel quality modifications**: nasalized ~~`̃`~~, centralized ~~`̈`~~, mid-centralized ~~`̽`~~
7. **Stop release:** unreleased `̚`
8. **Spacing modifier letters:** rhotic hook `˞`, nasal release `ⁿ`, lateral release `ˡ`, labialized `ʷ`, palatalized `ʲ`, velarized `ˠ`, pharyngealized `ˤ`, glottalized `ˀ`, aspirated `ʰ`, ejective `ʼ`, long `ː`, half long `ˑ`

# Marginal phonemes
Marginal phonemes are those that are notably different phonologically from the majority of segments found in a particular language. For example, loanwords containing non-native sounds can introduce maringal phonemes into the borrowing language. Any type of phoneme described as “marginal”, “dubious” or “occurs only in loan words” is included in the database alongside other phonemes, but is marked with a boolean <span class="mono">TRUE</span> value in the <span class="mono">Marginal</span> column of the data file. Ordinary phonemes typically have the value <span class="mono">FALSE</span>, although for data sources that explicitly exclude marginal phonemes, the <span class="mono">Marginal</span> column is given <span class="mono">NA</span> values for those inventories.
