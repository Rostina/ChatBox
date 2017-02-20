import os
import dj_database_url

from ChatBox.settings import *
from ChatBox import custom_storages


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


AWS_ACCESS_KEY_ID = 'AKIAIOSS67XBV6I5ZIBA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'yyf-chatbox-bucket'

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
# ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
