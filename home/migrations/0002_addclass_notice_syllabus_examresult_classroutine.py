# Generated by Django 4.2.5 on 2023-09-14 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_of_notice', models.CharField(max_length=350)),
                ('add_file', models.FileField(max_length=300, upload_to='Notice/')),
                ('uploaded_at', models.DateField(auto_now=True)),
                ('total_view', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_of_notice', models.CharField(max_length=350)),
                ('add_file', models.FileField(max_length=300, upload_to='Syllabus/')),
                ('select_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.addclass')),
            ],
        ),
        migrations.CreateModel(
            name='ExamResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_of_notice', models.CharField(max_length=350)),
                ('add_file', models.FileField(max_length=300, upload_to='ExamResult/')),
                ('select_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.addclass')),
            ],
        ),
        migrations.CreateModel(
            name='ClassRoutine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_of_notice', models.CharField(max_length=350)),
                ('add_file', models.FileField(max_length=300, upload_to='ClassRoutine/')),
                ('select_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.addclass')),
            ],
        ),
    ]
