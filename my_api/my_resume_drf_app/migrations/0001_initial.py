# Generated by Django 4.0 on 2023-06-20 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accomplishment',
            fields=[
                ('accomp_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'accomplishment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('educ_id', models.AutoField(primary_key=True, serialize=False)),
                ('school', models.CharField(max_length=100)),
                ('year_started', models.IntegerField()),
                ('year_graduated', models.IntegerField()),
                ('course', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'education',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmploymentHistory',
            fields=[
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('company', models.CharField(max_length=100)),
                ('emp_start', models.DateField()),
                ('emp_end', models.DateField(blank=True, null=True)),
                ('job_title', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'employment_history',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('person_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('website', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('repository', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('contact_number', models.CharField(blank=True, max_length=100, null=True, unique=True)),
            ],
            options={
                'db_table': 'personal_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('skill_id', models.AutoField(primary_key=True, serialize=False)),
                ('skill_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'skills',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TechStack',
            fields=[
                ('tech_id', models.AutoField(primary_key=True, serialize=False)),
                ('tool_name', models.CharField(max_length=100)),
                ('years_of_exp', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tech_stack',
                'managed': False,
            },
        ),
    ]
