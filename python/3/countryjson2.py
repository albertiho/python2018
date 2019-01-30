import sys
import json

with open(sys.argv[1]) as r, open(sys.argv[2]) as g:
  maat, gdp = json.load(r), g.read().split('\n')
  
for x in gdp[:len(gdp)-1]:
  temp = x.split('\t')
  temp[1] = temp[1][1:]
  for z in maat:
    if z['country'] == temp[1]:
      z['gdp_per_capita'] = int(temp[2].replace(",",""))

for x in maat:
  try:
    x['gdp_per_capita']
  except:
    x['gdp_per_capita'] = "N/A"
    
maat.sort(key= lambda x: x['country'])

with open(sys.argv[3], 'w') as w:
  json.dump(maat, w, indent=3, sort_keys=True)