# Generated by Django 5.0.2 on 2024-10-17 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsecundaria', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='frase',
            options={'verbose_name': 'Frase', 'verbose_name_plural': 'frases'},
        ),
        migrations.AlterField(
            model_name='alumnot',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='Nombre (s)'),
        ),
    ]
