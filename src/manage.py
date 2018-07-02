""" Entry point for the Application """

import os
import sys
import click

from app import create_app

app = create_app(environment=os.environ.get('APP_SETTINGS', 'Development'))

@app.cli.command()
@click.option('--coverage/--no-coverage', default=False, help='Enable code coverage')
def test(coverage):
    """ Run the unit tests """
    print('success')
    pass

@app.cli.command()
def create_database():
    """ Create database tables from sqlalchemy models """
    pass

@app.cli.command()
def drop_database():
    """ Drop database tables """
    pass

@app.cli.command()
def seed():
    """ Seed database tables with initial data """
    pass

