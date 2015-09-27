from utility import epsilon_equal

class Point(object):
   '''
   A class to define a point in space.
   Attributes:
   x --> float
   y --> float
   z --> float
   '''
   def __init__(self, x, y, z):
      self.x = x
      self.y = y
      self.z = z
   def __eq__(self, other):
      return (epsilon_equal(self.x, other.x) 
		  and epsilon_equal(self.y, other.y) 
		  and epsilon_equal(self.z, other.z))

class Vector(object):
   '''
   A class to define a vector in space.
   Attributes:
   x --> float
   y --> float
   z --> float
   '''
   def __init__(self, x, y, z):
      self.x = x
      self.y = y
      self.z = z
   def __eq__(self, other):
      return (epsilon_equal(self.x, other.x) 
		  and epsilon_equal(self.y, other.y) 
		  and epsilon_equal(self.z, other.z))

class Ray(object):
   '''
   A class to define a ray in space.
   Attributes:
   pt --> Point (object)
   dir --> Vector (object)
   '''
   def __init__(self, pt, dir):
      self.pt = pt
      self.dir = dir
   def __eq__(self, other):
      return (epsilon_equal(self.pt.x, other.pt.x) 
		  and epsilon_equal(self.pt.y, other.pt.y) 
		  and epsilon_equal(self.pt.z, other.pt.z) 
		  and epsilon_equal(self.dir.x, other.dir.x) 
		  and epsilon_equal(self.dir.y, other.dir.y) 
		  and epsilon_equal(self.dir.z, other.dir.z))

class Sphere(object):
   '''
   A class to define a sphere in space.
   Attributes:
   center --> Point (object)
   radius --> float
   color  --> Color (object)
   finish --> Finish (object)
   '''
   def __init__(self, center, radius, color, finish):
      self.center = center
      self.radius = radius
      self.color = color
      self.finish = finish

   def __eq__(self, other):
      return (epsilon_equal(self.center.x, other.center.x) 
          and epsilon_equal(self.center.y, other.center.y) 
          and epsilon_equal(self.center.z, other.center.z) 
          and epsilon_equal(self.radius, other.radius) 
          and epsilon_equal(self.color.r, other.color.r) 
          and epsilon_equal(self.color.g, other.color.g) 
          and epsilon_equal(self.color.b, other.color.b)
		  and epsilon_equal(self.finish.amb, other.finish.amb)
          and epsilon_equal(self.finish.diff, other.finish.diff)
          and epsilon_equal(self.finish.spec, other.finish.spec)
          and epsilon_equal(self.finish.rough, other.finish.rough))

class Color(object):
   '''
   A class to define a Color.
   Attributes:
   r --> float
   g --> float
   b --> float
   '''
   def __init__(self, r, g, b):
      self.r = r
      self.g = g
      self.b = b
   def __eq__(self, other):
      return (epsilon_equal(self.r, other.r) 
		  and epsilon_equal(self.g, other.g) 
		  and epsilon_equal(self.b, other.b))

class Finish(object):
   '''
   A class to define a finish to spheres
   Attirbutes:
   amb   --> float
   diff  --> float
   spec  --> float
   rough --> float
   '''
   def __init__(self, amb, diff, spec, rough):
      self.amb = amb
      self.diff = diff
      self.spec = spec
      self.rough = rough
   def __eq__(self, other):
      return (epsilon_equal(self.amb, other.amb) 
          and epsilon_equal(self.diff, other.diff)
          and epsilon_equal(self.spec, other.spec)
          and epsilon_equal(self.rough, other.rough))

class Light(object):
   '''
   A class to define a light source
   Attributes:
   pt    --> Point (object)
   color --> Color (object)
   '''
   def __init__(self, pt, color):
      self.pt = pt
      self.color = color
   def __eq__(self, other):
      return (epsilon_equal(self.pt.x, other.pt.x)
          and epsilon_equal(self.pt.y, other.pt.y)
          and epsilon_equal(self.pt.z, other.pt.z)
          and epsilon_equal(self.color.r, other.color.r)
          and epsilon_equal(self.color.g, other.color.g)
          and epsilon_equal(self.color.b, other.color.b))

class View(object):
   '''
   A class to define a view of the 3D world
   Attributes:
   min_x  --> float
   max_x  --> float
   min_y  --> float
   max_y  --> float
   width  --> float
   height --> float
   '''
   def __init__(self, min_x, max_x, min_y, max_y, width, height):
      self.min_x = min_x
      self.max_x = max_x
      self.min_y = min_y
      self.max_y = max_y
      self.width = width
      self.height = height
   def __eq__(self, other):
      return (epsilon_equal(self.min_x, other.min_x)
          and epsilon_equal(self.max_x, other.max_x)
          and epsilon_equal(self.min_y, other.min_y)
          and epsilon_equal(self.max_y, other.max_y)
          and epsilon_equal(self.width, other.width)
          and epsilon_equal(self.height, other.height))
