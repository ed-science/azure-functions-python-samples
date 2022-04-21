import os
import json

# Read Cosmosdb document given from ENV variable named 'inputCosmosdb' - Name for Input CosmosDB binding
inputCosmosdb = open(os.environ['inputCosmosdb'],'r').read()
print(inputCosmosdb)

# Deserialize inputCosmosdb (string) into JSON objects
docObjects = json.loads(inputCosmosdb)

# Dump documents
print(f"Document Count={len(docObjects)}")
for doc in docObjects:
    print(doc)
