# Generated by Django 5.0.7 on 2024-08-21 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mytrial', '0009_passticket_document_pdf'),
    ]

    operations = [
        migrations.RenameField(
            model_name='casefile',
            old_name='landlord_name',
            new_name='user_type',
        ),
        migrations.RemoveField(
            model_name='casefile',
            name='tenant',
        ),
    ]