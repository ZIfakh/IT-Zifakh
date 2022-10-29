# Generated by Django 4.1.2 on 2022-10-26 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=123, verbose_name='Название')),
                ('year', models.IntegerField(null=True)),
                ('color', models.CharField(max_length=10)),
            ],
        ),
    ]
