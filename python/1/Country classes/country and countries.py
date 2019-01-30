class Country:
  def __init__(self, name, population, area):
    self.name = name
    self.population = int(population)
    self.area = float(area)


class Countries:
  d_all = []
  
  def __init__(self, vals):
    with open(vals) as r:
      tiedosto = r.read().split('\n')
    for line in tiedosto[:-1]:
      temp = line.split('\t')
      self.d_all.append(Country(temp[0], temp[1], temp[2]))
      
  def size(self):
    return len(self.d_all)
    
  def list(self):
    return sorted(self.d_all, key= lambda x: x.name)