# Generated by Django 4.1.1 on 2022-10-16 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miblogApp', '0007_portfolio_titulo_portfolio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='tipo_portfolio',
        ),
    ]
