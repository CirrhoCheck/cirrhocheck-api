# Generated by Django 4.2.9 on 2024-02-04 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0004_remove_dummyitem_id_remove_user_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dummyitem',
            old_name='uuid',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='uuid',
            new_name='id',
        ),
    ]
