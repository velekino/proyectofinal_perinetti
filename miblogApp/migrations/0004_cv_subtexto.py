# Generated by Django 4.1.1 on 2022-10-03 19:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('miblogApp', '0003_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='subtexto',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
