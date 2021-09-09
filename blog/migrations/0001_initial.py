# Generated by Django 3.1.7 on 2021-04-09 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_text', models.TextField()),
                ('post_title', models.CharField(max_length=100)),
                ('post_date', models.DateField()),
                ('post_image', models.ImageField(upload_to='event_images/')),
            ],
        ),
    ]
