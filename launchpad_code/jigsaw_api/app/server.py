# Server

from connexion import FlaskApp
from connexion.resolver import Resolver
from importlib.resources import files


class JigsawRevolver(Resolver):
    pass

def serve(host:str, port:int) -> None:
    spec_fn = files('jigsaw.openapi').joinpath('openapi.yaml')
    app = FlaskApp(__name__)
    app.add_api(spec_fn)
    app.run(host = host, port = port)