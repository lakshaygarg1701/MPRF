# Generated by Django 2.1.7 on 2019-04-02 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20181116_1827'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('report', models.TextField()),
            ],
            options={
                'db_table': 'eventrep',
                'managed': False,
            },
        ),
    ]
