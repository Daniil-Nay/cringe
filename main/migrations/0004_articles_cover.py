# Generated by Django 3.2.23 on 2023-12-18 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_articles_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='cover',
            field=models.ImageField(default='image', upload_to='img/'),
            preserve_default=False,
        ),
    ]
