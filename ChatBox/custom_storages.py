from django.conf import settings
from storages.backends.s3boto import S3BotoStorage

from ChatBox.deploy_settings import STATICFILES_LOCATION, MEDIAFILES_LOCATION


class StaticStorage(S3BotoStorage):
    location = STATICFILES_LOCATION


class MediaStorage(S3BotoStorage):
    location = MEDIAFILES_LOCATION
