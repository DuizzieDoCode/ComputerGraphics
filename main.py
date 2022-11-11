from OpenGL.GL import *
from OpenGL.GLU import *

import random
import pygame
import os

from pygame.locals import *
from constants import *
from MeshRenderer import CubeMesh, ChairMesh, WineGlass

os.environ["SDL_VIDEO_CENTERED"]='1'


def random_color():
    x = random.randint(0, 255) / 255
    y = random.randint(0, 255) / 255
    z = random.randint(0, 255) / 255
    color = (x, y, z)
    return color

colors_list= []

for n in range(len(chair_faces_vector4)):
# for n in range(len(wine_faces_vector4)): 
    colors_list.append(random_color())


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL) 

    #Initialize a window or screen for display
    #create an OpenGL-renderable display

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    #gluPerspective( GLdouble ( fovy ) , GLdouble ( aspect ) , GLdouble ( zNear ) , GLdouble ( zFar ) )-> void

    glTranslatef(0.0, 0.0, -20) #multiply the current matrix by a translation matrix

    glRotatef(-90, 2, 0, 0)  #glRotate — multiply the current matrix by a rotation matrix


main()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    glRotatef(4, 3, -15, -45)

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    # ChairMesh()
    # CubeMesh()
    WineGlass()
    pygame.display.flip()
    pygame.time.wait(10)
pygame.quit()
quit()
