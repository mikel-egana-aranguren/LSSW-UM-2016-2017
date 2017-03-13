import rdflib

def visit(uri,graph,count,maxcount):
  print "Visiting resource: ",uri  
  print count,maxcount
  if count < maxcount:
  #if len(graph) < size:
    graph.parse(uri)
    count += 1
    for subj, pred, obj in graph:
      print "Obtained Triple: ",subj, pred, obj
      if (type(obj) == rdflib.term.URIRef):
	visit(str(obj),graph,count,maxcount)


# Config
uri = "http://purl.uniprot.org/uniprot/P05067"
size = 100
count = 0
maxcount = 10

graph = rdflib.Graph()
visit(uri,graph,count,maxcount)

print "Graph size: ", len(graph)
graph.serialize("result.ttl",format="turtle")


# uri != "http://www.w3.org/2000/01/rdf-schema-more"
   


