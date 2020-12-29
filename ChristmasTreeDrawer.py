import pygame
from pygame.locals import *
from random import *
from time import *
import sys

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
ORNAMENT_RADIUS = 10

def getWidthLength(height, smallHeight, width):
	return int((smallHeight / height) * width)

def randomPointOnTree(triangles):
	t1, t2, t3 = triangles

	#random point between highest and lowest point on the tree
	height = randint(t1[0][1] + ORNAMENT_RADIUS, t3[2][1] - ORNAMENT_RADIUS)

	if (height < t1[1][1]):
		triangleHeight = t1[1][1] - t1[0][1]
		triangleWidth = t1[2][0] - t1[1][0]
		widthLength = getWidthLength(triangleHeight, height - t1[0][1], triangleWidth)
	elif (height < t2[1][1]):
		triangleHeight = t2[2][1] - t1[2][1]
		triangleWidth = t2[2][0] - t2[1][0]
		widthLength = getWidthLength(triangleHeight, height - t1[2][1], triangleWidth)
	else:
		triangleHeight = t3[2][1] - t2[2][1]
		triangleWidth = t3[2][0] - t3[1][0]
		widthLength = getWidthLength(triangleHeight, height - t2[2][1], triangleWidth)

	i1 = SCREEN_WIDTH // 2 - widthLength // 2 + ORNAMENT_RADIUS
	i2 = SCREEN_WIDTH // 2 + widthLength // 2 - ORNAMENT_RADIUS

	if (i1 < i2):
		width = randint(i1, i2)
	else:
		width = randint(i2, i1)

	return width, height

def drawOneOrnament(screen, center):
	#get random color ovdje 
	red = (175, 50, 50)
	pygame.draw.circle(screen, red, center, ORNAMENT_RADIUS, 0)

def drawOrnaments(screen, triangles):
	for i in range(10):
		point = randomPointOnTree(triangles)
		drawOneOrnament(screen, point)
	pygame.display.flip()

def drawTriangle(screen, pointA, pointB, pointC):
	green = (70, 125, 71)
	pygame.draw.polygon(screen, green, [pointA, pointB, pointC], 0)

def findTrianglePoints(widthFraction, upperHeightFraction, lowerHeightFraction):
	pointA = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / upperHeightFraction)
	pointB = (SCREEN_WIDTH / widthFraction, SCREEN_HEIGHT / lowerHeightFraction)
	pointC = (SCREEN_WIDTH - SCREEN_WIDTH / widthFraction, SCREEN_HEIGHT / lowerHeightFraction)
	return pointA, pointB, pointC

def findRect(lowerHeightFraction):
	width = SCREEN_WIDTH / (20 / 3)
	height = SCREEN_HEIGHT / 6
	left = SCREEN_WIDTH / 2 - (width / 2)
	top = SCREEN_HEIGHT / lowerHeightFraction
	return (left, top, width, height)

def drawTree(screen, fractions):
	brown = (100, 75, 45)
	rect = findRect(fractions[2][2])
	pygame.draw.rect(screen, brown, rect, 0)

	triangles = []

	for i in range(3):
		f1, f2, f3 = fractions[i]
		pointA, pointB, pointC = findTrianglePoints(f1, f2, f3)
		triangles.append((pointA, pointB, pointC))
		drawTriangle(screen, pointA, pointB, pointC)
		
	pygame.display.flip()
	return triangles

def closeOnX():
	while True:
		for events in pygame.event.get():
			if events.type == QUIT:
				sys.exit(0)

def main():
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	screen.fill((0,0,0))

	# determines where are the triangles in regard to screen size
	fractions = [(4, 8, 3), (6, 4, 2), (8, 12/5, 3/2)]

	triangles = drawTree(screen, fractions)
	drawOrnaments(screen, triangles)
	closeOnX()

main()					