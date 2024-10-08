# Generated by Django 5.1 on 2024-09-01 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_domainform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('rating', models.IntegerField(choices=[(5, 'Excellent'), (4, 'Very Good'), (3, 'Good'), (2, 'Fair'), (1, 'Poor'), (0, 'Very Poor')], default=3)),
                ('feedback', models.TextField()),
            ],
        ),
    ]
