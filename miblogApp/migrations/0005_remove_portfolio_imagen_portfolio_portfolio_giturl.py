# Generated by Django 4.1.1 on 2022-10-16 03:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('miblogApp', '0004_cv_subtexto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='imagen_portfolio',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='giturl',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
