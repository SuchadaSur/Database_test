# Generated by Django 2.1.15 on 2022-10-10 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Skcone', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testrequest',
            name='system',
        ),
        migrations.DeleteModel(
            name='System',
        ),
        migrations.DeleteModel(
            name='testRequest',
        ),
    ]
