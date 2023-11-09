# Generated by Django 4.2.4 on 2023-08-10 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_consulta_data_consulta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consulta',
            name='data_consulta',
        ),
        migrations.AddField(
            model_name='consulta',
            name='dia',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='consulta',
            name='hora',
            field=models.TimeField(null=True),
        ),
    ]
