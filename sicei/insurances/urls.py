from django.urls import path
from .views import StudentView

urlpatterns = [
    path('api/student/', StudentView.as_view(), name='student'),
]