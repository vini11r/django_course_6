from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from mailing.forms import MailingSettingsForm, ClientForm, MailingSettingsManagerForm
from mailing.models import MailingSettings, Client, MailingMessage


class MailingListView(ListView):
    model = MailingSettings
    template_name = "mailing/mailingsettings_list.html"

    # def get_context_data(self):
    #     context = super().get_context_data()
    #     # context['blog_list'] = Blog.objects.order_by('?')[:3]
    #     return context


class MailingSettingCreateView(LoginRequiredMixin, CreateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy("mailing:mailing_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MailingSettingUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy("mailing:mailing_list")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return MailingSettingsForm
        elif user.has_perm("mailing.switch_status"):
            return MailingSettingsManagerForm
        raise PermissionDenied


class MailingSettingDeleteView(LoginRequiredMixin, DeleteView):
    model = MailingSettings
    success_url = reverse_lazy("mailing:mailing_list")


class MailingSettingDetailView(LoginRequiredMixin, DetailView):
    model = MailingSettings
    template_name = "mailing/mailingsettings_detail.html"


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'mailing/client_list.html'


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'mailing/client_detail.html'


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client_list')


class MessageListView(LoginRequiredMixin, ListView):
    model = MailingMessage
    template_name = 'mailing/mailingmessage_list.html'


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = MailingMessage
    template_name = 'mailing/mailingmessage_detail.html'


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = MailingMessage
    fields = '__all__'
    success_url = reverse_lazy('mailing:message_list')


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingMessage
    fields = '__all__'
    success_url = reverse_lazy('mailing:message_list')


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = MailingMessage
    success_url = reverse_lazy('mailing:message_list')
