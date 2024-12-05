# Generated by Django 5.1.4 on 2024-12-05 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='herosection',
            name='image',
        ),
        migrations.AddField(
            model_name='herosection',
            name='image_url',
            field=models.URLField(blank=True, default='https://flowbite.s3.amazonaws.com/blocks/marketing-ui/hero/phone-mockup.png', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='herosection',
            name='button_text',
            field=models.CharField(default='Get started', max_length=100),
        ),
        migrations.AlterField(
            model_name='herosection',
            name='button_url',
            field=models.URLField(default='#'),
        ),
        migrations.AlterField(
            model_name='herosection',
            name='secondary_button_text',
            field=models.CharField(blank=True, default='Speak to Sales', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='herosection',
            name='secondary_button_url',
            field=models.URLField(blank=True, default='#', null=True),
        ),
        migrations.AlterField(
            model_name='herosection',
            name='subtitle',
            field=models.TextField(default='From checkout to global sales tax compliance, companies around the world use Flowbite to simplify their payment stack.'),
        ),
        migrations.AlterField(
            model_name='herosection',
            name='title',
            field=models.CharField(default='Payments tool for software companies', max_length=255),
        ),
    ]
