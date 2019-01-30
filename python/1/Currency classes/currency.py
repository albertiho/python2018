import sys

class Currency:
  def __init__(self, name, fullName, euroRate):
    self.name = name
    self.fullName = fullName
    self.euroRate = float(euroRate)
    
def loadCurrencies(vals):
  with open(vals) as r:
    tiedosto = r.read().split('\n')
  rval = {}
  for x in tiedosto[:len(tiedosto) -1]:
    temp = x.split('\t')
    c = Currency(temp[0], temp[1], temp[3])
    rval[temp[0]] = c
  return rval

if __name__ == "__main__":
  temp = loadCurrencies(sys.argv[1])
  for q in sorted(temp, key= lambda x: temp[x].fullName):
    print(temp[q].fullName)