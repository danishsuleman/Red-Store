# Generated by Django 4.0.6 on 2022-07-20 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_members', '0005_alter_team_member_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team_member',
            name='image',
            field=models.FileField(upload_to='about/team_members'),
        ),
    ]
