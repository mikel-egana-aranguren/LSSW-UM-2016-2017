import rdflib

def visit(uri,graph,count,maxcount):
  print "Visiting resource: ",uri  
  print count,maxcount,len(graph)
  if count < maxcount:
    try:
      g = rdflib.Graph()
      g.parse(uri)
      count += 1
      for subj, pred, obj in g:
	print "Obtained Triple: ",subj, pred, obj
	if (type(obj) == rdflib.term.URIRef):
	  graph.add(subj, pred, obj)
	  visit(str(obj),graph,count,maxcount)
    except:
      pass


# Config
uri = "http://purl.uniprot.org/uniprot/P05067"
size = 100
count = 0
maxcount = 2

graph = rdflib.Graph()
visit(uri,graph,count,maxcount)

print "Graph size: ", len(graph)
graph.serialize("result.ttl",format="turtle")


# and (str(pred) == "http://www.w3.org/2000/01/rdf-schema#seeAlso")
   


