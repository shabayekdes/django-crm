from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from leads.forms import LeadForm
from leads.models import Lead


# Create your views here.
class LandPageTemplateView(TemplateView):
    template_name = "landing.html"


landing_page = LandPageTemplateView.as_view()


class LeadListView(ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


lead_list = LeadListView.as_view()


class LeadDetailView(DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


lead_detail = LeadDetailView.as_view()


class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadForm

    def get_success_url(self):
        return reverse("leads:lead-list")


lead_create = LeadCreateView.as_view()


class LeadUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadForm

    def get_success_url(self):
        return reverse("leads:lead-list")


lead_update = LeadUpdateView.as_view()


class LeadDeleteView(DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")


lead_delete = LeadDeleteView.as_view()

