from flask import Flask
import connexion

def create_app():
    # init the connexion application
    app = connexion.App(__name__, specification_dir = '../openapi/')

    # load the open api spec
    app.add_api('openapi.yml')

    # get the flask app instance

    flask_app = app.app

    flask_app.config.from_object('app.config.Config')

    return flask_app