import collisions
import data
import vector_math
import math

def cast_ray(ray, sphere_list, amb, light, eye_point):
	result_color = data.Color(1.0, 1.0, 1.0)
	#test for closest sphere to the eye
	collision_tuple = find_closest_collision(ray, sphere_list)
	if collision_tuple:
		#some useful variables
		sphere_hit = collision_tuple[0]
		sphere_hit_point = collision_tuple[1]
		#basic color before manipulation
		result_r = sphere_hit.color.r * sphere_hit.finish.amb * amb.r
		result_g = sphere_hit.color.g * sphere_hit.finish.amb * amb.g
		result_b = sphere_hit.color.b * sphere_hit.finish.amb * amb.b
		#computing light intensity
		sphere_vector = vector_math.vector_from_to(sphere_hit.center, sphere_hit_point)
		sphere_normal = vector_math.normalize_vector(sphere_vector)
		
		scaled_normal = vector_math.scale_vector(sphere_normal, 0.01)
		hit_point = vector_math.translate_point(sphere_hit_point, scaled_normal)
		
		light_vector = vector_math.vector_from_to(hit_point, light.pt)
		light_normal = vector_math.normalize_vector(light_vector)
		
		light_scale = vector_math.dot_vector(sphere_normal, light_normal)
		
		if light_scale > 0:
			sphere_normal_ray = data.Ray(hit_point, light_normal)
			possible_obstruction = find_closest_collision(sphere_normal_ray, sphere_list)
			if possible_obstruction == None or distance(hit_point, possible_obstruction[1]) > distance(hit_point, light.pt):
				result_r += sphere_hit.color.r * light_scale * light.color.r * sphere_hit.finish.diff
				result_g += sphere_hit.color.g * light_scale * light.color.g * sphere_hit.finish.diff
				result_b += sphere_hit.color.b * light_scale * light.color.b * sphere_hit.finish.diff
		
		#computing specular intensity
		tmp_vector = vector_math.scale_vector(sphere_normal, 2 * light_scale)
		reflection_vector = vector_math.difference_vector(light_normal, tmp_vector)
		
		eye_vector = vector_math.vector_from_to(eye_point, hit_point)
		eye_normal = vector_math.normalize_vector(eye_vector)
		
		spec_scale = vector_math.dot_vector(reflection_vector, eye_normal)
		
		if spec_scale > 0:
		
			result_r += light.color.r * sphere_hit.finish.spec * spec_scale ** (1 / float(sphere_hit.finish.rough))
			result_g += light.color.g * sphere_hit.finish.spec * spec_scale ** (1 / float(sphere_hit.finish.rough))
			result_b += light.color.b * sphere_hit.finish.spec * spec_scale ** (1 / float(sphere_hit.finish.rough))
		
		result_color = data.Color(result_r, result_g, result_b)
	return result_color

def cast_all_rays(view, eye_point, sphere_list, amb, light, file):
	j = view.max_y
	while j > view.min_y:
		i = view.min_x
		while i < view.max_x:
			screen_point = data.Point(i, j, 0)
			dir_to_pixel = vector_math.vector_from_to(eye_point, screen_point)
			ray = data.Ray(eye_point, dir_to_pixel)
			color = cast_ray(ray, sphere_list, amb, light, eye_point)
			printed_r = str(color_convert(color.r))
			printed_g = str(color_convert(color.g))
			printed_b = str(color_convert(color.b))
			file.write("{0} {1} {2}\n".format(printed_r, printed_g, printed_b))
			i += find_delta(view.min_x, view.max_x, view.width)
		j -= find_delta(view.min_y, view.max_y, view.height)

def find_delta(min, max, length):
	return (max - min)/float(length)

def distance(p1, p2):
	vector = vector_math.vector_from_to(p1, p2)
	return vector_math.length_vector(vector)

def find_closest_collision(ray, sphere_list):
	collision_list = collisions.find_intersection_points(sphere_list, ray)
	if collision_list:
		closest_sphere_index = 0
		for i in range(1, len(collision_list)):
			if distance(ray.pt, collision_list[i][1]) < distance(ray.pt, collision_list[closest_sphere_index][1]):
				closest_sphere_index = i
		return collision_list[closest_sphere_index]
	else:
		return None

def color_convert(color_component):
	result_color = 255
	if color_component < 1:
		result_color = int(color_component * 255)
	return result_color
