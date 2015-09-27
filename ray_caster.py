from sys import argv, stdout
from data import Point, Color, Finish, Sphere
from commandline import get_eye_point, get_view, get_light, get_ambient
from cast import cast_all_rays

def main():
	sphere_list = []
	
	#try to open file or throw error
	try:
		input_file = open(argv[1], "r")
	except:
		print "Error: Filename not correctly specified"
		print "Usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height"
		exit()
	
	#try to instantiate spheres from argv inputs or throw error
	line_count = 0
	for line in input_file:
		line_count += 1
		try:
			params = line.split()
			x = float(params[0])
			y = float(params[1])
			z = float(params[2])
			rad = float(params[3])
			r = float(params[4])
			g = float(params[5])
			b = float(params[6])
			amb = float(params[7])
			diff = float(params[8])
			spec = float(params[9])
			rough = float(params[10])
			sphere = Sphere(Point(x, y, z), rad, Color(r, g, b), Finish(amb, diff, spec, rough))
			sphere_list.append(sphere)
		except:
			print "malformed sphere on line {0} ... skipping".format(str(line_count))
	
	#initialize casting variables relative to argv inputs
	eye_point = get_eye_point(argv)
	view = get_view(argv)
	light = get_light(argv)
	ambient = get_ambient(argv)
	
	#write to image.ppm output image
	file = open("image.ppm", "w")
	file.write("P3\n")
	file.write("{0} {1}\n".format(str(view.width), str(view.height)))
	file.write("{0}\n".format(str(255)))
	cast_all_rays(view, eye_point, sphere_list, ambient, light, file)
	file.close()

if __name__ == "__main__":
	main()
