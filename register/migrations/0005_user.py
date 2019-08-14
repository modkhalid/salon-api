# Generated by Django 2.2.2 on 2019-07-14 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20190604_0914'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('country', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, upload_to='profile_pics')),
                ('password', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
