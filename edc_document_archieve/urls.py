from django.urls import include, path
from .views import CustomAuthToken, HomeView
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('projects/', HomeView.as_view()),
]


