# Generated by Django 2.2.1 on 2019-05-07 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default='a.abdelfatah.100@gmail.com', max_length=30),
        ),
    ]