from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
from math import radians, cos, sin
import OpenGL.GL as gl
import OpenGL.GLUT as glut

x, y = -0.7, 0.6
deltax = 0.0
deltay = 0.0

# yuvarlak hareket hızı
speed = 0.1

whell_color=[0.0,0.0,0.0]    # Başlangıçta siyah renk

def init():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

def draw_bird():
    # yuvarlağı çizmek için 360 derece döngü yaparız
    glBegin(GL_POLYGON)
    for i in range(360):
        angle = radians(i)
        glVertex2f(x + cos(angle)*0.1, y + sin(angle)*0.1)
    glEnd()
def draw_box():
    glLineWidth(5.0)
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.9, -0.6)
    glVertex2f(-0.9, 0.9)
    glVertex2f(0.9, 0.9)
    glVertex2f(0.9, -0.6)
    glEnd()
def drawWheel(x, y):
    glColor3f(*whell_color)
    glPushMatrix()
    glTranslatef(x, y+0.05, 0.0)
    glutSolidSphere(0.07, 20, 20)
    glTranslatef(0.0, 0.0, 0.2)
    glutSolidSphere(0.07, 20, 20)
    glPopMatrix()
def draw_tree():
    glColor3f(0.5, 1.0, 0.5)
    glBegin(GL_QUADS)
    glVertex2f(-0.9, -0.6)
    glVertex2f(-0.9, -0.30)
    glVertex2f(0.9, -0.30)
    glVertex2f(0.9, -0.6)
    glEnd()
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 0.5,0.0)
    glVertex2f(0.3, 0.2)
    glVertex2f(0.7, 0.2)
    glVertex2f(0.5, 0.8)
    glEnd()
    glColor3f(0.6, 0.3, 0.0)
    glBegin(GL_QUADS)
    glVertex2f(0.45, 0.2)
    glVertex2f(0.55, 0.2)
    glVertex2f(0.55, -0.3)
    glVertex2f(0.45, -0.3)
    glEnd()


def draw_car():
    global top_color
    global bottom_color
    global x
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.5,1,1)
    glTranslatef(deltax, deltay, 0.0)
    glBegin(GL_QUADS)
    glVertex2f(-0.65, 0.0)
    glVertex2f(-0.65, 0.2)
    glVertex2f(-0.45, 0.2)
    glVertex2f(-0.45,0.0)

    glColor3f(0.5,0,0.5)
    glVertex2f(-0.3, 0.0)
    glVertex2f(-0.8, 0.0)
    glVertex2f(-0.8, -0.2)
    glVertex2f(-0.3, -0.2)
    glEnd()
    drawWheel(-0.7, -0.315)
    drawWheel(-0.4, -0.315)
    glLoadIdentity()
    glColor3f(0.0, 0.0, 0.0)
    draw_box()
    draw_tree()
    glColor3f(1.0, 0.5, 0.0)
    draw_bird()
    glutSwapBuffers()

    # yuvarlağı sağa doğru hareket ettir
    x += speed

    if x > 1.0:
        x = -1.0
    glutSwapBuffers()


def mouse(button, state, x, y):
    global deltax
    global deltay
    if button == glut.GLUT_LEFT_BUTTON and state == glut.GLUT_DOWN:
        if deltax < 0.7:
            deltax += 0.05
    elif button == glut.GLUT_RIGHT_BUTTON and state == glut.GLUT_DOWN:
        deltax -= 0.05
    glut.glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b"Araba")
    glutDisplayFunc(draw_car)
    glMatrixMode(GL_PROJECTION)
    glOrtho(-1, 1, -1, 1, -1, 1)
    glut.glutMouseFunc(mouse)
    init()
    glutMainLoop()


main()
