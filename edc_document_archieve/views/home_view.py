from rest_framework.response import Response
from rest_framework.views import APIView
from edc_document_archieve.views.flourish_home_view_mixin import FlourishHomeViewMixin


class HomeView(FlourishHomeViewMixin,APIView):
    
    
   
    
    def get(self, request):
        studies = {
                'Tshilo Dikotla':{},
                'Flourish': {
                'pids':self.pids,
                'caregiver_forms': self.caregiver_forms,
                'child_forms': self.child_forms
                }
            }
        return Response(studies)
    
    