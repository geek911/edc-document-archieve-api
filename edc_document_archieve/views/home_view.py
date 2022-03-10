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
        return Response(studies)

    def post(self, request):
        tz = pytz.timezone('Africa/Gaborone')
        # All data capture before the date below
        created = datetime.datetime(2022, 3, 11, 11, 5)
        created = make_aware(created, tz, True)

        results = [
            {
                'subject_identifier': 'B142-040990462-9',
                'image_name': [request.data['image_name']],
                'image_url': [request.data['image_url']],
                'date_captured': created,
                'username': 'moffatmore',
                'app_label': 'edc_odk',
                'model_name': 'omang_copies',
            }
        ]
        self.populate_model_objects(results)
        return Response("Hello")
