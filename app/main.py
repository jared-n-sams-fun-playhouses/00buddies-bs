import bottle
import os
import random

from pprint import (
    pprint,
    pformat
    )

from bs_globals import *
from get import *

"""
Main Functions
"""
@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.post('/start')
def start():
    data = bottle.request.json
    
    head_url = "%s://%s/static/head.png" % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
        )

    return {
        'color': '#6751AE',
        'taunt': get_taunt(),
        'head_url': head_url,
        'name': name
        }


@bottle.post('/move')
def move():
    data = bottle.request.json

    invalid_moves = get_invalid_points(data)

    us = get_our_snake(data)

    right = get_point_from_direction('right', us['coords'][0])

    print(get_direction_from_point(us['coords'][0], right))

    return {
        'move': 'right',
        'taunt': get_taunt()
        }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', ip_addr), port=os.getenv('PORT', port))
