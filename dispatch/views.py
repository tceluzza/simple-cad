from django.shortcuts import render
from django.views import generic

from .models import Call

# Create your views here.

class CallsListView(generic.ListView):
    paginate_by = 20
    context_object_name = "calls_list"
    template_name = "dispatch/view_calls.html"

    queryset = Call.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context["calls_list"] = Call.objects.filter
        context["home_nav"] = "active"
        return context

class CallDetailView(generic.DetailView):
    model = Call
    template_name = "dispatch/call_details.html"

def new_call(request):
    context = {"calls_nav":"active"}
    return render(request, "dispatch/new_call.html", context)

def closed_calls(request):
    context = {"calls_nav":"active"}
    return render(request, "dispatch/closed_calls.html", context)

def shift(request):
    context = {"shift_nav":"active"}
    return render(request, "dispatch/shift.html", context)

def not_implemented(request):
    context = {}
    return render(request, "dispatch/not_implemented.html", context)

