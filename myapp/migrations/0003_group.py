# Generated by Django 3.0.5 on 2020-06-06 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField(max_length=50)),
                ('group', models.CharField(max_length=50)),
                ('contact', models.IntegerField(max_length=100)),
            ],
        ),
    ]