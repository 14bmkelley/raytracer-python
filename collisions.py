import math
from vector_math import *

def sphere_intersection_point(ray, sphere):
	origin_diff = difference_point(ray.pt, sphere.center)
	A = dot_vector(ray.dir, ray.dir)
	B = dot_vector(scale_vector(origin_diff, 2), ray.dir)
	C = dot_vector(origin_diff, origin_diff) - sphere.radius ** 2
	
	determinant = B ** 2 - 4 * A * C
	
	def get_point_from_root(t):
		return translate_point(ray.pt, scale_vector(ray.dir, t))
		
	if determinant >= 0:
		root1 = (-B + math.sqrt(determinant)) / (2.0 * A)
		root2 = (-B - math.sqrt(determinant)) / (2.0 * A)
		if root1 >= 0 and root2 >= 0:
			if root1 == root2:
				return get_point_from_root(root1)
			else:
				if root1 < root2:
					return get_point_from_root(root1)
				else:
					return get_point_from_root(root2)
		elif root1 >= 0 or root2 >= 0:
			if root1 >= 0:
				return get_point_from_root(root1)
			else:
				return get_point_from_root(root2)
		else:
			return None
	else:
		return None

def find_intersection_points(sphere_list, ray):
	return [(sphere, sphere_intersection_point(ray, sphere)) for sphere in sphere_list if sphere_intersection_point(ray, sphere) != None]

def sphere_normal_at_point(sphere, point):
	return normalize_vector(vector_from_to(sphere.center, point))
