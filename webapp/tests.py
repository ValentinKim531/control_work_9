import json
from datetime import datetime
from django.http import HttpResponse


def json_echo_view(request, *args, **kwargs):
    answer = {
        'time': datetime.now().strftime('%m-%d %H:%M:%S'),
        'method': request.method,
    }
    answer_as_json = json.dumps(answer)
    response = HttpResponse(answer_as_json)
    response['Content-Type'] = 'application/json'
    return response