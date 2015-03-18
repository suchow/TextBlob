# -*- coding: utf-8 -*-
"""Wordnet interface. Contains classes for creating Synsets and Lemmas
directly.

.. versionadded:: 0.7.0

"""
from nltk.corpus import wordnet

#: Synset constructor
Synset = wordnet.synset
#: Lemma constructor
Lemma = wordnet.lemma
# Part of speech constants
VERB, NOUN, ADJ, ADV = wordnet.VERB, wordnet.NOUN, wordnet.ADJ, wordnet.ADV
