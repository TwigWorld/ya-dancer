import json

from django.views.generic.base import View
from django.http import HttpResponse

from .models import HealthTable


class HealthCheckView(object):

    def _check_db(self):
        try:
            obj = HealthTable.objects.create(health_field="test")
            obj.health_field = "newtest"
            obj.save()
            obj.delete()
            return 'ok'
        except Exception, e:
            return str(e)

    def _default_dict(self):
        response_dict = {
            'app_status': 'ok'
        }
        return response_dict

    def _json_response(self, response_dict):
        response_json = json.dumps(response_dict)
        return HttpResponse(
            response_json,
            content_type='application/json'
        )        

class HealthCheckDatabaseView(HealthCheckView, View):

    def get(self, request, *args, **kwargs):
        response_dict = {'db': self._check_db()}
        return self._json_response(response_dict)

class HealthCheckAppView(HealthCheckView, View):

    def get(self, request, *args, **kwargs):
        response_dict = self._default_dict()
        return self._json_response(response_dict)

class HealthCheckElasticSearchView(HealthCheckView, View):
    pass

class HealthCheckRedisView(HealthCheckView, View):
    pass

class HealthCheckAllView(HealthCheckView, View):
    
    def get(self, request, *args, **kwargs):
        response_dict = self._default_dict()
        response_dict['db'] = self._check_db()
        return self._json_response(response_dict)

