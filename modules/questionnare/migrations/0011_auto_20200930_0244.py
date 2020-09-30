# Generated by Django 3.1.1 on 2020-09-30 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnare', '0010_auto_20200929_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='qn_type',
            field=models.CharField(choices=[('NONE', 'None'), ('SELECT', 'Select One'), ('CHECKBOX', 'Select Multiple'), ('NUMBER', 'Number'), ('TEXT', 'Norma Text'), ('TEXTAREA', 'Text Area')], default='NONE', max_length=50, verbose_name='Question type'),
        ),
        migrations.AlterField(
            model_name='subquestion',
            name='qn_type',
            field=models.CharField(choices=[('NONE', 'None'), ('SELECT', 'Select One'), ('CHECKBOX', 'Select Multiple'), ('NUMBER', 'Number'), ('TEXT', 'Norma Text'), ('TEXTAREA', 'Text Area')], default='NONE', max_length=50, verbose_name='Question type'),
        ),
    ]