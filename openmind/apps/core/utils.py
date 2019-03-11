import logging
import magic
import boto3
from botocore.exceptions import ClientError
from django.conf import settings
from rest_framework.serializers import Serializer


_logger = logging.getLogger(__name__)
_s3 = boto3.client(
    's3',
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name=settings.AWS_S3_REGION
)


def validate_data(schema_cls: Serializer, data: dict) -> dict:
    """Validate data using Marshmallow schema

    Return validated data if success, raise ValidationError if failed
    """
    schema = schema_cls(data=data)
    schema.is_valid(raise_exception=True)
    return schema.validated_data


def upload_file(bucket, name, file_obj) -> str:
    """Upload File to AWS S3 and return image url"""
    try:
        _s3.upload_fileobj(file_obj, bucket, name)
        url = 'https://{bucket}.s3.amazonaws.com/{name}'.format(bucket=bucket, name=name)
        return url
    except ClientError as err:
        _logger.error(err)
        raise err


def upload_image(name, file_obj) -> str:
    """Upload Image (JPG/PNG) to AWS S3 and return image url"""
    return upload_file(settings.AWS_S3_BUCKET_IMAGE, name, file_obj)


def upload_audio(name, file_obj) -> str:
    """Upload Audio/Video to AWS S3 and return image url"""
    return upload_file(settings.AWS_S3_BUCKET_STREAMING, name, file_obj)


def get_mimetype(file_obj) -> bool:
    buffer = file_obj.read()
    mimetype = magic.from_buffer(buffer, mime=True)
    file_obj.seek(0)
    return mimetype


def is_valid_audio_mimetype(file_obj) -> bool:
    mimetype = get_mimetype(file_obj)
    return mimetype.startswith('audio')


def is_valid_video_mimetype(file_obj) -> bool:
    mimetype = get_mimetype(file_obj)
    return mimetype.startswith('video')


def is_valid_image_mimetype(file_obj) -> bool:
    mimetype = get_mimetype(file_obj)
    return mimetype.startswith('image')


def get_device_type_from_request(request):
    if request.auth:
        access_token = request.auth.key
        key_parts = access_token.split(':')
        return key_parts[0]

    if 'device_type' in request.data:
        return request.data['device_type']

    return request.META.get('HTTP_DEVICE_TYPE')


def get_device_id_from_request(request):
    if request.auth:
        access_token = request.auth.key
        key_parts = access_token.split(':')
        return key_parts[1]

    if 'device_id' in request.data:
        return request.data['device_id']

    return request.META.get('HTTP_DEVICE_ID')
