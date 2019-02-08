
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
