# Generated by Django 2.1 on 2018-08-20 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0003_article_last_update_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='auther',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
