import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


TYPE_USER = (
        ("1", "Admin"),
        ("2", "Comprador"),
        ("3", "Vendedor"),
    )

class User(AbstractUser):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    user_type = models.CharField("Tipo de Usuário",max_length=8,choices=TYPE_USER, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    phone = models.CharField(max_length=15, blank=True, null=True, default=None)
    name = models.CharField(max_length=100, blank=False, null=False)
    is_active = models.BooleanField("Active", default=True, blank=False, null=False)
    is_staff = models.BooleanField("Staff", default=False, blank=False, null=False)
    is_superuser = models.BooleanField(
        "Superuser", default=False, blank=False, null=False
    )
    updated_at = models.DateTimeField(auto_now=True)
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Users"

    def get_username(self) -> str:
        return self.email

    def __str__(self) -> str:
        return f"{self.email}"