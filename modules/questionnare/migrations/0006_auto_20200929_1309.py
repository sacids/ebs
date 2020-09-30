# Generated by Django 3.1.1 on 2020-09-29 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnare', '0005_auto_20200929_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='has_sub',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], default='NO', max_length=10, null=True, verbose_name='Has sub question?'),
        ),
        migrations.AddField(
            model_name='question',
            name='parent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='questionnare.question'),
        ),
    ]