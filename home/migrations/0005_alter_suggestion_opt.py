# Generated by Django 4.0.5 on 2022-10-10 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_suggestion_opt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestion',
            name='opt',
            field=models.CharField(default='General Management', editable=False, max_length=25),
        ),
    ]
