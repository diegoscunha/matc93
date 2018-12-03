#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
from nltk.corpus import stopwords

stopwords_en = stopwords.words('english')
stopwords_pt = stopwords.words('portuguese')

def remove_stopwords(texto):
	# separando as palavras em tokens
	tokens = nltk.word_tokenize(texto)
	filtered_tokens = [word for word in tokens if word not in stopwords_en]
	return filtered_tokens

def refine(tokens):
	# NN   - Noun, singular or mass
	# NNS  - Noun, plural
	# NNP  - Proper noun, singular
	# NNPS - Proper noun, plural
	tokens_class = nltk.pos_tag(tokens)
	filtered_tokens = [clss[0] for clss in tokens_class if clss[1] in ['NN', 'NNS', 'NNP', 'NNPS']]
	return filtered_tokens