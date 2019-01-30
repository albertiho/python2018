import sys
import json

with open(sys.argv[1]) as r:
  tiedosto = r.read().split('\n')

l = []
for x in tiedosto[:len(tiedosto) -1]:
  temp_l = x.split('\t')
  temp_d = {'country': temp_l[0], 'population': int(temp_l[1]), 'area': float(temp_l[2])}
  l.append(temp_d)
  
l.sort(key=lambda x: x['country'])

with open(sys.argv[2], 'w') as w:
  json.dump(l, w, indent=3, sort_keys=True)