import json
import regex as re

f = open("movies2.json", "r")
a = f.read()

a = a.replace("},", "}")
with open('movies.txt', 'w') as f:
    f.write(a)
#b = json.loads(a)
#j = json.dumps(b, indent=4)
#with open('fixex_bulk_elastic.json', 'w') as f:
    #f.write(j)
    #f.close