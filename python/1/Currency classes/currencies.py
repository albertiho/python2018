import sys

class Currencies:
  
  cd = {}
  
  def __init__(self, vals):
    with open(vals) as r:
      tiedosto = r.read().split('\n')
    for x in tiedosto[:len(tiedosto) -1]:
      temp = x.split('\t')
      self.cd[temp[0]] = [temp[0], temp[1], float(temp[2]), float(temp[3])]
  
  def listByName(self):
    for q in sorted(self.cd, key= lambda x: self.cd[x]):
      print("{} {}".format(self.cd[q][0], self.cd[q][3]))
      
  def listByRate(self):
    for q in sorted(self.cd, key= lambda x: (self.cd[x][3], self.cd[x][0])):
      print("{} {}".format(self.cd[q][0], self.cd[q][3]))
      
  def convert(self, currA, x, currB):
    return float(self.cd[currA][3] * x * self.cd[currB][2])