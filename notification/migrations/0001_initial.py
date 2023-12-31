# Generated by Django 4.2.3 on 2023-07-31 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.CharField(choices=[('Item Warning', 'Item Warning'), ('Expiration Warning', 'Expiration Warning')], max_length=100)),
                ('content', models.CharField(max_length=200)),
                ('sent_at', models.DateField(auto_now_add=True, null=True)),
                ('seen', models.BooleanField(default=False)),
            ],
        ),
    ]
