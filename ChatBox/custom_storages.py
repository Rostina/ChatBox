from django.conf import settings
from storages.backends.s3boto import S3BotoStorage

from ChatBox import deploy_settings


class StaticStorage(S3BotoStorage):
    location = deploy_settings.STATICFILES_LOCATION


class MediaStorage(S3BotoStorage):
    location = deploy_settings.MEDIAFILES_LOCATION
