import rdflib

#g = rdflib.Graph()
#result = g.parse("http://purl.uniprot.org/uniprot/P05067")

g = rdflib.Graph()
result = g.parse("http://sameas.org/rdf?uri=http://identifiers.org/go/GO:0006915")



#g = rdflib.Graph()
#result = g.parse("http://sameas.org/rdf?uri=http://dbpedia.org/resource/London")

for subj, pred, obj in g:
   print subj, pred, obj
   
#g.serialize("result.ttl",format="turtle")