# Generated by Django 2.2 on 2019-11-23 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20191107_0446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.IntegerField(choices=[(1, 'Professor'), (2, 'Student')], default=2),
        ),
    ]