# Generated by Django 3.1 on 2021-06-27 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holidays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateTimeField(default='')),
                ('credited_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'holidays',
                'managed': True,
            },
        ),
    ]
