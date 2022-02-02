from nazgul.views import BaseView, sendus
from django.urls import path


urlpatterns = [
    path('', BaseView.as_view(), name='baseview'),
    path('send-us', sendus, name='send-us')
]
