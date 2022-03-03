from django.urls import include, path
from .views import CustomAuthToken, HomeView, FlourishHomeView
from django.contrib import admin
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('projects/', HomeView.as_view()),
    path('flourish/pids/', FlourishHomeView.as_view({'get': 'pids'})),
    path('flourish/caregiver_forms/', FlourishHomeView.as_view({'get': 'caregiver_forms'})),
]


