from decouple import config
import dj_database_url
from environ import Env
from pathlib import Path
from django.core.management.utils import get_random_secret_key
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
env = Env()
ENVIRONMENT = config('ENVIRONMENT')
if ENVIRONMENT == 'development':
  DEBUG = True
else:
  DEBUG = False


# Quick-start development settings - unsuitable for production
@@ -120,11 +114,6 @@
    },
]

POSTGRES_LOCALLY = True
database_url = env('DATABASE_URL', default='')
if database_url and (ENVIRONMENT == "production" or POSTGRES_LOCALLY == True):
  DATABASES['default'] = dj_database_url.parse(database_url)


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/
@@ -153,4 +142,12 @@
# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
