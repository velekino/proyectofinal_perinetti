# Generated by Django 4.1.1 on 2022-10-16 04:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('miblogApp', '0006_alter_portfolio_giturl'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='titulo_portfolio',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
