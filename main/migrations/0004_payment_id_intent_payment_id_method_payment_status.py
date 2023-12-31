# Generated by Django 4.2.4 on 2023-08-27 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='id_intent',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='id_намерение платежа'),
        ),
        migrations.AddField(
            model_name='payment',
            name='id_method',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='id_метод платежа'),
        ),
        migrations.AddField(
            model_name='payment',
            name='status',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='статус платежа'),
        ),
    ]
