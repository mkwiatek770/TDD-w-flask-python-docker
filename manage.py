from flask import Flask
from flask.cli import FlaskGroup

from src import app


cli = FlaskGroup(app)

if __name__ == '__main__':
    cli()
