# Generated by Django 3.2.8 on 2021-10-30 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my', '0003_alter_admin_advisor_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
