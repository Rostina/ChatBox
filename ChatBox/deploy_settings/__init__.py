import os
import dj_database_url

from ChatBox.settings import *
from ChatBox import custom_storages

from django.conf import settings
from storages.backends.s3boto import S3BotoStorage

from ChatBox import settings


class StaticStorage(S3BotoStorage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3BotoStorage):
    location = settings.MEDIAFILES_LOCATION



DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
    'localhost',
    '.herokuapp.com',
]

SECRET_KEY = get_env_variables("SECRET_KEY")

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

# STATICFILES_STORAGE = "whitenoise.django.GzipManifestStaticFilesStorage"


AWS_STORAGE_BUCKET_NAME = 'yyf-chatbox-bucket'
AWS_ACCESS_KEY_ID = 'AKIAIOSS67XBV6I5ZIBA'
AWS_SECRET_ACCESS_KEY = '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'

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

STATIC_URL = 'http://s3.amazonaws.com/%s' % AWS_STORAGE_BUCKET_NAME + '/'

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME



# STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
# STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
# ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

# STATICFILES_LOCATION = 'static'
# STATICFILES_STORAGE = 'StaticStorage'
# STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

# MEDIAFILES_LOCATION = 'media'
# MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
# DEFAULT_FILE_STORAGE = 'MediaStorage'
