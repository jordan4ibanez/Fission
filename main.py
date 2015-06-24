#Maybe call this game fission?

#have a way to rotate the map, or have a mini map

#have smooth node transition (walking from node to node)

#make some basic ai

#make a function for drawing objects/items on the grid

#this is currently programmed very poorly, i.e., everything is a global, functions are cluttered ->
#the notes are a mess

#do transition steps based on wether you're sneaking, walking, or running (1000,100,10)

import pygame

pygame.init();

size = width, height = 500, 500
screen = pygame.display.set_mode(size)

cube = 10               # this is the size of the grid nodes (Can be used to zoom/pan)
map_size = 20,20        # the size of the map (x,y)
offsetx,offsety = 10,10 # this moves the camera

playerx,playery = 0,0

grid = 1 #map zoom test

moving = False

transitionx,transitiony = 0,0
transition_step  = 0
transition_steps = 100

#node id table - if you add different lists, or sub lists to this, don't add before other ones so you don't break functions
id_table = [
# 0 ID   1 Walkable 
["floor", [True ],],
["wall",  [False],],
]
print(id_table[0])


#draw the grid (build up this method)
def drawgrid():
	for x in xrange(map_size[0]): 
		for y in xrange(map_size[1]):
			poly = (((x*cube)+offsetx,(y*cube)+offsety),((x*cube)+offsetx,(y*cube)+cube+offsety),((x*cube)+cube+offsetx,(y*cube)+cube+offsety),((x*cube)+cube+offsetx,(y*cube)+offsety));
			pygame.draw.polygon(screen, (255,255,255), poly)

#for drawing the player
def drawplayer(transition_step,moving,transitionx,transitiony,playerx,playery,cube):
	#do x steps of the transition
	transformx = 0
	transformy = 0
	#this is the smooth transition of the player
	if transition_step > 0:

		#print(((transition_steps/cube) * transition_step)/10)
		if transitionx > 0:
			transformx = ((((float(cube)/float(transition_steps)) * transition_step))-cube)*-1
		elif transitionx < 0:
			transformx = ((((float(cube)/float(transition_steps)) * transition_step))-cube)
		if transitiony > 0:
			transformy = ((((float(cube)/float(transition_steps)) * transition_step))-cube)*-1
		elif transitiony < 0:
			transformy = ((((float(cube)/float(transition_steps)) * transition_step))-cube)
		transition_step -= 1 
	elif moving == True:
		#print(transitionx,transitiony)
		playerx = playerx + transitionx
		playery = playery + transitiony
		transitionx,transitiony = 0,0
		moving = False
	playernode = (((playerx*cube)+offsetx+transformx,(playery*cube)+offsety+transformy),((playerx*cube)+offsetx+transformx,(playery*cube)+cube+offsety+transformy),((playerx*cube)+cube+offsetx+transformx,(playery*cube)+cube+offsety+transformy),((playerx*cube)+cube+offsetx+transformx,(playery*cube)+offsety+transformy));
	pygame.draw.polygon(screen, (255,0,0), playernode)
	return(transition_step,moving,transitionx,transitiony,playerx,playery)


#player movement events
def moveplayer(playerx,playery,moving,transitionx,transitiony,transition_step):
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.KEYDOWN:
			if moving == False:
				if event.key == pygame.K_LEFT:
					#playerx -= 1    -----MOVE PLAYER'S COORDS AFTER THE TRANSITION IS DONE
					transition_step = transition_steps
					moving = True
					transitionx = -1
					transitiony = 0
					transition_step = transition_steps
				elif event.key == pygame.K_RIGHT:
					#playerx += 1
					transition_step = transition_steps				
					moving = True
					transitionx = 1
					transitiony = 0
					transition_step = transition_steps
				elif event.key == pygame.K_UP:
					#playery -= 1
					transition_step = transition_steps
					moving = True
					transitionx = 0
					transitiony = -1
					transition_step = transition_steps
				elif event.key == pygame.K_DOWN:
					#playery += 1
					transition_step = transition_steps
					moving = True
					transitionx = 0
					transitiony = 1
					transition_step = transition_steps
	return(playerx,playery,moving,transitionx,transitiony,transition_step)

#standard pygame backend methods (i.e. leave game if escape, or close window)
def backend():
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE: #close the game if you hit escape
				exit()
	

#this is a test of the camera transition, say we need to zoom into the map for some reason, bam, now you can do that
def cameratest(cube,offsetx,offsety,grid):
	#camera testing
	################################
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
	################################
	return(cube,offsetx,offsety,grid)

while 1:
	screen.fill((0,0,0))
	
	#backend()
	drawgrid()
	transition_step,moving,transitionx,transitiony,playerx,playery = drawplayer(transition_step,moving,transitionx,transitiony,playerx,playery,cube)
	cube,offsetx,offsety,grid = cameratest(cube,offsetx,offsety,grid) #this is a test of the camera
	playerx,playery,moving,transitionx,transitiony,transition_step = moveplayer(playerx,playery,moving,transitionx,transitiony,transition_step)


	
	
	
	pygame.display.flip()	
