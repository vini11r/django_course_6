from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingListView, MailingSettingCreateView, MailingSettingDetailView, \
    MailingSettingDeleteView, MailingSettingUpdateView, ClientListView, ClientCreateView, ClientDetailView, \
    ClientUpdateView, ClientDeleteView

app_name = MailingConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='mailing_list'),
    path('create/', MailingSettingCreateView.as_view(), name='mailing_create'),
    path('detail/<int:pk>/', MailingSettingDetailView.as_view(), name='mailing_detail'),
    path('update/<int:pk>/', MailingSettingUpdateView.as_view(), name='mailing_update'),
    path('delete/<int:pk>/', MailingSettingDeleteView.as_view(), name='mailing_delete'),

    path('client/', ClientListView.as_view(), name='client_list'),
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/detail/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),

]
