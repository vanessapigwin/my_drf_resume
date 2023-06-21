from django.db import models


class PersonalInfo(models.Model):
    person_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=100)
    website = models.CharField(unique=True, max_length=100, blank=True, null=True)
    repository = models.CharField(unique=True, max_length=100, blank=True, null=True)
    contact_number = models.CharField(unique=True, max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal_info'


class Skills(models.Model):
    skill_id = models.AutoField(primary_key=True)
    skill_name = models.CharField(max_length=100)
    fk_person = models.ForeignKey(PersonalInfo, models.DO_NOTHING, related_name='skills', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skills'


class TechStack(models.Model):
    tech_id = models.AutoField(primary_key=True)
    tool_name = models.CharField(max_length=100)
    years_of_exp = models.IntegerField(blank=True, null=True)
    fk_skill = models.ForeignKey(Skills, models.DO_NOTHING, related_name='tech_stack', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tech_stack'


class EmploymentHistory(models.Model):
    history_id = models.AutoField(primary_key=True)
    company = models.CharField(max_length=100)
    emp_start = models.DateField()
    emp_end = models.DateField(blank=True, null=True)
    job_title = models.CharField(max_length=200, blank=True, null=True)
    fk_person = models.ForeignKey(
        'PersonalInfo', models.DO_NOTHING, related_name='employment_history', blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = 'employment_history'


class Accomplishment(models.Model):
    accomp_id = models.AutoField(primary_key=True)
    description = models.TextField()
    fk_history = models.ForeignKey(
        'EmploymentHistory', models.CASCADE, related_name='accomplishment', blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = 'accomplishment'


class Education(models.Model):
    educ_id = models.AutoField(primary_key=True)
    school = models.CharField(max_length=100)
    year_started = models.IntegerField()
    year_graduated = models.IntegerField()
    course = models.CharField(max_length=100, blank=True, null=True)
    fk_person = models.ForeignKey('PersonalInfo', models.DO_NOTHING, related_name='education', blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'education'