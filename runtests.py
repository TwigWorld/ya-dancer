import os
import django

from django.core.management import call_command


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

django.conf.settings.configure(
    DEBUG=True,
    USE_TZ=True,
    INSTALLED_APPS=[
        "ya_dancer",
    ],
    ROOT_URLCONF='ya_dancer.urls',
)

django.setup()

call_command('test')
