from django.db import models
from django.core import validators


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True, validators=[
                              validators.EmailValidator(message="Invalid Email")])
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey(
        'auth.User', related_name='todos', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
