import pygame
import math

WORLD = {
    "width": 320,
    "height": 640,
    "fps": 30
}

UI = {
    "color": {
        "white": pygame.Color("#FFFFFF"),
        "black": pygame.Color("#000000"),
        "blue": pygame.Color("#4169E1"),
        "red": pygame.Color("#CA0202"),
        "green": pygame.Color("#81a963"),
        "purple": pygame.Color("#021f95"),
        "orange": pygame.Color("#d57318"),
        "grey": pygame.Color("#5E706A"),
        "yellow": pygame.Color("#DBA334"),
        "border": pygame.Color("#A9A9A9")
    }
}

GRID = {
    "cell": 32,
    "rows": math.floor(WORLD['height'] / 32),
    "cols": math.floor(WORLD['width'] / 32),
    "drop_timer": 1
}

# Shapes
from shapes import *

SHAPE = [
    BlueShape,
    RedShape,
    GreenShape,
    PurpleShape,
    OrangeShape,
    GreyShape,
    YellowShape
]