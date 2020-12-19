import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Webhook(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Script(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    webhook = models.ForeignKey('Webhook', on_delete=models.CASCADE)
    code = models.TextField()

    def __str__(self):
        # truncate at 25 chars and add "..." to indicate
        return self.code[:25] + (self.code[25:] and "...")


class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    time_of_receipt = models.DateTimeField(auto_now_add=True)
    webhook = models.ForeignKey('Webhook', on_delete=models.CASCADE)
    payload = models.TextField()

    def __str__(self):
        # truncate at 25 chars and add "..." to indicate
        return self.payload[:25] + (self.payload[25:] and "...")


class Secret(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
