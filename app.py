#!/usr/bin/env python
# -*- coding: utf-8 -*-

from modules import pln

from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route("/")
def index(): 
	return render_template('index.html')
	
@app.route("/analisar", methods=['POST'])
def analisar():
	idioma = request.form['idioma']
	texto = request.form['texto']
	#texto = """He is best known as the author of MINIX, a free Unix-like operating system for teaching purposes, and for his computer science textbooks, regarded as standard texts in the field."""
	filtro = pln.remove_stopwords(texto, idioma)
	final = pln.refine(filtro)
	
	# modelo do resultado da consulta sparql
	resultado = dict([('MINIX','MINIX (from "mini-Unix") is a POSIX-compliant (since version 2.0), Unix-like computer operating system based on a microkernel architecture. Early versions of MINIX were created by Andrew S. Tanenbaum for educational purposes. Starting with MINIX 3, the primary aim of development shifted from education to the creation of a highly reliable and self-healing microkernel OS.'), 
					  ('operating system','An operating system (OS) is system software that manages computer hardware and software resources and provides common services for computer programs.'), 
					  ('computer','A computer is a device that can be instructed to carry out sequences of arithmetic or logical operations automatically via computer programming.'), 
					  ('science','Science (from Latin scientia, meaning "knowledge") is a systematic enterprise that builds and organizes knowledge in the form of testable explanations and predictions about the universe.'), 
					  ('textbooks','A textbook or coursebook (UK English) is a manual of instruction in any branch of study. Textbooks are produced according to the demands of educational institutions. Schoolbooks are textbooks and other books used in schools.')])
	
	texto = preparar_texto(texto, resultado)
	return render_template('resultado.html', resultado=resultado, texto=texto)

def preparar_texto(texto, tokens):
	for item in tokens:
		texto = texto.replace(item, '<span class="tag is-success">' + item + '</span>')
	return texto
	
if __name__ == '__main__':
	app.run(debug=True)