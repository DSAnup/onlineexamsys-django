# Generated by Django 3.1 on 2020-08-16 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='currect_ans',
            field=models.CharField(choices=[('0', 'False'), ('1', 'True')], max_length=1, verbose_name='Choice Currect Answer'),
        ),
    ]
