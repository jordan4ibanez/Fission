#Maybe call this game fission?

#have a way to rotate the map, or have a mini map

#have smooth node transition (walking from node to node)

#make some basic ai



import pygame

pygame.init();

size = width, height = 500, 500
screen = pygame.display.set_mode(size)

cube = 10               # this is the size of the grid nodes (Can be used to zoom/pan)
map_size = 20,20        # the size of the map (x,y)
offsetx,offsety = 10,10 # this moves the camera

grid = 1 #map zoom test

while 1:
	screen.fill((0,0,0))
	
	#camera testing
	if cube >= 20:
		grid = -1
	elif cube <= 10:
		grid = 1
	if grid == 1:
		cube += 0.01
		offsetx += 0.1
		offsety += 0.1
	elif grid == -1:
		cube -= 0.01
		offsetx -= 0.1
		offsety -= 0.1
	
		
	for x in xrange(map_size[0]): 
		for y in xrange(map_size[1]):

			poly = (((x*cube)+offsetx,(y*cube)+offsety),((x*cube)+offsetx,(y*cube)+cube+offsety),((x*cube)+cube+offsetx,(y*cube)+cube+offsety),((x*cube)+cube+offsetx,(y*cube)+offsety));
			pygame.draw.polygon(screen, (255,255,255), poly)
	
	
	
	
	pygame.display.flip()	
