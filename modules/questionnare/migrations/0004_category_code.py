# Generated by Django 3.1.1 on 2020-09-29 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnare', '0003_auto_20200928_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='code',
            field=models.PositiveIntegerField(null=True),
        ),
    ]