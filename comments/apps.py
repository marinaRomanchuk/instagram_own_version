from django.apps import AppConfig


class CommentsConfig(AppConfig):
    default_auto_field: str = "django.db.models.BigAutoField"
    name: str = "comments"
