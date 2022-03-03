from rest_framework.views import APIView
from django.apps import apps as django_apps
from rest_framework.response import Response
from django.db.utils import IntegrityError
import json


class FlourishCaregiverFormsViewMixin:
    
    @property
    def caregiver_non_crfs(self):
        models = []
        app_models = django_apps.get_app_config(self.odk_app).get_models()
        for model in app_models:
            if model._meta.verbose_name.isupper():
                models.append(model._meta.verbose_name)
        return models
    
    @property
    def caregiver_crfs(self):
        models = [
             'Caregiver Clinician Notes',
        ]
        return models
    
    def caregiver_forms(self, request):
        data = {
            'crfs': self.caregiver_crfs,
            'non_crfs': self.caregiver_non_crfs
            }
        return Response(data)
    
    def create_non_crf_from(self):
        pass