import yaml
from openapi_core import OpenAPIRequest, OpenAPIResponse
from openapi_core.spec import Spec
from openapi_core.validator import Validator
from abc import ABC, abstractmethod


# Loading the OpenApi spec from YAML file


with open('openapi.yaml', 'r') as file:
    spec_dict = yaml.safe_load(file)
spec = Spec(**spec_dict)


# Set up the OpenApi validator

validator = Validator(spec)

# define abstract baseclass for handling each endpoint


class EndpointHandler(ABC):

    @abstractmethod
    def available_workflows(self, request: OpenAPIRequest) -> OpenAPIResponse:
        pass

    @abstractmethod
    def process_requests(self, request: OpenAPIRequest) -> OpenAPIResponse:
        pass

    @abstractmethod
    def ping_hippo_avail_resources(self, request: OpenAPIRequest) -> OpenAPIResponse:
        pass

    @abstractmethod
    def ping_hippo_missing_resources(self, request: OpenAPIRequest) -> OpenAPIResponse:
        pass

    @abstractmethod
    def ping_hippo_notify(self, request: OpenAPIRequest) -> OpenAPIResponse:
        pass

    @abstractmethod
    def ping_workflow_manager(self, request: OpenAPIRequest) -> OpenAPIResponse:
        pass

def no_implementation(request: OpenAPIRequest) -> OpenAPIResponse:
    return OpenAPIResponse

def ConcreteEndpointHandler(EndpointHandler):

    def available_workflows(self, request: OpenAPIRequest) -> OpenAPIResponse:
        # Logic Implementation

        return OpenAPIResponse(data = {"workflows":['wgbs', 'RNA-Seq']}, status_code = 200)

def handle_request(request: OpenAPIRequest) -> OpenAPIResponse:
    try:
        validator.validate(request)
        endpoint = request.path
        handler = EndpointHandler()

        # compute the appropriate method name given the endpoint

        stem, endpoint = endpoint[1].split('/')
        method_name = f"handle_{stem}_{endpoint}"

        if not hasattr(handler, method_name): 
        
        method = getattr(handler, method_name)

        if endpoint == "/available-workflows":
            return handler.available_workflows(request)
        
        elif endpoint == "/process-requests":
            return handler.process_requests(request)
        
        elif endpoint == "/ping-hippo-avail-resources":
            return handler.ping_hippo_avail_resources(request)
        
        elif endpoint == "/ping-hippo-missing-resources":
            return handler.ping_hippo_missing_resources(request)
        
        elif endpoint == "/ping-hippo-notify":
            return handler.ping_hippo_notify(request)
        
        elif endpoint == "/ping-workflow-manager":
            return handler.ping_workflow_manager(request)
        
        else:
            return OpenAPIResponse(status_code = 404)
        
    except Exception as e:

        return OpenAPIResponse(body = str(e), status_code = 500)