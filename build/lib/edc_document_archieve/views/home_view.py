from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from django.apps import apps as django_apps



class HomeView(viewsets.ViewSet):
    
    td_consent_model = 'tshilo_dikotla_subject.subjectconsent'
    flourish_consent_model = 'flourish_caregiver.subjectconsent'
    studies = [
        'Tshilo Dikotla',
        'Flourish'
    ]
    
    
    @property
    def flourish_consent_cls(self):
        return django_apps.get_model(self.flourish_consent_model)
    
    @property
    def td_consent_cls(self):
        return django_apps.get_model(self.td_consent_model)
    
    def list(self, request):
        return Response(self.studies)
    
    def retrieve(self, request, pk=None):
        if pk == self.studies[1]:
            registed_subject_model = self.flourish_consent_cls.objects.values_list(
                'subject_identifier',flat=True).distinct()
            
        return Response(registed_subject_model)