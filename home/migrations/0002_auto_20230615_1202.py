# Generated by Django 3.2.16 on 2023-06-15 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentinfo',
            name='user',
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='degreePercentage',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='yop',
            field=models.CharField(max_length=200, null=True),
        ),
    ]