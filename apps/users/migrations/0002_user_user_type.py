# Generated by Django 4.0.4 on 2022-06-14 21:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('1', 'Admin'), ('2', 'Comprador'), ('3', 'Vendedor')], default=django.utils.timezone.now, max_length=8, verbose_name='Tipo de Usuário'),
            preserve_default=False,
        ),
    ]
