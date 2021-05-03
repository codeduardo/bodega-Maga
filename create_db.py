import click
from flask.cli import with_appcontext
from app.migrate import init_db


@click.command(name='create_tables')
@with_appcontext
def create_tables():
    init_db()
