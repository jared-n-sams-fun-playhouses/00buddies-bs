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
        print('func:%r args:[%r, %r] took: %2.8f msec' % \
            (f.__name__, args, kw, (te-ts) * 1000))
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

@timing
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
    return {
        'up'   : [point[0], (point[1] - 1)],
        'down' : [point[0], (point[1] + 1)],
        'left' : [(point[0] - 1), point[1]],
        'right': [(point[0] + 1), point[1]]
        }.get(move, point)