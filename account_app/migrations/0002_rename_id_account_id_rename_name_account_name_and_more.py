# Generated by Django 5.1 on 2024-08-24 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='ID',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='Name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='account',
            name='email',
            field=models.EmailField(default='default@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='account',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='account',
            name='password',
            field=models.CharField(default='1234', max_length=200),
        ),
    ]
