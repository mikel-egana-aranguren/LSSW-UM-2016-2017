curl --data-urlencode query@UniProt-4 http://sparql.uniprot.org/sparql/
curl -H "Accept: text/csv" --data-urlencode query@UniProt-4 http://sparql.uniprot.org/sparql/
curl -H "Accept: application/sparql-results+xml" --data-urlencode query@UniProt-4 http://sparql.uniprot.org/sparql/
curl -H "Accept: application/sparql-results+json" --data-urlencode query@UniProt-4 http://sparql.uniprot.org/sparql/

curl -H "Accept: application/rdf+xml" --data-urlencode query@describe http://sparql.uniprot.org/sparql/
curl -H "Accept: text/turtle" --data-urlencode query@describe http://sparql.uniprot.org/sparql/

curl -H "Accept: application/rdf+xml" --data-urlencode query@describe http://sparql.uniprot.org/sparql/ > result.rdf
curl -H "Accept: application/rdf+xml" --data-urlencode query@describe http://sparql.uniprot.org/sparql/ | grep "GO_0008201" > result-go






