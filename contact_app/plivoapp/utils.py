
import simplejson
from django.http import HttpResponse

class JSONResponse(HttpResponse):
    """
        JSON response
    """
    def __init__(self, content, status=None, content_type='application/json'):

        if not isinstance(content, str):
            content = simplejson.dumps(content)
        super(JSONResponse, self).__init__(
            content=content,
            status=status,
            content_type=content_type,
        )
        
def authenticate_request(*params):
    def decorater_maker(fn):
        @functools.wraps(fn)
        def wrapper(request, *args, **kwargs):
            if isinstance(request, HttpRequest):
                request_dict = request.__getattribute__(request.method)
                for param in params:
                    if not request_dict.get(param, None):
                        return render_error_response(
                            400,
                            "Missing field '%s' in request" % param)
            return fn(request, *args, **kwargs)

        return wrapper

    return decorater_maker 
