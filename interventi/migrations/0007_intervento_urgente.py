# Generated by Django 2.2.1 on 2019-05-31 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interventi', '0006_auto_20190530_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='intervento',
            name='urgente',
            field=models.BooleanField(default=False),
        ),
    ]
