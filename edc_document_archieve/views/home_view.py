from rest_framework.response import Response
from rest_framework.views import APIView
from ..classes import FlourishHelper, TshiloDikotlaHelper
from ..classes import DocumentArchiveHelper


class HomeView(FlourishHelper, TshiloDikotlaHelper, DocumentArchiveHelper, APIView):

    def get(self, request):
        study = request.GET.get('study')
        data = {}
        if study == 'flourish':
            data = {
                'pids': self.flourish_pids,
                'caregiver_forms': self.caregiver_forms,
                'child_forms': self.child_forms,
            }
        elif study == 'tshilo dikotla':
            data = {
                'pids': self.td_pids,
                'caregiver_forms': self.maternal_forms,
                'child_forms': self.infant_forms,
            }
        return Response(data)

    def post(self, request):

        results = request.data
        files = request.FILES.getlist('files')
        count, updated = self.populate_model_objects(results, files)
        return Response({
            'count': count,
            'updated': updated,
        })
