# Generated by Django 2.2 on 2020-11-04 21:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20201104_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiles',
            name='id',
        ),
        migrations.AlterField(
            model_name='profiles',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]