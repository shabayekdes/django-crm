from django.shortcuts import render, redirect

from leads.forms import LeadForm
from leads.models import Lead


# Create your views here.
def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/lead_list.html", context)


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, "leads/lead_detail.html", context)


def lead_create(request):
    form = LeadForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/leads/')

    context = {
        'form': form
    }
    return render(request, 'leads/lead_create.html', context=context)


def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadForm(request.POST or None, instance=lead)
    if form.is_valid():
        form.save()
        return redirect('/leads/')

    context = {
        'form': form
    }
    return render(request, 'leads/lead_update.html', context=context)
