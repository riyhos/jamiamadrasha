# Generated by Django 4.2.5 on 2023-09-14 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_gallary_lagacy_subject_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacher_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
