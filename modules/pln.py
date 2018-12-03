#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
from nltk.corpus import stopwords

def remove_stopwords(texto, idioma):
	# separando as palavras em tokens
	tokens = nltk.word_tokenize(texto)
	if idioma=='pt':
		stopwords_txt = stopwords.words('portuguese')
	else:
		stopwords_txt = stopwords.words('english')
	filtered_tokens = [word for word in tokens if word not in stopwords_txt]
	return filtered_tokens

def refine(tokens):
	# NN   - Noun, singular or mass
	# NNS  - Noun, plural
	# NNP  - Proper noun, singular
	# NNPS - Proper noun, plural
	tokens_class = nltk.pos_tag(tokens)
	filtered_tokens = [clss[0] for clss in tokens_class if clss[1] in ['NN', 'NNS', 'NNP', 'NNPS']]
	return filtered_tokens