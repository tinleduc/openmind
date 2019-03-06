import binascii
import os

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

NOTIFY_TYPE_ADD_NEW_FOLDER = 'add-new-folder'
NOTIFY_TYPE_ADD_NEW_FEATURE = 'add-new-feature'
NOTIFY_TYPE_PROMOTIONAL_CAMPAIGN = 'promotional-campaign'
NOTIFY_TYPE_PRE_ORDER = 'pre-order'
NOTIFY_TYPE_EVENT = 'event'
NOTIFY_TYPE_UPDATE_CONTENT = 'update-content'
NOTIFY_TYPE_UPDATE_VERSION = 'update-version'
NOTIFY_TYPE_LOGIN_REMINDER = 'login-reminder'
NOTIFY_TYPE_ACHIEVING_GOAL_INFO = 'achieving-goal-information'
NOTIFY_TYPE_RATING_APP = 'rating-app'

NOTIFY_TYPE_CHOICES = (
    (NOTIFY_TYPE_ADD_NEW_FOLDER, 'Add New Folder'),
    (NOTIFY_TYPE_ADD_NEW_FEATURE, 'Add New Feature'),
    (NOTIFY_TYPE_PROMOTIONAL_CAMPAIGN, 'Promotional Campaign'),
    (NOTIFY_TYPE_PRE_ORDER, 'Pre Order'),
    (NOTIFY_TYPE_EVENT, 'Event'),
    (NOTIFY_TYPE_UPDATE_CONTENT, 'Update Content'),
    (NOTIFY_TYPE_LOGIN_REMINDER, 'Login Reminder'),
)


TOKEN_LENGTH = 64
RESET_TOKEN_LENGTH = 10
CONFIRM_EMAIL_TOKEN_LENGTH = 128


def generate_access_token(device_id, device_type):
    num_bytes = TOKEN_LENGTH // 2
    token = binascii.hexlify(os.urandom(num_bytes)).decode()
    access_token = '{device_type}:{device_id}:{token}'.format(
        device_type=device_type,
        device_id=device_id,
        token=token,
    )
    return access_token


class User(AbstractUser):
    username = models.CharField()
    email = models.EmailField()
    user_type = models.IntegerField()
    status = models.IntegerField()
    facebook_id = models.CharField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'user'

    def __str__(self):
        return 'User: {}'.format(self.username)


class Token(models.Model):
    """
    The default authorization token model.
    """
    key = models.CharField("Key", max_length=128, primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='tokens',
        on_delete=models.CASCADE, verbose_name="User"
    )
    created = models.DateTimeField()

    class Meta:
        db_table = 'token'

    def __str__(self):
        return 'Token(user {}):{}'.format(self.user_id, self.key)


class ResetToken(models.Model):
    reset_token = models.CharField(
        "Reset token", primary_key=True, max_length=RESET_TOKEN_LENGTH
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='reset_token',
        on_delete=models.CASCADE, verbose_name='user'
    )
    created_at = models.DateTimeField("Created", auto_now_add=True)

    class Meta:
        db_table = 'reset_token'

    def save(self, *args, **kwargs):
        if not self.reset_token:
            self.reset_token = self.generate_reset_token()
        return super(ResetToken, self).save(*args, *kwargs)

    def generate_reset_token(self):
        num_bytes = RESET_TOKEN_LENGTH // 2
        return binascii.hexlify(os.urandom(num_bytes)).decode()

    def __str__(self):
        return 'ResetToken (user {}):{}'.format(self.user_id, self.reset_token)


class ConfirmEmailToken(models.Model):
    token = models.CharField(
        _("token"), primary_key=True, max_length=CONFIRM_EMAIL_TOKEN_LENGTH
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='confirm_email_token',
        on_delete=models.CASCADE, verbose_name=_('user')
    )
    created_at = models.DateTimeField(_('Created'), auto_now_add=True)

    class Meta:
        db_table = 'confirm_email_token'

        def save(self, *args, **kwargs):
            if not self.token:
                self.token = self.generate_confirm_email_token()
            return super(ConfirmEmailToken, self).save(*args, **kwargs)

        def generate_confirm_email_token(self):
            num_bytes = CONFIRM_EMAIL_TOKEN_LENGTH // 2
            return binascii.hexlify(os.urandom(num_bytes)).decode()

        def __str__(self):
            return 'ConfirmEmailToken (user {}): {}'.format(self.user, self.token)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    num_stars = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'rating'


class LoginHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now=True)
    num_date = models.IntegerField(default=1)

    class Meta:
        db_table = 'login_history'


class Notification(models.Model):
    title = models.TextField(blank=True, default='')
    body = models.TextField(blank=True, default='')
    notify_type = models.CharField(max_length=60, choices=NOTIFY_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'notification'
        ordering = ['-created_at']


class UserNotification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification = models.ForeignKey(
        Notification, on_delete=models.CASCADE(),
        related_name='user_notifications'
    )
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_notification'
        ordering = ['-created_at']








