# Generated by Django 4.0.3 on 2022-05-13 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('task', models.CharField(max_length=1000)),
                ('date', models.DateField(auto_now=True)),
                ('date_end', models.DateField()),
            ],
        ),
    ]
