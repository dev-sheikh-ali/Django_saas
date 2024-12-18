# Generated by Django 5.1.4 on 2024-12-05 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavbarBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(default='We have launched Flowbite Blocks featuring over 450+ website sections!', max_length=255)),
                ('link_text', models.CharField(default='Check it out', max_length=100)),
                ('link_url', models.URLField(default='#', max_length=500)),
                ('svg_icon', models.TextField(default='', help_text='Paste SVG content here for the icon')),
                ('is_active', models.BooleanField(default=True, help_text='Toggle to enable or disable this banner')),
            ],
        ),
        migrations.DeleteModel(
            name='Banner',
        ),
        migrations.AlterField(
            model_name='newslettersubscription',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
