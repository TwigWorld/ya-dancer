import json

from django.views.generic.base import View
from django.http import HttpResponse

from .models import HealthTable


class HealthCheckView(View):

    def check_db(self):
        try:
            obj = HealthTable.objects.create(health_field="test")
            obj.health_field = "newtest"
            obj.save()
            obj.delete()
            return {
                'status': 'ok',
                'error': ''
            }
        except Exception, e:
            return {
                'status': 'fail',
                'error': str(e)
            }

    def get(self, request, *args, **kwargs):
        response_dict = {
            'app_status': 'ok',
            'db': self.check_db()
        }

        response_json = json.dumps(response_dict)

        return HttpResponse(
            response_json,
            content_type='application/json'
        )
