class Point2D:

  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def __str__(self):
    return str("Point2D(x={:3.1f}, y={:3.1f})".format(self.x, self.y))
    
class Rectangle:
  
  def __init__(self, p1=Point2D(), p2=Point2D()):
    if (p1.x < p2.x):
      ll_x = p1.x
      ur_x = p2.x
    else:
      ll_x = p2.x
      ur_x = p1.x
    if(p1.y < p2.y):
      ll_y = p1.y
      ur_y = p2.y
    else:
      ll_y = p2.y
      ur_y = p1.y
      
    self.ll = Point2D(ll_x, ll_y)
    self.ur = Point2D(ur_x, ur_y)
      
  def __str__(self):
    return str("Rectangle(ll={}, ur={})".format(str(self.ll), str(self.ur)))
  