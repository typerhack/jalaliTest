# Generated by Django 3.0.6 on 2020-05-16 14:13

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DateTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_persian_date', django_jalali.db.models.jDateTimeField()),
            ],
        ),
    ]