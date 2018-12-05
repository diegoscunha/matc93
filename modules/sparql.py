#!/usr/bin/env python
# -*- coding: utf-8 -*-

from SPARQLWrapper import SPARQLWrapper, JSON

def consutar_termos(uri, termos, idioma):
	sparql = SPARQLWrapper(uri)
	#list_querys = []
	list_querys = {}
	try:
		for t in termos:
			query = """
					SELECT DISTINCT(?subject) ?termo
					WHERE
					{
						?subject dct:subject ?comp .
						?subject dbo:abstract ?termo
						FILTER (regex(str(?comp), "Comput", "i") && regex(?termo, "%s", "i"))
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
		
	
'''
sparql = SPARQLWrapper('http://dbpedia.org/sparql')

query = """
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX : <http://dbpedia.org/resource/>
PREFIX dbpedia2: <http://dbpedia.org/property/>
PREFIX dbpedia: <http://dbpedia.org/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT DISTINCT(?subject) ?termo
WHERE
{
    ?subject dct:subject ?comp .
    ?subject dbo:abstract ?termo
    FILTER (regex(?comp, "Comput", "i") && regex(?termo, "%s", "i"))
    FILTER (LANG(?termo) = "%s")
} LIMIT 1
"""%('MINIX', 'en')

sparql.setQuery(query)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

print(results['results']['bindings'])
'''