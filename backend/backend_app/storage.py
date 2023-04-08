import sys

from django.utils.deconstruct import deconstructible
from storages.backends.s3boto3 import S3Boto3Storage
from django_hashedfilenamestorage.storage import HashedFilenameMetaStorage
from django.conf import settings


def get_location():
    return settings.TEST_DIR if "test" in sys.argv else "media"


@deconstructible
class CustomS3Boto3Storage(S3Boto3Storage):
    bucket_name = settings.YANDEX_BUCKET_NAME
    location = get_location()


HashedFilenameS3Boto3Storage = HashedFilenameMetaStorage(
    storage_class=CustomS3Boto3Storage
)
