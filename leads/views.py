from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic

from leads.forms import LeadForm
from leads.models import Lead


# Create your views here.
class LandPageTemplateView(generic.TemplateView):
    template_name = "landing.html"


landing_page = LandPageTemplateView.as_view()


class LeadListView(generic.ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


lead_list = LeadListView.as_view()


class LeadDetailView(generic.DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


lead_detail = LeadDetailView.as_view()


class LeadCreateView(generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadForm

    def get_success_url(self):
        return reverse("leads:lead-list")

    def form_valid(self, form):
        send_mail(
            subject="A lead has been created",
            message="Go to the site to see the new lead",
            from_email="test@test.com",
            recipient_list=["test2@test.com"]
        )
        return super(LeadCreateView, self).form_valid(form)


lead_create = LeadCreateView.as_view()


class LeadUpdateView(generic.UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadForm

    def get_success_url(self):
        return reverse("leads:lead-list")


lead_update = LeadUpdateView.as_view()


class LeadDeleteView(generic.DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")


lead_delete = LeadDeleteView.as_view()

