# Generated by Django 5.1.4 on 2024-12-05 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeroSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.TextField()),
                ('button_text', models.CharField(max_length=100)),
                ('button_url', models.URLField()),
                ('secondary_button_text', models.CharField(blank=True, max_length=100, null=True)),
                ('secondary_button_url', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='hero_images/')),
            ],
        ),
    ]
