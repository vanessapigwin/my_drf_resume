from my_resume_drf_app.models import *
from rest_framework import viewsets
from rest_framework import permissions
from my_resume_drf_app.serializers import *

class PersonalInfoViewSet(viewsets.ModelViewSet):
    '''
    Personal and contact information
    '''

    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer


class SkillsViewSet(viewsets.ModelViewSet):
    '''
    Skills acquired from experience
    '''

    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer


class TechStackViewSet(viewsets.ModelViewSet):
    '''
    Tools used and years of experience using a particular tool 
    '''
    queryset = TechStack.objects.all()
    serializer_class = TechStackSerializer


class EmploymentHistoryViewSet(viewsets.ModelViewSet):
    '''
    Professional experience from the last 10 years
    '''
    
    queryset = EmploymentHistory.objects.all()
    serializer_class = EmploymentHistorySerializer


class EducationViewSet(viewsets.ModelViewSet):
    '''
    Educational background (not that it matters)
    '''

    queryset = Education.objects.all()
    serializer_class = EducationSerializer