from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from mailing.forms import MailingSettingsForm
from mailing.models import MailingSettings, MailingLog, MailingMessage, Client


class MailingListView(ListView):
    model = MailingSettings
    template_name = "mailing/mailing_list.html"


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
    template_name = "mailing/mailing_detail.html"



