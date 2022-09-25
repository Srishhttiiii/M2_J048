# Generated by Django 4.0.6 on 2022-09-25 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_specialskills_assignment_specialskills_cycling_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(blank=True, choices=[('Mon', 'Monday'), ('Mon', 'Monday'), ('Mon', 'Monday'), ('Mon', 'Monday'), ('Mon', 'Monday'), ('Mon', 'Monday'), ('Mon', 'Monday')], default='None', max_length=30, null=True)),
            ],
            options={
                'verbose_name_plural': 'Week',
            },
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]