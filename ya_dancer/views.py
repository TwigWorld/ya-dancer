import json

from django.views.generic.base import View
from django.http import HttpResponse

from .models import HealthTable, MongoHealthDocument


class HealthCheckView(object):

    def _check_db(self):
        try:
            obj = HealthTable.objects.create(health_field="test")
            obj.health_field = "newtest"
            obj.save()
            obj.delete()
            return 'ok'
        except Exception as e:
            return str(e)

    def _check_mongo(self):
        try:
            import mongoengine as mongo
            all_connection_settings = mongo.connection._connection_settings

            for settings_key in mongo.connection._connection_settings.keys():
                connection_setting = all_connection_settings[settings_key]
                mongo.connect(
                    connection_setting['name'],
                    alias=settings_key,
                    host=connection_setting['host'],
                    port=connection_setting['port'],
                    username=connection_setting['username'],
                    password=connection_setting['password']
                )
                obj = MongoHealthDocument(health_field="newtest")
                obj.save()
                obj.delete()
                return 'ok'
        except Exception as e:
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


class HealthCheckMongoView(HealthCheckView, View):

    def get(self, request, *args, **kwargs):
        response_dict = {'mongo_db': self._check_mongo()}
        return self._json_response(response_dict)


class HealthCheckAllView(HealthCheckView, View):

    def get(self, request, *args, **kwargs):
        response_dict = self._default_dict()
        response_dict['db'] = self._check_db()
        if self.request.GET.get('mongodb', ''):
            response_dict['mongo_db'] = self._check_mongo()
        return self._json_response(response_dict)
