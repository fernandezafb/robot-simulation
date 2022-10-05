from OpenGL.GL import *

from abc import ABC, abstractmethod
from math import cos, sin
from constants import Constants


class Robot(ABC):

    @abstractmethod
    def __init__(self, s, c, h, x, z, move):
        self._half_size = s / 2
        self._color = c
        self._limit = Constants.LIMIT_ENVIRONMENT_LENGTH
        self._x = x
        self._y = h
        self._z = z
        self._direction = -1
        self._move = move
        self._theta = 0

    @abstractmethod
    def draw_robot(self):
        pass

    def draw(self):
        glPushMatrix()
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, self._color)
        glTranslated(self._x, self._y, self._z)

        self.draw_robot()

        glPopMatrix()

    def update(self):
        """
        Updates one of the robot coordinates to represent movements in the environment. Each specific robot moves
        in one way through one of the axis.
        """
        if self._move == 0:
            self.move_x()
        elif self._move == 1:
            self.move_y()
        elif self._move == 2:
            self.move_z()
        else:
            self.move_spiral()

        self.draw()

    def move_spiral(self):
        """
        Moves the robot drawing a spiral.
        """
        self._theta = self._theta + 0.02
        self._x = 5 * cos(self._theta)
        self._y = 5 * sin(self._theta)
        self._z += 0.01

        self.draw()

    def move_x(self):
        self._x += self._direction * 0.05
        if self._x > self._limit:
            self._x = self._limit
            self._direction = -1
        elif self._x < self._half_size:
            self._x = self._half_size
            self._direction = 1

    def move_y(self):
        self._y += self._direction * 0.05
        if self._y > self._limit:
            self._y = self._limit
            self._direction = -1
        elif self._y < self._half_size:
            self._y = self._half_size
            self._direction = 1

    def move_z(self):
        self._z += self._direction * 0.05
        if self._z > self._limit:
            self._z = self._limit
            self._direction = -1
        elif self._z < self._half_size:
            self._z = self._half_size
            self._direction = 1
