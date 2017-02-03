import os
from math import *

mapWidth  = 50; # The width  of the data file
mapHeight = 12;  # The height of the data file

mapData = [];

# Create the 2D map, initializing each element
for h in range(mapHeight) :
	mapData.append([])
	for x in range(mapWidth) :
		if abs(sin(x * 0.1) * cos(h * 0.1)) > 0.5 :
			mapData[h].append('#')
		else :
			mapData[h].append('.')


file = open('map0.txt', 'w');

# Write the map data to a file
for h in range(mapHeight) :
	line = '';
	for x in range(mapWidth) :
		line += mapData[h][x]

	file.write(line + '\n')

file.close()