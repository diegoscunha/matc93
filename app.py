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
	lingua = request.form['lingua']
	texto = request.form['texto']
	#texto = """He is best known as the author of MINIX, a free Unix-like operating system for teaching purposes, and for his computer science textbooks, regarded as standard texts in the field."""
	filtro = pln.remove_stopwords(texto)
	final = pln.refine(filtro)
	return render_template('teste.html')
	
if __name__ == '__main__':
	app.run(debug=True)