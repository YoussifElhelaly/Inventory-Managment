# Generated by Django 4.2.3 on 2023-08-05 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banlist', '0002_dangerlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dangerlist',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
