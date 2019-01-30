import sys
import string

with open(sys.argv[1]) as f:
  population = f.read().split('\n')
with open(sys.argv[2]) as q:
  area = q.read().split('\n')
  
  d = {}
  for i in range(len(population) -1):
    apu = population[i].split('\t')
    d[apu[0]] = [int(apu[1].replace(",",""))]

  for i in range(len(area) -1):
    apu= area[i].split('\t')
    l = d[apu[0]]
    l.append(float(apu[1].replace(",","")))
    
  toWrite = ""
  for x in sorted(d):
    l = d[x]
    toWrite = toWrite + ("{}\t{}\t{}\n".format(x, l[0], l[1]))
    
with open(sys.argv[3], "w+") as w:
  w.write(toWrite)