from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import HistoryUrl
from .forms import HistoryUrlModelForm

# create history list view that will show all Url in Database


def historyList(request):
    qs = HistoryUrl.objects.all()
    context = {'title': 'History List', 'object_list': qs}
    template_name = 'historyList.html'
    return render(request, template_name, context)

# create a view that will contain a form to save new Url to Database


def StoreToHistory(request):
    form = HistoryUrlModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = HistoryUrlModelForm()
    template_name = 'storeToHistory.html'
    context = {"title": "Save URL to History", "form": form}
    return render(request, template_name, context)
