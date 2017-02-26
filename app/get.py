import random

from bs_globals import *


def get_taunt():
    return random.choice(taunts)


def get_invalid_points(data):
    bad_coords = []

    for snake in data['snakes']:
        bad_coords.extend(snake['coords'])

    if debug:
        print("Invalid Points: %s" % bad_coords)

    return bad_coords


def get_our_snake(data):
    for snake in data['snakes']:
        if name == snake['name']:
            return snake
    else:
        return {}


def get_direction_from_point(head, point):
    directions = {
        'up'   : [head[0], (head[1] - 1)],
        'down' : [head[0], (head[1] + 1)],
        'left' : [(head[0] - 1), head[1]],
        'right': [(head[0] + 1), head[1]]
        }

    for key, coord in directions.items():
        if point == coord:
            return key


def get_point_from_direction(move, point):
    return {
        'up'   : [point[0], (point[1] - 1)],
        'down' : [point[0], (point[1] + 1)],
        'left' : [(point[0] - 1), point[1]],
        'right': [(point[0] + 1), point[1]]
        }.get(move, point)