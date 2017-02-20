import os
import dj_database_url

from ChatBox.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
    'localhost',
    '.herokuapp.com',
]

SECRET_KEY = get_env_variables("SECRET_KEY")

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

ARTIFILES_STORAGE = "whitenoise.django.GzipManfestStaticFileStorage"


AWS_ACCESS_KEY_ID = 'AKIAIOSS67XBV6I5ZIBA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'yyf-chatbox-bucket'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# STATIC_URL = "https://yyf-chatbox-bucket.s3.amazonaws.com/"
# ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
