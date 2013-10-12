import json

from django.http import HttpResponse


class JsonResponse(HttpResponse):

    def __init__(self, data, status=200):
        content = json.dumps(data, separators=(',', ':'))
        super(JsonResponse, self).__init__(
            content, content_type='application/json', status=status)


def like(request):
	return JsonResponse({'likeness': 1})
