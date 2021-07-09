from django.db import models
from django.utils.timezone import now

# Create your models here.


class CreatedUpdatedModel(models.Model):
    """
    A model to reuse the `created_at` and `updated_at` fields
    """
    created_at = models.DateTimeField(default=now, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self._state.adding:
            self.updated_at = now()
        super().save(*args, **kwargs)


class BotUser(CreatedUpdatedModel):
    """
    The bot user
    """

    # Basic data
    chat_id = models.CharField(max_length=255)
    username = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)

    # Permissions
    is_admin = models.BooleanField(default=False)

    # State
    has_blocked_bot = models.BooleanField(default=False)
    last_action_datetime = models.DateTimeField(null=True, blank=True)

    language = models.CharField(max_length=2, choices=(
        # define your bot languages here
        ('ES', 'es'),
        ('EN', 'en'),
    ), default=None, null=True, blank=True)

    def __str__(self):
        name = self.first_name
        if self.last_name is not None:
            name += f' {self.last_name}'
        if self.username is not None:
            name += f' (@{self.username})'
        return name

    def report_last_action(self):
        self.last_action_datetime = now()
