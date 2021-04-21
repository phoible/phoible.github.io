==============================
PHOIBLE notational conventions
==============================

.. role:: ipa

.. role:: dia

.. role:: codept

.. role:: iso


In order to preserve distinctions both within and across language descriptions, additions to the approved International Phonetic Alphabet (IPA) glyph set were needed; wherever possible these were drawn from the `extIPA symbols for disordered speech`_. This page describes our additions to the IPA glyph set, and also describes any idiosyncracies in our interpretation and usage of approved IPA glyphs, and conventions regarding glyph ordering. When we use the terms "official IPA", "approved IPA glyphs", or just "IPA" we are referring to `the 2005 update of the full chart`_ unless otherwise indicated.

Similar-looking glyphs
======================

There are a number of IPA symbols that resemble ordinary keyboard glyphs. In all cases the data in PHOIBLE use the codepoints for the official glyphs. The most common of these are summarized here:


.. class:: table table-bordered order-column compact stripe dataTable no-footer table-nonfluid

+----------------------------------------------+----------------------------------------------------------+----------------------+
| Keyboard letter                              | Representation in PHOIBLE                                | Meaning in IPA       |
+==============================================+==========================================================+======================+
| :ipa:`g` :codept:`0067 LATIN SMALL LETTER G` | :ipa:`ɡ` :codept:`0261 LATIN SMALL LETTER SCRIPT G`      | voiced velar stop    |
+----------------------------------------------+----------------------------------------------------------+----------------------+
| :ipa:`!` :codept:`0021 EXCLAMATION POINT`    | :ipa:`ǃ` :codept:`01C3 LATIN LETTER RETROFLEX CLICK`     | (post)alveolar click |
+----------------------------------------------+----------------------------------------------------------+----------------------+
| :ipa:`|` :codept:`007C VERTICAL LINE`        | :ipa:`ǀ` :codept:`01C0 LATIN LETTER DENTAL CLICK`        | dental click         |
+----------------------------------------------+----------------------------------------------------------+----------------------+
| :ipa:`'` :codept:`0027 APOSTROPHE`           | :ipa:`ʼ` :codept:`02BC MODIFIER LETTER APOSTROPHE`       | ejective             |
+----------------------------------------------+----------------------------------------------------------+----------------------+
| :ipa:`:` :codept:`003A COLON`                | :ipa:`ː` :codept:`02D0 MODIFIER LETTER TRIANGULAR COLON` | long                 |
+----------------------------------------------+----------------------------------------------------------+----------------------+


In addition, PHOIBLE eschews the use of precomposed digraphs such as :ipa:`ʤ`, :ipa:`ʨ`, etc. to represent affricates. Note that since each entry in PHOIBLE represents a single phonologically contrastive sound in its doculect, there is never any risk that an entry such as :ipa:`tɕ` might be confused as a sequence of two phonemes (stop + fricative) rather than a single affricate.

Additions to the IPA
====================


Fortis / Lenis
--------------

Languages described as having a fortis/plain/lenis distinction that corresponds poorly with the traditional voiced/voiceless-unaspirated/voiceless-aspirated continuum are marked using the voiceless glyph for the "plain" phoneme, and either :dia:`͈` (:codept:`0348 COMBINING DOUBLE VERTICAL LINE BELOW`) to mark the fortis articulation, and/or :dia:`͉` (:codept:`0349 COMBINING LEFT ANGLE BELOW`) for the lenis articulation.


Frictionalized sounds
---------------------

The frictionalized diacritic :dia:`͓` (:codept:`0353 COMBINING X BELOW`) is used in PHOIBLE to represent three types of sounds:

- Click consonants where the release of the anterior closure involves an ingressive "sucking" sound similar to a fricative. In such cases the diacritic is placed on the click glyph, not on the glyph indicating the posterior closure location. Example: :ipa:`kǃ͓ʰ`
- "Frictionalized" vowels (sounds that are phonologically vocalic, but with sufficiently close closures to create buzzing).
- Fricative sounds at places of articulation that do not have dedicated fricative glyphs (e.g., sounds with voiceless velar lateral frication: :ipa:`ʟ̥͓`, :ipa:`ɬʟ̥͓`, :ipa:`kʟ̥͓ʼ`).


Non-sibilant fricatives
-----------------------

Languages described as having a sibilant/non-sibilant distinction among coronal fricatives and affricates are handled using :dia:`͇` (:codept:`0347 COMBINING EQUALS SIGN BELOW`) to mark the non-sibilant phoneme.


Retroflex clicks
----------------

Retroflex clicks are represented by :ipa:`‼` (:codept:`203C DOUBLE EXCLAMATION MARK`). Note that :ipa:`ǃ` (:codept:`01C3`, the symbol representing (post)alveolar clicks in the IPA) is confusingly referred to as :codept:`LATIN LETTER RETROFLEX CLICK` in the Unicode standard.

Glottalization
--------------

Sounds described as "glottalized" are marked with :ipa:`ˀ` (:codept:`02C0 MODIFIER LETTER GLOTTAL STOP`), unless it is clear from context that either "ejective" or "creaky voicing" are the intended meaning. See the section on `Glottalization, laryngealization, and creaky voicing`_ for more details.

Summary table of PHOIBLE symbols not in the IPA
-----------------------------------------------

.. class:: table table-bordered order-column compact stripe dataTable no-footer table-nonfluid

===========  ================  ===============================================  ======================
 Glyph        Codepoint         Description                                      Meaning in PHOIBLE
===========  ================  ===============================================  ======================
 :dia:`͈`     :codept:`0348`    :codept:`COMBINING DOUBLE VERTICAL LINE BELOW`   Fortis
-----------  ----------------  -----------------------------------------------  ----------------------
 :dia:`͉`     :codept:`0349`    :codept:`COMBINING LEFT ANGLE BELOW`             Lenis
-----------  ----------------  -----------------------------------------------  ----------------------
 :dia:`͓`     :codept:`0353`    :codept:`COMBINING X BELOW`                      Frictionalized
-----------  ----------------  -----------------------------------------------  ----------------------
 :dia:`͇`     :codept:`0347`    :codept:`COMBINING EQUALS SIGN BELOW`            Non-sibilant
-----------  ----------------  -----------------------------------------------  ----------------------
 :ipa:`‼`     :codept:`203C`    :codept:`DOUBLE EXCLAMATION MARK`                Retroflex click
-----------  ----------------  -----------------------------------------------  ----------------------
 :ipa:`ˀ`     :codept:`02C0`    :codept:`MODIFIER LETTER GLOTTAL STOP`           (Pre-)glottalization
-----------  ----------------  -----------------------------------------------  ----------------------
 :ipa:`ʱ`     :codept:`02B1`    :codept:`MODIFIER LETTER SMALL H WITH HOOK`      Pre-aspirated voiced
===========  ================  ===============================================  ======================



Idiosyncratic usages
====================

Place matching
--------------

In PHOIBLE, all affricates, prenasalized stops, and pre-stopped nasals adhere to strict place-matching. For example, although it is common to use :ipa:`t` or :ipa:`d` to designate the stop portion of all coronal affricates, in PHOIBLE a palatal affricate will always be represented as :ipa:`cç` (not :ipa:`tç`). A similar constraint holds for dental affricates :ipa:`t̪s̪` and :ipa:`t̪θ`, post-alveolar affricates :ipa:`t̠ʃ`, and retroflex affricates :ipa:`ʈʂ`. Note that :ipa:`tɕ` is considered simultaneously (lamino-)alveolar and palatal, so no retraction diacritic is used on the :ipa:`t`.


Labialization, velarization and pharyngealization
-------------------------------------------------

In PHOIBLE we do not use :dia:`̴` (:codept:`0334 COMBINING TILDE OVERLAY`), which the IPA defines as a "velarized or pharyngealized" diacritic. For velarized articulations we use :ipa:`ˠ` (:codept:`02E0 MODIFIER LETTER SMALL GAMMA`), for pharyngealized articulations we use :ipa:`ˤ` (:codept:`02E4 MODIFIER LETTER REVERSED GLOTTAL STOP`).

The diacritic :ipa:`ʷ` (:codept:`02B7 MODIFIER LETTER SMALL W`) is strictly used to mark *labialization* and not *labio-velarization*. If a source describes a sound as "labio-velarized" we use modifier letters :ipa:`ʷ` and :ipa:`ˠ` together.


Aspiration, murmur, and breathy voicing
---------------------------------------

Voiceless aspirated sounds are marked with the standard :ipa:`ʰ` (:codept:`02B0 MODIFIER LETTER SMALL H`). Voiceless sounds that are described as "pre-aspirated" are marked with the diacritic to the left of the base glyph: :ipa:`ʰt`. Voiced sounds described as either "aspirated", "breathy", or "murmured" are marked with :dia:`̤` (:codept:`0324 COMBINING DIARESIS BELOW`). Voiced sounds described as "pre-aspirated" are marked with :ipa:`ʱ` (:codept:`02B1 MODIFIER LETTER SMALL H WITH HOOK`) to the left of the base glyph: :ipa:`ʱd`.


Glottalization, laryngealization, and creaky voicing
----------------------------------------------------

Voiced sounds described as creaky or laryngealized are marked with :dia:`̰` (:codept:`0330 COMBINING TILDE BELOW`). Sounds described as "glottalized" are marked with :ipa:`ˀ` (:codept:`02C0 MODIFIER LETTER GLOTTAL STOP`), unless the sound is voiceless and it is evident from the surrounding description that what is meant is that the consonant is ejective, in which case we use :ipa:`ʼ` (:codept:`02BC MODIFIER LETTER APOSTROPHE`). Sounds described as "pre-glottalized" are marked with :ipa:`ˀ` to the left of the base glyphː :ipa:`ˀt`.

## Lowered fricatives and raised approximants
PHOIBLE somewhat grudgingly follows common practice in the literature in using the "uptack" and "downtack" to convert between fricative and approximant manners of articulation, when no suitable single glyph is available. For example, the Stanford Phonology Archive includes sounds described as "z-approximant" and "ɻ-fricative", which we represent as :ipa:`z̞` and :ipa:`ɻ̝`, respectively. The raised diacritic is also used with the pharyngeal fricative to indicate a voiced pharyngeal plosive :ipa:`ʕ̝`


Low vowels
----------

As with all representations in PHOIBLE, we privilege the textual description of the original authors over their choice of symbols. Consequently, sounds described as "low back unrounded vowels" are represented as :ipa:`ɑ` (:codept:`0251 LATIN SMALL LETTER ALPHA`), even if the author used the keyboard :ipa:`a` in his or her charts.


Diphthongs
----------

The glyphs :ipa:`j`, :ipa:`ɰ`, :ipa:`ɥ`, :ipa:`w` are used only for glide consonants, and never occur as on- or off-glides in diphthongs and triphthongs. Instead, polyphthong on- and off-glides use vowel symbols :ipa:`i`, :ipa:`ɯ`, :ipa:`y`, and :ipa:`u`. If necessary, the non-syllabic diacritic :dia:`̯` (:codept:`032F COMBINING INVERTED BREVE BELOW`) is used to disambiguate nucleus from glide portion (when such is indicated in the language description).


Clicks
------

Clicks are always represented in PHOIBLE as a combination of anterior and posterior articulations. The posterior articulation is given first, and indicates both place (velar or uvular) and phonation during the click. Posterior click glyphs thus comprise the set :ipa:`k` :ipa:`q` :ipa:`ɡ` :ipa:`ɢ` :ipa:`ŋ` :ipa:`ɴ`. Laryngeal/phonatory modifiers are placed on the posterior glyph: :ipa:`ŋ̊ǃ`. The anterior place and manner of the click are then indicated with the usual IPA click symbols :ipa:`ʘ` :ipa:`ǀ` :ipa:`ǁ` :ipa:`ǃ` :ipa:`ǂ` and the PHOIBLE symbol for retroflex clicks :ipa:`‼`. Note also that alveolar and post-alveolar clicks are distinguished in PHOIBLE by the use of the retraction diacritic: :ipa:`kǃ` for alveolar, :ipa:`kǃ̠` for post-alveolar. See also the section on `frictionalized sounds`_ for notation of frictionalized clicks.


Epilaryngeal phonation
----------------------

There are some rare articulations that make use of an epilaryngeal phonation mechanism (e.g., the "sphincteric vowels" of !Xóõ). To represent these vowels, we use :ipa:`ᴱ` (:codept:`1D31 MODIFIER LETTER CAPITAL E`) to denote sphincteric phonation.


Apical vowels
-------------

The so-called "apical vowels" (most famously described in Modern Standard Chinese, a.k.a. "Mandarin") have been traditionally represented by many Sinologists using non-standard glyphs :ipa:`ɿ` and :ipa:`ʅ`. In PHOIBLE we follow `Lee-Kim 2014`_ in treating segments described as "apical vowels" as (possibly syllabic) approximants — in particular, as the dental approximant :ipa:`ɹ̪̩` and the retroflex approximant :ipa:`ɻ̩`.


Double articulations / tie bars
-------------------------------

The representations of speech sounds in PHOIBLE do not make use of the tie bar (:codept:`0361 COMBINING DOUBLE INVERTED BREVE` or :codept:`035C COMBINING DOUBLE BREVE BELOW`). The reasons for this choice are (1) it aids legibility when there are other diacritics, and (2) since the data are limited to single phonemes (i.e., there are no transcriptions of words or longer passages), there is no need to distinguish single phonemes from sequences. Put another way, every phoneme in PHOIBLE that is represented as a digraph has an implicit tiebar.


Ordering of diacritics and modifier letters
===========================================

.. note::
   This section makes a distinction between "combining characters" and "spacing modifier letters", which most linguists would group together under one term "diacritics". Briefly, combining characters are diacritics that sit above or below the glyph they modify, or are superimposed on it (e.g., the tilde above a nasalized vowel :dia:`̃` is a combining character, encoded as :codept:`0303` in the Unicode standard). Spacing modifier letters are diacritics that sit next to the glyph they modify (e.g., the superscript :ipa:`ʰ` used to indicate aspiration is a modifier letter, encoded as :codept:`02B0`).

Each representation of a phoneme is first normalized into a canonical decomposition form that adheres to the `Unicode Normalization Form D (NFD)`_. However, the NFD algorithm does not define a prescribed order for all possible pairs of combining characters. For example, :codept:`0301` (combining acute accent) and :codept:`0308` (combining diaresis) are not re-ordered with respect to one another by the NFD algorithm, regardless of which order they occurred in the input string. PHOIBLE imposes an ordering that is consistent with NFD, but sets an explicit order for all combining characters used in the database. A rigid ordering for spacing modifier letters is also enforced. The chosen ordering is guided by the linguistic literature and typographical concerns, since to the best of our knowledge the IPA does not provide a recommended ordering for diacritics.

The ordering conventions used in PHOIBLE are as follows:

1. **Place features:** velarized/pharyngealized :dia:`̴`, linguolabial :dia:`̼`, dental :dia:`̪`, apical :dia:`̺`, laminal :dia:`̻`, advanced :dia:`̟`, retracted :dia:`̠`
2. **Manner features:** non-sibilant :dia:`͇`, raised :dia:`̝`, lowered :dia:`̞`, advanced tongue root :dia:`̘`, retracted tongue root :dia:`̙`, frictionalized :dia:`͓`
3. **Secondary articulations:** more round :dia:`̹`, less round :dia:`̜`
4. **Laryngeal settings:** creaky :dia:`̰`, breathy :dia:`̤`, voiced :dia:`̬`, stiff :dia:`̬`, devoiced (below) :dia:`̥`, devoiced (above) :dia:`̊`, fortis :dia:`͈`, lenis :dia:`͉`
5. **Length:** short :dia:`̆`
6. **Syllabicity:** syllabic :dia:`̩` and non-syllabic markers :dia:`̯`
7. **Vowel quality modifications**: nasalized :dia:`̃`, denasalized :dia:`͊`, centralized :dia:`̈`, mid-centralized :dia:`̽`
8. **Stop release:** unreleased :dia:`̚`
9. **Spacing modifier letters:** rhotic hook :ipa:`˞`, nasal release :ipa:`ⁿ`, lateral release :ipa:`ˡ`, labialized :ipa:`ʷ`, palatalized :ipa:`ʲ`, labial-palatalized :ipa:`ᶣ`, velarized :ipa:`ˠ`, pharyngealized :ipa:`ˤ`, glottalized :ipa:`ˀ`, schwa-like release :ipa:`ᵊ`, epilaryngeal source :ipa:`ᴱ`, aspirated :ipa:`ʰ`, breathy aspirated :ipa:`ʱ`, ejective :ipa:`ʼ`, long :ipa:`ː`, half long :ipa:`ˑ`


Marginal phonemes
=================

Marginal phonemes are those that are notably different phonologically from the majority of segments found in a particular language. For example, loanwords containing non-native sounds can introduce maringal phonemes into the borrowing language. Any type of phoneme described as "marginal", "dubious" or "occurs only in loan words" is included in the database alongside other phonemes, but is marked with a boolean ``TRUE`` value in the ``Marginal`` column of the data file. Ordinary phonemes typically have the value ``FALSE``, although for data sources that explicitly exclude marginal phonemes, the ``Marginal`` column is given ``NA`` values for those inventories.


Pitch accent
============

This section lists inventories that are known to have pitch accents among their tonemes, and describes how the pitch accents were encoded in PHOIBLE. This list should not be considered exhaustive; there may be doculects where the author chose not to describe pitch accent even though it was present in the object language, or (in doculects absorbed into PHOIBLE from other databases) cases where the original database aggregator ignored information about pitch accent when building their database.


:iso:`nld` (Dutch)
------------------


Hasselt dialect
~~~~~~~~~~~~~~~

Accent 1: no underlying tone. Accent 2: low tone. Peters 2006, p.121 (emphasis added):

    The timing difference between accent 1 and accent 2 can be accounted for by assuming that **accent 2 words have a lexical L tone**, while accent 1 words are lexically toneless. In nuclear position, the lexical L tone, which is pre-linked to the accented syllable, does not allow  H∗ to  associate.

Maastricht dialect
~~~~~~~~~~~~~~~~~~

Accent 1: no underlying tone. Accent 2: high tone. Gussenhoven 1999, p.162 (emphasis added):

    ... the fundamental frequency of syllables with Accent 2 differs from those with Accent 1. In view of its effect in utterances with Accent 2 as compared with equivalent utterances with Accent 1, **it is reasonable to assume that Accent 2 is a H-tone** occurring in or immediately after the stressed syllable.


.. _extIPA symbols for disordered speech: https://www.internationalphoneticassociation.org/sites/default/files/extIPAChart2008.pdf
.. _the 2005 update of the full chart: https://www.internationalphoneticassociation.org/content/full-ipa-chart
.. _Lee-Kim 2014: https://doi.org/10.1017/S0025100314000267
.. _Unicode Normalization Form D (NFD): http://unicode.org/reports/tr15/
