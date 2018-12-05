#!/usr/bin/env python
# -*- coding: utf-8 -*-

from SPARQLWrapper import SPARQLWrapper, JSON

def consutar_termos(uri, termos, idioma):
	sparql = SPARQLWrapper(uri)
	list_querys = {}
	try:
		for t in termos:
			query = """
					PREFIX dbr: <http://dbpedia.org/resource/>
					PREFIX dbp: <http://dbpedia.org/property/>	
					PREFIX dct: <http://purl.org/dc/terms/>
					
					SELECT DISTINCT(?subject) ?termo
					WHERE
					{
						?subject dct:subject dbc:Computer_systems_researchers .
						?subject dbo:abstract ?termo
						FILTER (regex(?termo, "%s", "i"))
						FILTER (LANG(?termo) = "%s")
					} LIMIT 1
					"""%(t, idioma)
		
			sparql.setQuery(query)
			sparql.setReturnFormat(JSON)
			result = sparql.query().convert()
			list_querys[t] = parse(result['results']['bindings'])
	except Exception as error:
		raise Exception("Error :{}".format(str(error)))
		
	return list_querys
	
def parse(value):
	r = {}
	
	for v in value:
		r['subject'] = v['subject']['value'].split('/')[-1]
		r['uri'] = v['subject']['value']
		r['abstract'] = v['termo']['value']
	return r