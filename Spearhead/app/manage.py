import click
from flask.cli import with_appcontext


@click.command("init")
@with_appcontext
def init():
    """Create a new admin user"""
    from app.extensions import db
    from app.models import User

    click.echo("create user")
    user = User(username="Cvicnaire", email="camv@bu.edu", password="89Summer", active=True)
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")
