# battlesnake-python

A simple [BattleSnake AI](http://battlesnake.io) written in Python. 

Visit [battlesnake.io/readme](http://battlesnake.io/readme) for API documentation and instructions for running your AI.

This AI client uses the [bottle web framework](http://bottlepy.org/docs/dev/index.html) to serve requests and the [gunicorn web server](http://gunicorn.org/) for running bottle on Heroku. Dependencies are listed in [requirements.txt](requirements.txt).

## You will need...

* a working `Python 3.x` development environment

* [pip](https://pip.pypa.io/en/latest/installing.html) to install Python dependencies


## Setup Snake Locally
1. Install virtualenv
```
pip install virtualenv
# if you dont have permissions or want to avoid sudo, can use the --user flag
pip install --user virtualenv
```

1. Setup a virtualenv, make sure you're at the root dir for this git repo
```
virtualenv -p <path to python 3 exe> default
```

1. Activate the virtualenv
```
source default/bin/activate
```

1. Install dependencies using [pip](https://pip.pypa.io/en/latest/installing.html)
```
pip install -r requirements.txt
```

1. Run local server
```
python app/main.py
```

1. If you need to change the default ip address or the port number, they are variables located in `app/bs_globals.py`


## Use ngrok to make local snake accessable by game server
1. Sign up at [ngrok.com](https://ngrok.com), it's free and you can use your Github Credentials for quick signup

1. Setup ngrok on your machine, [ngrok.com](https://ngrok.com/download)

1. Once setup, activate ngrok to tunnel your snake app
```
ngrok http <port of your app>
```

1. To double check to see if the tunnel is working, visit the ngrok url with the path to the snake's head image
```
<ngrok url>/static/head.png
```

1. Remember, when entering the ngrok url to the game board, make sure they're no trailing slash for your snake's url