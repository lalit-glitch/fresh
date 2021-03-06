# Generated by Django 3.2.8 on 2021-10-30 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('advisor_name', models.CharField(max_length=20)),
                ('advisor_profile_pic', models.ImageField(upload_to='G/')),
                ('advisor_id', models.IntegerField(default=1, unique=True)),
                ('booking_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geeks', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
