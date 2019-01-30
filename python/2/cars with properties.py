class Car:
  __slots__ = ["__make","__model","__year","__mileage"]
  
  def __init__(self, make, model, year, mileage):
    self.__make = make
    self.__model = model
    self.__year = year
    self.mileage = mileage
   
  # getters
  def get_make(self):
    return self.__make
    
  def get_model(self):
    return self.__model
    
  def get_year(self):
    return self.__year
    
  def get_mileage(self):
    return self.__mileage
    
  # setters
  def set_mileage(self, val):
    self.__mileage = val
  
  # properties
  make = property(get_make)
  model = property(get_model)
  year = property(get_year)
  mileage = property(get_mileage, set_mileage)
  
  def __str__(self):
    return str("Make: {}\nModel: {}\nYear: {}\nMileage: {}\n".format(self.make, self.model, self.year, self.mileage))
    
  def __lt__(self, val):
    if self.make < val.make:
      return True
    elif self.make == val.make:
      if self.model < val.model:
        return True
      elif self.model == val.model:
        if self.year < val.year:
          return True
        elif self.year == val.year:
          if self.mileage < val.mileage:
            return True
    return False
    
  def __eq__(self, val):
    return self.make == val.make and self.model == val.model and self.year == val.year