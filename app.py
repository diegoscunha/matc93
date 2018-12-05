#!/usr/bin/env python
# -*- coding: utf-8 -*-

from modules import pln, sparql

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
	
	try:
		resultado = sparql.consutar_termos('http://dbpedia.org/sparql', final, idioma)
	except Exception as error:
		print(str(error))
		return render_template('error.html', error=str(error)), 200
		
	texto = preparar_texto(texto, resultado)
	return render_template('resultado.html', resultado=resultado, texto=texto)
	
def preparar_texto(texto, tokens):
	for item in tokens:
		texto = texto.replace(item, '<span class="tag is-success">' + item + '</span>')
	return texto
	
if __name__ == '__main__':
	app.run(debug=True)