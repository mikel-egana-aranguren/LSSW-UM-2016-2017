# LSSW-UM-2016-2017
Life Sciences Semantic Web (Máster Bioinformática UM 2016 2017) 

## Enlaces

Slides: http://slides.com/mikel-egana-aranguren/lssw-um-16-17#/

Live: http://slides.com/mikel-egana-aranguren/lssw-um-16-17/live

Speaker: http://slides.com/mikel-egana-aranguren/lssw-um-16-17/speaker

## Linked Data Server

Blazegraph Triple Store. Go to `LinkedDataServer/blazegraph` and:

`java -server -Djetty.port=8081 -jar bigdata-bundled.jar`

Upload data at `http://localhost:8081/bigdata/`

Pubby. Go to `LinkedDataServer/pubby` and (Watch out for `conf:webBase`, `conf:sparqlEndpoint`, `conf:datasetBase`, and `conf:webResourcePrefix`!):

`java -jar start.jar jetty.port=8080`

Then go to http://localhost:8080/resource/Prot_A




