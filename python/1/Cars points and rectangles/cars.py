class Car:
  def __init__(self, make, model, year, mileage):
    self.make = make
    self.model = model
    self.year = year
    self.mileage = mileage
    
  def __str__(self):
    return str("Make: {}\nModel: {}\nYear: {}\nMileage: {}\n".format(self.make, self.model, self.year, self.mileage))
    
def carsByYear(vals):
  s = sorted(vals, key=lambda x: (x.make, x.make, x.model))
  return sorted(s, key= lambda x: x.year, reverse=True)
  
def filterCars(cars, minyear, maxyear, minkm, maxkm):
  rlist = []
  for x in cars:
    if minyear <= x.year <= maxyear and minkm <= x.mileage <= maxkm:
      rlist.append(x)
  return sorted(rlist, key= lambda x: (x.make, x.model, x.year, x.mileage))