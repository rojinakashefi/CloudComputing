# Generated by Django 4.1.3 on 2022-11-07 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad_manager_api', '0004_todo_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=100)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.FileField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]