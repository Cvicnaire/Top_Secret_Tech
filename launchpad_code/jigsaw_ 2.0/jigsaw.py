# Workflow Orchestrator Testing Version

from flask import Flask, request
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version = '1.0', title = 'capella',
        description = ' An Api for processing requested data and composing workflows')

# defining the namespace

ns = api.namespace('process', description = 'Data processing operations')

data_model = api.model('Data', {
    'key1': fields.String(required=True, description = 'The first key'),
    'key2': fields.String(required=True, description = 'The second key')
})

# Defining the resource
@ns.route('/')
class ProcessData(Resource):
    @ns.expect(data_model)
    @ns.doc('process_data')
    def post(self):
        ''' Process the input data and return the result '''
        data = api.payload
        processed_data = {
            "processed_key1": data['key1'],
            "processed_key2": data['key2']
        }
        return processed_data, 200

# adding the namespace to the API
api.add_namespace(ns)

if __name__ == '__main__': 
        app.run(port = 5002, debug = True)
