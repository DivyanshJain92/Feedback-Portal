# Generated by Django 4.0.5 on 2022-10-10 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('des', models.TextField()),
                ('other', models.TextField()),
                ('sugg', models.TextField()),
            ],
        ),
    ]
