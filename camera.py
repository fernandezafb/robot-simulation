from math import cos, sin


class Camera:
    """Represents the static values of a camera, and implements methods to locate or move the camera.
    """

    def __init__(self):
        self._theta = 6
        self._y = 55
        self._dTheta = 0.05
        self._dy = 0.2

    def get_x(self):
        return 25 * cos(self._theta)

    def get_y(self):
        return self._y

    def get_z(self):
        return 25 * sin(self._theta)

    def move_right(self):
        self._theta += self._dTheta

    def move_left(self):
        self._theta -= self._dTheta

    def move_up(self):
        self._y += self._dy

    def move_down(self):
        if self._y > self._dy:
            self._y -= self._dy
