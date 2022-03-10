from rest_framework.response import Response
from rest_framework.views import APIView
from .flourish_home_view_mixin import FlourishHomeViewMixin


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
        results = request.data
        files = request.FILES.getlist('files')
        print(files)
        self.populate_model_objects(results, files)
        return Response("Hello")
