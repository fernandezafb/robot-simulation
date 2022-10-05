from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from camera import Camera
from constants import Constants


class Environment:
    def __init__(self, width, depth, robots):
        self._display_list_id = 0
        self._width = width
        self._depth = depth
        self._robots = robots
        self._camera = Camera()

    def get_robots(self):
        return self._robots

    def get_camera(self):
        return self._camera

    def center_x(self):
        return self._width / 2

    def center_z(self):
        return self._depth / 2

    def draw(self):
        glCallList(self._display_list_id)

    def create(self):
        """
        Creates the visual environment. It has two sides of an imaginary cube visible, inside which robots move.
        """
        self._display_list_id = glGenLists(1)
        glNewList(self._display_list_id, GL_COMPILE)
        light_position = [4, 3, 7, 1]
        glLightfv(GL_LIGHT0, GL_POSITION, light_position)
        glBegin(GL_QUADS)
        glNormal3d(0, 1, 0)

        for x in range(0, self._width - 1):
            for z in range(0, self._depth - 1):
                glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, Constants.WHITE)
                glVertex3d(x, 0, z)
                glVertex3d(x + 1, 0, z)
                glVertex3d(x + 1, 0, z + 1)
                glVertex3d(x, 0, z + 1)

                glVertex3d(0, x, z)
                glVertex3d(0, x + 1, z)
                glVertex3d(0, x + 1, z + 1)
                glVertex3d(0, x, z + 1)

        glEnd()
        glEndList()

    def create_empty(self):
        """
        Creates an empty visual environment without the visual sides of the imaginary cube.
        """
        self._display_list_id = glGenLists(1)
        glNewList(self._display_list_id, GL_COMPILE)
        glBegin(GL_QUADS)
        glNormal3d(0, 1, 0)
        glEnd()
        glEndList()

    def init_display_parameters(self, empty=False):
        """
        Sets up parameters for display and creates the visual environment.
        """
        glEnable(GL_DEPTH_TEST)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, Constants.WHITE)
        glLightfv(GL_LIGHT0, GL_SPECULAR, Constants.WHITE)
        glMaterialfv(GL_FRONT, GL_SPECULAR, Constants.WHITE)
        glMaterialf(GL_FRONT, GL_SHININESS, 30)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)

        if empty:
            self.create_empty()
        else:
            self.create()

    def display(self):
        """
        The display method sets a camera point and draws the imaginary cube and all the robots in the environment.
        """
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluLookAt(self._camera.get_x(), self._camera.get_y(), self._camera.get_z(),
                  self.center_x(), 0.0, self.center_z(),
                  0.0, 1.0, 0.0)

        self.draw()

        for robot in self._robots:
            robot.update()

        glFlush()
        glutSwapBuffers()
