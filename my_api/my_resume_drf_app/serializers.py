from my_resume_drf_app.models import *
from rest_framework import serializers


class PersonalInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = [
            'first_name', 'last_name', 'email', 'website', 
            'repository', 'contact_number'
        ]


class TechStackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TechStack
        fields = ['tool_name', 'years_of_exp']


class SkillsSerializer(serializers.HyperlinkedModelSerializer):
    tech_stack = TechStackSerializer(many=True, read_only=True)

    class Meta:
        model = Skills
        fields = ['skill_name', 'tech_stack']


class EmploymentHistorySerializer(serializers.HyperlinkedModelSerializer):
    accomplishment = serializers.SlugRelatedField(many=True, queryset=Accomplishment.objects.all(), slug_field='description')

    class Meta:
        model = EmploymentHistory
        fields = ['company', 'job_title', 'emp_start', 'emp_end', 'accomplishment']


class AccomplishmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Accomplishment
        fields = ['description']


class EducationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Education
        fields = ['school', 'course', 'year_started', 'year_graduated']