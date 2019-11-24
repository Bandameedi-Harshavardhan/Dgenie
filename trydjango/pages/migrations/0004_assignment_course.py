# Generated by Django 2.2.7 on 2019-11-24 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20191124_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.TextField()),
                ('username', models.ManyToManyField(related_name='user_course', to='pages.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('references', models.CharField(max_length=100)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Course')),
            ],
        ),
    ]