from django.conf.urls import url

from .views import HealthCheckAllView
from .views import HealthCheckAppView
from .views import HealthCheckDatabaseView
from .views import HealthCheckElasticSearchView
from .views import HealthCheckMongoView
from .views import HealthCheckRedisView

urlpatterns = [
    url(r"^$", HealthCheckAllView.as_view(), name="health_check_status"),
    url(r"^db/$", HealthCheckDatabaseView.as_view(), name="health_check_db_status"),
    url(r"^redis/$", HealthCheckRedisView.as_view(), name="health_check__redis_status"),
    url(
        r"^elastic-search/$",
        HealthCheckElasticSearchView.as_view(),
        name="health_check_elasticsearch_status",
    ),
    url(
        r"^mongodb/$",
        HealthCheckMongoView.as_view(),
        name="health_check_mongodb_status",
    ),
    url(
        r"^app/$",
        HealthCheckAppView.as_view(),
        name="health_check_elasticsearch_status",
    ),
]
