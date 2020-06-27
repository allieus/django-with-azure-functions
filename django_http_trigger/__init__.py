import sys
sys.path.insert(0, 'django_proj')

import azure.functions as func
from myproj.wsgi import application

wsgi = func.WsgiMiddleware(application)

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return wsgi.main(req, context)
