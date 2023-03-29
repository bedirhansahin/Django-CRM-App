# Generated by Django 4.1.7 on 2023-03-29 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, db_column='Created Date')),
                ('first_name', models.CharField(db_column='First Name', max_length=50)),
                ('last_name', models.CharField(db_column='Last Name', max_length=50)),
                ('email', models.EmailField(db_column='Email', max_length=100)),
                ('phone', models.CharField(db_column='Phone Number', max_length=15)),
                ('country', models.CharField(db_column='Country', max_length=150)),
                ('city', models.CharField(db_column='City', max_length=50)),
                ('zipcode', models.CharField(db_column='Zipcode', max_length=20)),
            ],
            options={
                'verbose_name': 'Record',
                'verbose_name_plural': 'Records',
                'db_table': 'newschema"."record',
            },
        ),
    ]
