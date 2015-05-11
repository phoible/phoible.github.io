---
layout: default
title:  "PHOIBLE"
---

This is the work-in-progress documentation website for the PHOIBLE database. Here is some IPA text for testing whether our webfont is loading correctly: `ɲ̊ⱱ̤̥ɐ̃̋`. Above are links to the various pages in this documentation; the footer contains links to various other websites associated with PHOIBLE.

# About PHOIBLE
PHOIBLE is a database of phonological inventories and distinctive features, encompassing more than 1600 languages (and growing). PHOIBLE data is published in browsable form at [PHOIBLE Online](http://phoible.org), which corresponds with the most recent year-numbered [release](https://github.com/phoible/phoible/releases) of [the development repository](https://github.com/phoible/phoible).

## Types of information available in PHOIBLE
Ideally, every phonological inventory in PHOIBLE would:

1. be published and citeable
2. describe all consonants, vowels, and tonemes
3. include information about major allophonic alternations

However, because PHOIBLE subsumes information from several pre-existing compilations of phonological inventories, not all inventories fully comply with the second and third criteria. Violations of the second criterion are limited to inventories that describe consonants and vowels but not tones; violations of the third criterion are discussed more fully below.

What this means is that, if you're interested in a typological analysis of vowel qualities, or only care about comparing consonant place of articulation cross-linguistically, you should feel confident in using all the data in PHOIBLE. If instead you care most about the ratio of lexical tone languages to non-tonal languages, you should first restrict yourself to only the sources with a “yes” in the Tone column of the table above. This is easily accomplished by filtering on the <span class="mono">Source</span> column.

If you're interested in analyzing allophones, a further issue is that there is no standard for what counts as a “major” allophonic alternation, and levels of allophonic detail will necessarily vary from author to author. In all cases, if a phonological description includes *some* information about allophonic alternations, it is assumed that phonemes with no allophones mentioned do not exhibit “major” allophonic variation (in the judgment of the original author(s) of the language description). For such phonemes, the sole allophone is treated as identical with the phonemic representation.

In phonological descriptions where *no* information about allophonic alternations was given about *any* of the phonemes, the description is considered incomplete with regard to allophonic information, and all phonemes of that inventory are given the value of <span class="mono">NA</span> for their allophones.

Here is a table summarizing the information available in the various data sources subsumed by PHOIBLE.

Source | Tone | Allophones | Notes
:------|:----:|:----------:|:------
UPSID  |  no  |     no     |
SAPHON |  no  |     no     | <span class="sm">No phonological analysis of tonemes. Includes boolean “tone/no tone” information, which is *not* incorporated into PHOIBLE.</span>
RA     |  no  |     no     |
SPA    |  yes |     yes    |
GM     |  yes |     yes    |
PH     |  yes |     yes    |

# How to cite PHOIBLE
If you are citing the database as a whole, or making use of the phonological distinctive feature systems in PHOIBLE, please cite as follows:
> Moran, Steven & McCloy, Daniel & Wright, Richard (eds.) 2014. PHOIBLE Online. Leipzig: Max Planck Institute for Evolutionary Anthropology. http://phoible.org.

If you are citing phoneme inventory data for a particular language or languages, please use the name of the language as the title, and include the original data source as an element within PHOIBLE. If possible also include the URL for the inventory being referenced. For example:
> UCLA Phonological Segment Inventory Database. 2014. Lelemi sound inventory (UPSID). In: Moran, Steven & McCloy, Daniel & Wright, Richard (eds.) PHOIBLE Online. Leipzig: Max Planck Institute for Evolutionary Anthropology. http://phoible.org/inventories/view/441.

If you are using the raw data from [the development repository](https://github.com/phoible/phoible) but are *not* using a [labeled release](https://github.com/phoible/phoible/releases), we recommend citing using the last commit hash at the time of your most recent cloning/forking of the repository, so that others can reproduce your work starting from the same snapshot of the repository that you are using. For example:
> Moran, Steven & McCloy, Daniel & Wright, Richard (eds.) 2015. PHOIBLE. https://github.com/phoible/phoible/commit/acebcf525998e5770b275c4049f05910887243cc
