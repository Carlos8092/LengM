# Generated by Django 5.1.2 on 2024-10-22 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Choice',
            new_name='Choices',
        ),
        migrations.RenameField(
            model_name='choices',
            old_name='choice_text',
            new_name='Choice_text',
        ),
    ]
