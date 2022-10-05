import argparse

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from random import uniform, randint
from robot import Robot
from environment import Environment
from constants import Constants


class Ball(Robot):
    def __init__(self, s, c, h, x, z, move=randint(0, 2)):
        super().__init__(s, c, h, x, z, move)

    def draw_robot(self):
        glutSolidSphere(self._half_size, 30, 30)


class Cube(Robot):
    def __init__(self, s, c, h, x, z, move=randint(0, 2)):
        super().__init__(s, c, h, x, z, move)

    def draw_robot(self):
        glutSolidCube(self._half_size, 30, 30)


def create_ball_robots(number):
    """
    Creates the given number of Ball robots.
    """
    half_size = Constants.ROBOT_SIZE / 2
    return [Ball(Constants.ROBOT_SIZE,
                 Constants.GREEN,
                 round(uniform(0 + half_size, Constants.LIMIT_ENVIRONMENT_LENGTH - half_size), 2),
                 round(uniform(0 + half_size, Constants.LIMIT_ENVIRONMENT_LENGTH - half_size), 2),
                 round(uniform(0 + half_size, Constants.LIMIT_ENVIRONMENT_LENGTH - half_size), 2)
                 ) for i in range(number)
            ]


def create_cube_robots(number):
    """
    Creates the given number of Cube robots.
    """
    half_size = Constants.ROBOT_SIZE / 2
    return [Cube(Constants.ROBOT_SIZE,
                 Constants.MAGENTA,
                 round(uniform(0 + half_size, Constants.LIMIT_ENVIRONMENT_LENGTH - half_size), 2),
                 round(uniform(0 + half_size, Constants.LIMIT_ENVIRONMENT_LENGTH - half_size), 2),
                 round(uniform(0 + half_size, Constants.LIMIT_ENVIRONMENT_LENGTH - half_size), 2)
                 ) for i in range(number)
            ]


def reshape(w, h):
    """
    Sets up the perspective that fits the window
    """
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(40.0, w / h, 1.0, 150.0)
    glMatrixMode(GL_MODELVIEW)


def timer(v):
    """
    Draws next frame.
    """
    glutPostRedisplay()
    glutTimerFunc(int(1000 / 60), timer, v)


def main():
    """
    Main section of the program. Creates the visual environment with the robots and initializes OpenGL.
    """

    parser = argparse.ArgumentParser(description='Robots Simulation')
    parser.add_argument('--spiral', action='store_true', help='A boolean to show a Robot moving in spiral')
    args = parser.parse_args()

    if args.spiral:
        environment = Environment(Constants.LIMIT_ENVIRONMENT_LENGTH,
                                  Constants.LIMIT_ENVIRONMENT_LENGTH,
                                  [Ball(Constants.ROBOT_SIZE, Constants.GREEN, 0, 0, 0, 3)])
    else:
        environment = Environment(Constants.LIMIT_ENVIRONMENT_LENGTH,
                                  Constants.LIMIT_ENVIRONMENT_LENGTH,
                                  create_ball_robots(10) + create_cube_robots(20))

    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowPosition(80, 80)
    glutInitWindowSize(1280, 720)
    glutCreateWindow("Robots Simulation")
    glutDisplayFunc(environment.display)
    glutReshapeFunc(reshape)
    glutTimerFunc(100, timer, 0)
    environment.init_display_parameters(True if args.spiral else False)
    glutMainLoop()


if __name__ == '__main__':
    main()
