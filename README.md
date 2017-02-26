# battlesnake-python

A simple [BattleSnake AI](http://battlesnake.io) written in Python. 

Visit [battlesnake.io/readme](http://battlesnake.io/readme) for API documentation and instructions for running your AI.

This AI client uses the [bottle web framework](http://bottlepy.org/docs/dev/index.html) to serve requests and the [gunicorn web server](http://gunicorn.org/) for running bottle on Heroku. Dependencies are listed in [requirements.txt](requirements.txt).


#### You will need...

* a working `Python 3.x` development environment

* [pip](https://pip.pypa.io/en/latest/installing.html) to install Python dependencies

## Running the Snake Locally

1. Install dependencies using [pip](https://pip.pypa.io/en/latest/installing.html):
```
pip install -r requirements.txt
```

1. Run local server:
```
python app/main.py
```
