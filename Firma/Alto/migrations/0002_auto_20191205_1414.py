# Generated by Django 2.2.7 on 2019-12-05 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personel',
            name='Grupa',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dane_firmy',
            name='Kod_pocztowy',
            field=models.CharField(max_length=6),
        ),
    ]
