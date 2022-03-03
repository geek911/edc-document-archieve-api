from django.apps import apps as django_apps
from rest_framework.response import Response
from rest_framework import viewsets

import json
from .flourish_caregiver_forms_view_mixin import FlourishCaregiverFormsViewMixin

class FlourishHomeView(FlourishCaregiverFormsViewMixin,viewsets.ViewSet):
    
    odk_app = 'edc_odk'
    app_name = 'flourish_caregiver'
    caregiver_consent_model = 'flourish_caregiver.subjectconsent'
    child_consent_model = 'flourish_child.childdummysubjectconsent'
    
    @property
    def child_consent_cls(self):
        return django_apps.get_model(self.child_consent_model)
    
    @property
    def caregiver_consent_cls(self):
        return django_apps.get_model(self.caregiver_consent_model)
    
    def pids(self, request):
        caregiver_pids = self.caregiver_consent_cls.objects.values_list(
                'subject_identifier', flat=True).distinct()
                
        child_pids = self.child_consent_cls.objects.values_list(
                'subject_identifier', flat=True).distinct()
        data = {
            'caregiver': caregiver_pids,
            'child': child_pids
            }
        return Response(data)
    