import json
import regex as re

def intersperse(lst, item):
    result = [item] * (len(lst) * 2 - 1)
    result[0::2] = lst
    return result

with open ('movies.json', "r") as f:
    data = json.load(f)

print(type(data))
fixed_list = intersperse(data,{"index":{}})

j = json.dumps(fixed_list, indent=0)
with open('letssee.json', 'w') as f:
    f.write(j)
    f.close

f = open("letssee.json", "r")
a = f.read()

a = a.replace("},", "}")
with open('movies.txt', 'w') as f:
    f.write(a)




""""
b = json.loads(a)
j = json.dumps(b, indent=4)
with open('fixex_bulk_elastic.json', 'w') as f:
    f.write(j)
    f.close

j = json.dumps(fixed_list, indent=0)
with open('letssee.json', 'w') as f:
    f.write(j)
    f.close"""


#b = json.loads(a)
#j = json.dumps(b, indent=4)
#with open('fixex_bulk_elastic.json', 'w') as f:
    #f.write(j)
    #f.close