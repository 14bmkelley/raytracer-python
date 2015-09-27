from math import sqrt
import data

def scale_vector(vector, scalar):
   return data.Vector(scalar * vector.x, scalar * vector.y, scalar * vector.z)

def dot_vector(vector1, vector2):
   return vector1.x * vector2.x + vector1.y * vector2.y + vector1.z * vector2.z

def length_vector(vector):
   return sqrt(vector.x ** 2 + vector.y ** 2 + vector.z ** 2)

def normalize_vector(vector):
   mag = float(length_vector(vector))
   return data.Vector(vector.x / mag, vector.y / mag, vector.z / mag)

def difference_point(point2, point1):
   return data.Vector(point2.x - point1.x, point2.y - point1.y, point2.z - point1.z)

def difference_vector(vector2, vector1):
   return data.Vector(vector2.x - vector1.x, vector2.y - vector1.y, vector2.z - vector1.z)

def translate_point(point, vector):
   return data.Point(point.x + vector.x, point.y + vector.y, point.z + vector.z)

def vector_from_to(from_point, to_point):
   return data.Point(to_point.x - from_point.x, to_point.y - from_point.y, to_point.z - from_point.z)
