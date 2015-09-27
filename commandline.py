from data import Point, Color, View, Light

def get_eye_point(argv):
	if '-eye' in argv:
		flag_index = argv.index('-eye')
		try:
			x = float(argv[flag_index + 1])
		except:
			print "eye_point x value incorrectly defined... using default"
			x = 0
		try:
			y = float(argv[flag_index + 2])
		except:
			print "eye_point y value incorrectly defined... using default"
			y = 0
		try:
			z = float(argv[flag_index + 3])
		except:
			print "eye_point z value incorrectly defined... using default"
			z = -14
		eye_point = Point(x, y, z)
	else:
		eye_point = Point(0, 0, -14)
	return eye_point

def get_view(argv):
	if '-view' in argv:
		flag_index = argv.index('-view')
		try:
			min_x = float(argv[flag_index + 1])
		except:
			print "view min_x value incorrectly defined... using default"
			min_x = -10
		try:
			max_x = float(argv[flag_index + 2])
		except:
			print "view max_x value incorrectly defined... using default"
			max_x = 10
		try:
			min_y = float(argv[flag_index + 3])
		except:
			print "view min_y value incorrectly defined... using default"
			min_y = -7.5
		try:
			max_y = float(argv[flag_index + 4])
		except:
			print "view max_y value incorrectly defined... using default"
			max_y = 7.5
		try:
			width = float(argv[flag_index + 5])
		except:
			print "view width value incorrectly defined... using default"
			width = 1024
		try:
			height = float(argv[flag_index + 6])
		except:
			print "view height value incorrectly defined... using default"
			height = 768
		view = View(min_x, max_x, min_y, max_y, width, height)
	else:
		view = View(-10, 10, -7.5, 7.5, 1024, 768)
	return view

def get_light(argv):
	if '-light' in argv:
		flag_index = argv.index('-light')
		try:
			x = float(argv[flag_index + 1])
		except:
			print "light x value incorrectly defined... using default"
			x = -100
		try:
			y = float(argv[flag_index + 2])
		except:
			print "light y value incorrectly defined... using default"
			y = 100
		try:
			z = float(argv[flag_index + 3])
		except:
			print "light z value incorrectly defined... using default"
			z = -100
		try:
			r = float(argv[flag_index + 4])
		except:
			print "light r value incorrectly defined... using default"
			r = 1.5
		try:
			g = float(argv[flag_index + 5])
		except:
			print "light g value incorrectly defined... using default"
			g = 1.5
		try:
			b = float(argv[flag_index + 6])
		except:
			print "light b value incorrectly defined... using default"
			b = 1.5
		light = Light(Point(x, y, z), Color(r, g, b))
	else:
		light = Light(Point(-100, 100, -100), Color(1.5, 1.5, 1.5))
	return light

def get_ambient(argv):
	if '-ambient' in argv:
		flag_index = argv.index('-ambient')
		try:
			r = float(argv[flag_index + 1])
		except:
			print "ambient r value incorrectly defined... using default"
			r = 1
		try:
			g = float(argv[flag_index + 2])
		except:
			print "ambient g value incorrectly defined... using default"
			g = 1
		try:
			b = float(argv[flag_index + 3])
		except:
			print "ambient b value incorrectly defined... using default"
			b = 1
		ambient = Color(r, g, b)
	else:
		ambient = Color(1, 1, 1)
	return ambient
