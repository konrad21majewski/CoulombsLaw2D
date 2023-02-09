import pygame
import math

WIDTH, HEIGHT = 800, 800

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)

class ChargePoint:
    CM = 0.01  # CM = 0.01M
    k = 8.99 * (10 ** 9) #Coulumbs constant
    SCALE = 250 / CM  # 1CM = 100 pixels
    TIMESTEP = 1 * (10**(-6))  # 1µs - slowdown

    def __init__(self, x, y, promien, kolor, charge):
        self.x = x * ChargePoint.CM
        self.y = y * ChargePoint.CM
        self.promien = promien
        self.kolor = kolor
        self.charge = charge * 10 ** (-9)
        self.orbit = []

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x, y))

            pygame.draw.lines(win, self.kolor, False, updated_points, 2) # rysowanie toru ruchu

        pygame.draw.circle(win, self.kolor, (x, y), self.promien) #rysowanie koła


    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        force = self.k * self.charge * other.charge / distance ** 2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_position(self, planets):
        total_fx = total_fy = 0
        # obliczanie wektora siły Fx i Fy dla wybranego punktowego ładunku
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += - total_fx / abs(self.charge) * self.TIMESTEP
        self.y_vel += - total_fy / abs(self.charge) * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))