# Исправлены пробелы и отступы
from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                ("id", models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name="ID")),
                ("title", models.CharField(max_length=255)),
                ("is_completed", models.BooleanField(default=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("user", models.ForeignKey(
                    on_delete=models.CASCADE,
                    to=settings.AUTH_USER_MODEL
                )),
            ],
        ),
    ]
