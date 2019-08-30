---
layout: default
title:  "PHOIBLE notational conventions"
---

In order to preserve distinctions both within and across language descriptions, additions to the approved International Phonetic Alphabet (IPA) glyph set were needed; wherever possible these were drawn from the [extIPA symbols for disordered speech](https://www.internationalphoneticassociation.org/sites/default/files/extIPAChart2008.pdf). This page describes our additions to the IPA glyph set, and also describes any idiosyncracies in our interpretation and usage of approved IPA glyphs, and conventions regarding glyph ordering. The terms "official IPA", "approved IPA glyphs", or just "IPA" we are referring to [the 2005 update of the full chart](https://www.internationalphoneticassociation.org/content/full-ipa-chart) unless otherwise indicated.

# Similar-looking glyphs
There are a number of IPA symbols that resemble ordinary keyboard glyphs. In all cases the data in PHOIBLE use the codepoints for the official glyphs. The most common of these are summarized here:


| Keyboard letter                            | Representation in PHOIBLE                     | Meaning in IPA       |
|:-------------------------------------------|:----------------------------------------------|:---------------------|
| `g` <mark>0067 LATIN SMALL LETTER G</mark>          | `ɡ` <mark>0261 LATIN SMALL LETTER SCRIPT G</mark>      | voiced velar stop    |
| `!` <mark>0021 EXCLAMATION POINT</mark>             | `ǃ` <mark>01C3 LATIN LETTER RETROFLEX CLICK</mark>     | (post)alveolar click |
| <code>&#124;</code> <mark>007C VERTICAL LINE</mark> | `ǀ` <mark>01C0 LATIN LETTER DENTAL CLICK</mark>        | dental click         |
| `'` <mark>0027 APOSTROPHE</mark>                    | `ʼ` <mark>02BC MODIFIER LETTER APOSTROPHE</mark>       | ejective             |
| `:` <mark>003A COLON</mark>                         | `ː` <mark>02D0 MODIFIER LETTER TRIANGULAR COLON</mark> | long                 |


In addition, PHOIBLE eschews the use of precomposed digraphs such as `ʤ`, `ʨ`, etc. to represent affricates. Note that since each entry in PHOIBLE represents a single phonologically contrastive sound in its doculect, there is never any risk that an entry such as `tɕ` might be confused as a sequence of two phonemes (stop + fricative) rather than a single affricate.

# Additions to the IPA
## Fortis / Lenis
Languages described as having a fortis/plain/lenis distinction that corresponds poorly with the traditional voiced/voiceless-unaspirated/voiceless-aspirated continuum are marked using the voiceless glyph for the “plain” phoneme, and either ~~`͈`~~ (<mark>0348 COMBINING DOUBLE VERTICAL LINE BELOW</mark>) to mark the fortis articulation, and/or ~~`͉`~~ (<mark>0349 COMBINING LEFT ANGLE BELOW</mark>) for the lenis articulation.

## Frictionalized sounds
The frictionalized diacritic ~~`͓`~~ (<mark>0353 COMBINING X BELOW</mark>) is used in PHOIBLE to represent three types of sounds:

- Click consonants where the release of the anterior closure involves an ingressive "sucking" sound similar to a fricative. In such cases the diacritic is placed on the click glyph, not on the glyph indicating the posterior closure location. Example: `kǃ͓ʰ`
- "Frictionalized" vowels (sounds that are phonologically vocalic, but with sufficiently close closures to create buzzing).
- Fricative sounds at places of articulation that do not have dedicated fricative glyphs (e.g., sounds with voiceless velar lateral frication: `ʟ̥͓`, `ɬʟ̥͓`, `kʟ̥͓ʼ`).

## Non-sibilant fricatives
Languages described as having a sibilant/non-sibilant distinction among coronal fricatives and affricates are handled using ~~`͇`~~ (<mark>0347 COMBINING EQUALS SIGN BELOW</mark>) to mark the non-sibilant phoneme.

## Retroflex clicks
Retroflex clicks are represented by `‼` (<mark>203C DOUBLE EXCLAMATION MARK</mark>). Note that `ǃ` (<mark>01C3</mark>, the symbol representing (post)alveolar clicks in the IPA) is confusingly referred to as <mark>LATIN LETTER RETROFLEX CLICK</mark> in the Unicode standard.

## Glottalization
Sounds described as “glottalized” are marked with `ˀ` (<mark>02C0 MODIFIER LETTER GLOTTAL STOP</mark>), unless it is clear from context that either “ejective” or “creaky voicing” are the intended meaning. See the section on [Glottalization, laryngealization, and creaky voicing](#glottalization,-laryngealization,-and-creaky-voicing) for more details.

## Summary table of PHOIBLE symbols not in the IPA

| Glyph   | Codepoint  | Description                              | Meaning in PHOIBLE   |
|:-------:|:----------:|:-----------------------------------------|:---------------------|
| ~~`͈`~~  | <mark>0348</mark>   | <mark>COMBINING DOUBLE VERTICAL LINE BELOW</mark> | Fortis               |
| ~~`͉`~~  | <mark>0349</mark>   | <mark>COMBINING LEFT ANGLE BELOW</mark>           | Lenis                |
| ~~`͓`~~  | <mark>0353</mark>   | <mark>COMBINING X BELOW</mark>                    | Frictionalized       |
| ~~`͇`~~  | <mark>0347</mark>   | <mark>COMBINING EQUALS SIGN BELOW</mark>          | Non-sibilant         |
| `‼`    | <mark>203C</mark>   | <mark>DOUBLE EXCLAMATION MARK</mark>              | Retroflex click      |
| `ˀ`     | <mark>02C0</mark>   | <mark>MODIFIER LETTER GLOTTAL STOP</mark>         | (Pre-)glottalization |
| `ʱ`     | <mark>02B1</mark>   | <mark>MODIFIER LETTER SMALL H WITH HOOK</mark>    | Pre-aspirated voiced |

# Idiosyncratic usages
## Place matching
In PHOIBLE, all affricates, prenasalized stops, and pre-stopped nasals adhere to strict place-matching. For example, although it is common to use `t` or `d` to designate the stop portion of all coronal affricates, in PHOIBLE a palatal affricate will always be represented as `cç` (not `tç`). A similar constraint holds for dental affricates `t̪s̪` and `t̪θ`, post-alveolar affricates `t̠ʃ`, and retroflex affricates `ʈʂ`. Note that `tɕ` is considered simultaneously (lamino-)alveolar and palatal, so no retraction diacritic is used on the `t`.

## Labialization, velarization and pharyngealization
In PHOIBLE we do not use ~~`̴`~~ (<mark>0334 COMBINING TILDE OVERLAY</mark>), which the IPA defines as a “velarized or pharyngealized” diacritic. For velarized articulations we use `ˠ` (<mark>02E0 MODIFIER LETTER SMALL GAMMA</mark>), for pharyngealized articulations we use `ˤ` (<mark>02E4 MODIFIER LETTER REVERSED GLOTTAL STOP</mark>).

The diacritic `ʷ` (<mark>02B7 MODIFIER LETTER SMALL W</mark>) is strictly used to mark *labialization* and not *labio-velarization*. If a source describes a sound as “labio-velarized” we use modifier letters `ʷ` and `ˠ` together.

## Aspiration, murmur, and breathy voicing
Voiceless aspirated sounds are marked with the standard `ʰ` (<mark>02B0 MODIFIER LETTER SMALL H</mark>). Voiceless sounds that are described as “pre-aspirated” are marked with the diacritic to the left of the base glyph: `ʰt`. Voiced sounds described as either “aspirated”, “breathy”, or “murmured” are marked with ~~`̤`~~ (<mark>0324 COMBINING DIARESIS BELOW</mark>). Voiced sounds described as “pre-aspirated” are marked with `ʱ` (<mark>02B1 MODIFIER LETTER SMALL H WITH HOOK</mark>) to the left of the base glyph: `ʱd`.

## Glottalization, laryngealization, and creaky voicing
Voiced sounds described as creaky or laryngealized are marked with ~~`̰`~~ (<mark>0330 COMBINING TILDE BELOW</mark>). Sounds described as “glottalized” are marked with `ˀ` (<mark>02C0 MODIFIER LETTER GLOTTAL STOP</mark>), unless the sound is voiceless and it is evident from the surrounding description that what is meant is that the consonant is ejective, in which case we use `ʼ` (<mark>02BC MODIFIER LETTER APOSTROPHE</mark>). Sounds described as “pre-glottalized” are marked with `ˀ` to the left of the base glyphː `ˀt`.

## Lowered fricatives and raised approximants
PHOIBLE somewhat grudgingly follows common practice in the literature in using the “uptack” and “downtack” to convert between fricative and approximant manners of articulation, when no suitable single glyph is available. For example, the Stanford Phonology Archive includes sounds described as “z-approximant” and “ɻ-fricative”, which we represent as `z̞` and `ɻ̝`, respectively. The raised diacritic is also used with the pharyngeal fricative to indicate a voiced pharyngeal plosive `ʕ̝`

## Low vowels
As with all representations in PHOIBLE, we privilege the textual description of the original authors over their choice of symbols. Consequently, sounds described as “low back unrounded vowels” are represented as `ɑ` (<mark>0251 LATIN SMALL LETTER ALPHA</mark>), even if the author used the keyboard `a` in his or her charts.

## Diphthongs
The glyphs `j`, `ɰ`, `ɥ`, `w` are used only for glide consonants, and never occur as on- or off-glides in diphthongs and triphthongs. Instead, polyphthong on- and off-glides use vowel symbols `i`, `ɯ`, `y`, and `u`. If necessary, the non-syllabic diacritic ~~`̯`~~ (<mark>032F COMBINING INVERTED BREVE BELOW</mark>) is used to disambiguate nucleus from glide portion (when such is indicated in the language description).

## Clicks
Clicks are always represented in PHOIBLE as a combination of anterior and posterior articulations. The posterior articulation is given first, and indicates both place (velar or uvular) and phonation during the click. Posterior click glyphs thus comprise the set `k` `q` `ɡ` `ɢ` `ŋ` `ɴ`. Laryngeal/phonatory modifiers are placed on the posterior glyph: `ŋ̊ǃ`. The anterior place and manner of the click are then indicated with the usual IPA click symbols `ʘ` `ǀ` `ǁ` `ǃ` `ǂ` and the PHOIBLE symbol for retroflex clicks `‼`. Note also that alveolar and post-alveolar clicks are distinguished in PHOIBLE by the use of the retraction diacritic: `kǃ` for alveolar, `kǃ̠` for post-alveolar. See also the section on [frictionalized sounds](#frictionalized-sounds) for notation of frictionalized clicks.

## Epilaryngeal phonation
There are some rare articulations that make use of an epilaryngeal phonation mechanism (e.g., the “sphincteric vowels” of !Xóõ). To represent these vowels, we use `ᴱ` (<mark>1D31 MODIFIER LETTER CAPITAL E</mark>) to denote sphincteric phonation.

## Apical vowels
The so-called “apical vowels” (most famously described in Modern Standard Chinese, a.k.a. “Mandarin”) have been traditionally represented by many Sinologists using non-standard glyphs `ɿ` and `ʅ`. In PHOIBLE we follow [Lee-Kim 2014](https://doi.org/10.1017/S0025100314000267) in treating segments described as “apical vowels” as (possibly syllabic) approximants — in particular, as the dental approximant `ɹ̪̩` and the retroflex approximant `ɻ̩`.

## Double articulations / tie bars
The representations of speech sounds in PHOIBLE do not make use of the tie bar (<mark>0361 COMBINING DOUBLE INVERTED BREVE</mark> or <mark>035C COMBINING DOUBLE BREVE BELOW</mark>). The reasons for this choice are (1) it aids legibility when there are other diacritics, and (2) since the data are limited to single phonemes (i.e., there are no transcriptions of words or longer passages), there is no need to distinguish single phonemes from sequences. Put another way, every phoneme in PHOIBLE that is represented as a digraph has an implicit tiebar.

# Ordering of diacritics and modifier letters
*This section makes a distinction between “combining characters” and “spacing modifier letters”, which most linguists would group together under one term “diacritics”. Briefly, combining characters are diacritics that sit above or below the glyph they modify, or are superimposed on it (e.g., the tilde above a nasalized vowel ~~`̃`~~ is a combining character, encoded as <mark>0303</mark> in the Unicode standard). Spacing modifier letters are diacritics that sit next to the glyph they modify (e.g., the superscript `ʰ` used to indicate aspiration is a modifier letter, encoded as <mark>02B0</mark>).*

Each representation of a phoneme is first normalized into a canonical decomposition form that adheres to the [Unicode Normalization Form D (NFD)](http://unicode.org/reports/tr15/). However, the NFD algorithm does not define a prescribed order for all possible pairs of combining characters. For example, <mark>0301</mark> (combining acute accent) and <mark>0308</mark> (combining diaresis) are not re-ordered with respect to one another by the NFD algorithm, regardless of which order they occurred in the input string. PHOIBLE imposes an ordering that is consistent with NFD, but sets an explicit order for all combining characters used in the database. A rigid ordering for spacing modifier letters is also enforced. The chosen ordering is guided by the linguistic literature and typographical concerns, since to the best of our knowledge the IPA does not provide a recommended ordering for diacritics.

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

# Pitch accent
This section lists inventories that are known to have pitch accents among their tonemes, and describes how the pitch accents were encoded in PHOIBLE. This list should not be considered exhaustive; there may be doculects where the author chose not to describe pitch accent even though it was present in the object language, or (in doculects absorbed into PHOIBLE from other databases) cases where the original database aggregator ignored information about pitch accent when building their database.

## <span class="mono">nld</span> (Dutch)
### Hasselt dialect
Accent 1: no underlying tone. Accent 2: low tone. Peters 2006, p.121 (emphasis added):
> The timing difference between accent 1 and accent 2 can be accounted for by assuming that **accent 2 words have a lexical L tone**, while accent 1 words are lexically toneless. In nuclear position, the lexical L tone, which is pre-linked to the accented syllable, does not allow  H∗ to  associate.

### Maastricht dialect
Accent 1: no underlying tone. Accent 2: high tone. Gussenhoven 1999, p.162 (emphasis added):
> ... the fundamental frequency of syllables with Accent 2 differs from those with Accent 1. In view of its effect in utterances with Accent 2 as compared with equivalent utterances with Accent 1, **it is reasonable to assume that Accent 2 is a H-tone** occurring in or immediately after the stressed syllable.
