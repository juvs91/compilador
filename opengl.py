#!/usr/bin/env python2.3
# * 3-D gear wheels.  This program is in the public domain.
# * Brian Paul
# * Conversion to GLUT by Mark J. Kilgard 
# conversion to Python using PyOpenGL with frame rates ala glxgears
# Peter Barth
import OpenGL 
OpenGL.ERROR_ON_COPY = True 
from OpenGL.GL import *
from OpenGL.GLUT import *
import sys, time 
from math import sin,cos,sqrt,pi
from OpenGL.constants import GLfloat
vec4 = GLfloat_4
#the x starting from the origin
x_pos = 0                      
#the y starting from the origin
y_pos = 0        
#the angle that is alway looking ot the top of the window
angle = 0                                              
#the variable that tells if it can draw 
can_draw = True     

#the colors that the user want to use 

#red
red = 0
#green
green =0
#blue
blue = 0





def square(size):
	global x_pos,y_pos
	if(can_draw):
		use_color()   
		
		glBegin(GL_QUADS)
		glVertex2f(x_pos,y_pos)
		glVertex2f(x_pos+size, y_pos)
		glVertex2f(x_pos+size, y_pos+size)
		glVertex2f(x_pos,y_pos+size) 
		glEnd()
	

def fd(size):#need to check for the rotation angle 
	global x_pos,y_pos 
	end_point_x =x_pos + size * cos(angle) 
	end_point_y =y_pos + size * sin(angle)
	print x_pos,y_pos,end_point_x,end_point_y
	if(can_draw):    
		print "entro"
		use_color()   
		glBegin(GL_LINES)
		glVertex2f(end_point_y,end_point_x)
		glVertex2f(y_pos,x_pos)
		glEnd()
	x_pos = end_point_x
	y_pos = end_point_y
	
def circle(radious): 
	global x_pos,y_pos
	if(can_draw):    
		use_color()
		glBegin(GL_TRIANGLE_FAN)
		glVertex2f(x_pos,y_pos)
		for angle in range(360):
			glVertex2f(sin(angle)*radious, cos(angle)*radious)
		glEnd()
	
	
def rt(rotation):
	global angle
	if(angle+rotation >= 360):
		angle = angle+rotation - 360
	else:
		angle = angle + rotation

def pd():
	can_draw = True
                   
def pu():
	can_draw = False 
	
def home():
	global x_pos,y_pos
	x_pos = 0;
	y_pos = 0;   
	
def color(red_in,gree_in,blue_in):
	global red,green,blue
	red = red_in
	green = green_in
	blue = blue_in
	
def use_color():    
	global red,gree,blue
	glColor4f( red , green , blue , 0 )
	
def brush(color,size): 
	pass
	
	
	
def arc(x,y):
	pass

def init():
	glEnable(GL_DEPTH_TEST)
	 
	glOrtho(-400, 400,-300, 300,-100,100)


def draw():      
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	
	glClearColor(1,1,1,1)#DEFINE EL COLOR DEL FONDO DE TU PANTALLA 
	fd(30)
	rt(90)  
	fd(30)
	#circle(100)
	glutSwapBuffers()  

	
	
def main():
	
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
	glutInitWindowPosition(0, 0)
	glutInitWindowSize(800, 600)
	glutCreateWindow("pyGears")
	
	init()                    
	
	glutDisplayFunc(draw)
	
	glutMainLoop()
	


if __name__ == '__main__':
    main()
    
