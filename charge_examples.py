import math

from fizyka import ChargePoint
# kolory
background_colour = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)
PURPLE = (118,0,142)
color = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)

systemNiceTwo = [ChargePoint(-0.5, 0, 20, BLUE, 700000), ChargePoint(0.5, 0, 20, RED, 700000)]
systemNiceTwo[0].y_vel = 12500
systemNiceTwo[1].y_vel = -12500

minus2 = [ChargePoint(-0.5, 0, 15, BLUE, -12), ChargePoint(0.5, 0, 15, BLUE, -12)]

plus2 = [ChargePoint(-0.5, 0, 15, RED, 12), ChargePoint(0.5, 0, 15, RED, 12)]

opossite = [ChargePoint(-0.5, 0, 15, BLUE, -12), ChargePoint(0.5, 0, 15, RED, 12)]

charge_grid = []
for x in range(50):
    radius = 7
    charge_grid.append(ChargePoint(-1.4 + 0.048*x, -1.4 + 0.48*(x%5), radius, RED, 3))
    charge_grid.append(ChargePoint(-1.3 + 0.040*x, -1.3 + 0.40*(x%5), radius, BLUE, -3))

tempo_grid = []
for charge in range(50):
    radius = 7
    tempo = 500

    x1 = -1.4 + 0.048*charge
    y1 = -1.4 + 0.48*(charge%5)
    charge_point = ChargePoint(x1, y1, radius, RED, 3)
    charge_point.y_vel = tempo*y1
    charge_point.x_vel = -tempo*x1

    x2= -1.3 + 0.040 * charge
    y2 = -1.3 + 0.40 * (charge % 5)
    charge_point1 = ChargePoint(x2, y2 , radius, BLUE, -3)
    charge_point1.y_vel = tempo * y2
    charge_point1.x_vel = -tempo * x2


    tempo_grid.append(charge_point1)
    tempo_grid.append(charge_point)








examples = [[minus2, "Dwa ujemne"], [plus2, "Dwa dodadnie"], [opossite, "Dwa przeciwne"], [charge_grid, "Sieć"],
            [tempo_grid, "Szybka sieć"]]