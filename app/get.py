import random

from bs_globals import *

from functools import wraps
from time import time


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print(te-ts)
        print('func:%r took: %0.5f msec' % \
            (f.__name__, (te-ts) * 1000.0))
        return result
    return wrap


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
    if point[0] == head[0]:
        if (point[1] + 1) == head[1]:
            return 'up'
        if (point[1] - 1) == head[1]:
            return 'down'

    if point[1] == head[1]:
        if (point[0] + 1) == head[0]:
            return 'left'
        if (point[0] - 1) == head[0]:
            return 'right'


def get_point_from_direction(move, point):
    if move == 'up':
        return [point[0], (point[1] - 1)]

    if move == 'down':
        return [point[0], (point[1] + 1)]

    if move == 'left':
        return [(point[0] - 1), point[1]]

    if move == 'right':
        return [(point[0] + 1), point[1]]

    return point
