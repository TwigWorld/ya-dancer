from django.conf.urls import patterns, url

from .views import HealthCheckView


urlpatterns = patterns('',
    url(r'^$', HealthCheckView.as_view(), name='health_check_status'),
)
