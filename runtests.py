import os
import django

from django.core.management import call_command


# path to envoy
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

django.conf.settings.configure(
    DEBUG=True,
    USE_TZ=True,
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
        }
    },
    INSTALLED_APPS=[
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sites",
        "ya_dancer",
    ],
    SITE_ID=1,
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'APP_DIRS': True,
            'OPTIONS': {
                "debug": True,  # We want template errors to raise
            },
        },
    ],
)

django.setup()

call_command('test')
