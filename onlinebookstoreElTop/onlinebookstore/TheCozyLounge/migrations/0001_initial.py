# Generated by Django 5.1.2 on 2024-11-11 15:12
#auto generated an incremented 
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_name', models.CharField(max_length=64)),
                ('b_Language', models.CharField(max_length=64)),
                ('b_title', models.CharField(max_length=64)),
                ('a_about', models.TextField(max_length=500)),
                ('b_review', models.TextField(max_length=400)),
                ('b_description', models.TextField(max_length=800)),
                ('b_genres', models.TextField()),
                ('b_version', models.IntegerField()),
                ('b_nu_of_pages', models.IntegerField()),
                ('b_price', models.IntegerField()),
                ('b_rate', models.IntegerField()),
                ('b_y_of_pub', models.DateField()),
                ('b_sound', models.BooleanField(default=False)),
                ('b_pic', models.ImageField(upload_to='')),
            ],
        ),
        
    ]
