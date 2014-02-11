import json

from django.views.generic.base import View
from django.http import HttpResponse


class HealthCheckView(View):

	def get(self, request, *args, **kwargs):
		response_dict = {
				'app_status': 'ok'
		}

		response_json = json.dumps(response_dict)

		return HttpResponse(
            response_json,
            content_type='application/json'
        )		
