from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from mailing.forms import MailingSettingsForm, ClientForm
from mailing.models import MailingSettings, Client


class MailingListView(ListView):
    model = MailingSettings
    template_name = "mailing/mailingsettings_list.html"


class MailingSettingCreateView(CreateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy("mailing:mailing_list")


class MailingSettingUpdateView(UpdateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy("mailing:mailing_list")


class MailingSettingDeleteView(DeleteView):
    model = MailingSettings
    success_url = reverse_lazy("mailing:mailing_list")


class MailingSettingDetailView(DetailView):
    model = MailingSettings
    template_name = "mailing/mailingsettings_detail.html"


class ClientListView(ListView):
    model = Client
    template_name = 'mailing/client_list.html'


class ClientDetailView(DetailView):
    model = Client
    template_name = 'mailing/client_detail.html'


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client_list')
