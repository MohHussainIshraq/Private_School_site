# Generated by Django 4.1.2 on 2022-11-03 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_contact_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copy_right', models.CharField(max_length=100)),
                ('tag_message', models.CharField(max_length=100)),
            ],
        ),
    ]