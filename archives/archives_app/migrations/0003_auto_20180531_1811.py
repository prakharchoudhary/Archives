# Generated by Django 2.0.5 on 2018-05-31 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('archives_app', '0002_auto_20180531_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='subdirs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='archives_app.Category'),
        ),
    ]
