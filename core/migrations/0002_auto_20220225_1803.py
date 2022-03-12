# Generated by Django 3.1.7 on 2022-02-25 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('OM', models.CharField(max_length=100, verbose_name='Nome')),
                ('email', models.CharField(max_length=100, verbose_name='email')),
                ('message', models.CharField(max_length=100, verbose_name='message')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
    ]