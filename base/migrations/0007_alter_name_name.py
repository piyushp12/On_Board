# Generated by Django 4.0.6 on 2022-07-28 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_name_alter_studentfive_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='name',
            field=models.CharField(blank=True, default='1', max_length=20, null=True),
        ),
    ]
