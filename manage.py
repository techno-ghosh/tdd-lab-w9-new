# manage.py adding comment content to check auto restarting of the server.
from flask.cli import FlaskGroup
from src import app
cli = FlaskGroup(app)
if __name__ == '__main__':
 cli()