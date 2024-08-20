# Generated by Django 5.1 on 2024-08-20 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReorderingParagraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('question', models.TextField(default='')),
                ('correctAns', models.TextField(default='')),
                ('ansScript', models.TextField(blank='true', default='')),
                ('score', models.IntegerField(default=0)),
            ],
        ),
    ]
