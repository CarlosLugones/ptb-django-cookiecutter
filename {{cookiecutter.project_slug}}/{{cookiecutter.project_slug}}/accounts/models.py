from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    def __str__(self):
        return self.get_full_name() or self.username
