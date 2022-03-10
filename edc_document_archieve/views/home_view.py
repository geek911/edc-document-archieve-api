import datetime
import pytz

from rest_framework.response import Response
from rest_framework.views import APIView
from .flourish_home_view_mixin import FlourishHomeViewMixin
from django.apps import apps as django_apps
from django.utils.timezone import make_aware


class HomeView(FlourishHomeViewMixin, APIView):

    def get(self, request):
        studies = {
            'flourish': {
                'pids': self.pids,
                'caregiver_forms': self.caregiver_forms,
                'child_forms': self.child_forms
            },
            'tshilo-dikotla': {},
        }

        results = [
            {
                'subject_identifier': 'B142-040990462-9',
                'visit_code': '1000M',
                'timepoint': 0
            }
        ]
        print(self.populate_model_objects(
            'flourish_caregiver',
            results,
            self.clinician_notes_model_cls('flourish_caregiver'),
        ))
        return Response(studies)

    def post(self, request):
        tz = pytz.timezone('Africa/Gaborone')
        # All data capture before the date below
        created = datetime.datetime(2022, 3, 11, 0, 12)
        created = make_aware(created, tz, True)
        results = [
            {
                'subject_identifier': 'B142-040990462-9',
                'visit_code': '1000M',
                'timepoint': 0,
                'image_name': [request.data['image_name']],
                'image_url': [request.data['image_url']],
                'date_captured': created,
                'username': 'moffatmore',
                'model_cls': 'flourish_caregiver',
                'model_name': ''
            }
        ]
        img_cls = django_apps.get_model(self.clinician_notes_image_model('flourish_caregiver'))
        image_cls_field = 'clinician_notes'
        self.populate_model_objects(
            'flourish_caregiver',
            results,
            self.clinician_notes_model_cls('flourish_caregiver'),
            img_cls,
            image_cls_field)

        return Response("Hello")