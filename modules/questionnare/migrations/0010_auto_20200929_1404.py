# Generated by Django 3.1.1 on 2020-09-29 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnare', '0009_subquestion_qn_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='subquestion',
            name='code',
            field=models.CharField(max_length=10),
        ),
    ]
