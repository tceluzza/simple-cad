from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView


from .models import Call, Officer
from .forms import CallForm

# Create your views here.

class CallsListView(generic.ListView):
    paginate_by = 20
    context_object_name = "calls_list"
    template_name = "dispatch/view_calls.html"

    queryset = Call.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["home_nav"] = "active"
        return context

class CallCreateView(CreateView):
    model = Call
    fields = ["name"]
    template_name = "dispatch/call_create_form.html"
    

class CallUpdateView(UpdateView):
    model = Call
    fields = ["name", "active", "notes",]
    template_name = "dispatch/call_update_form.html"

class CallDeleteView(DeleteView):
    model = Call
    success_url = reverse_lazy("dispatch:view_calls")


# class CallFormView(generic.FormView):
#     template_name = "dispatch.call_details.html"
#     form_class = CallForm
#     success_url = "#"

class CallDetailView(generic.DetailView):
    model = Call
    template_name = "dispatch/call_details.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["calls_nav"] = "active"
        
        avofc = Officer.objects.filter(active_call=None)
        if (avofc.count() > 0):
            context["available_officers"] = avofc
        
        return context

def new_call(request):
    context = {"calls_nav":"active",
               "new_call_nav":"active",
               }
    return render(request, "dispatch/new_call.html", context)

def closed_calls(request):
    context = {"calls_nav":"active",
               "closed_calls_nav":"active",
               }
    return render(request, "dispatch/closed_calls.html", context)

def shift(request):
    context = {"shift_nav":"active"}
    return render(request, "dispatch/shift.html", context)

def not_implemented(request):
    context = {}
    return render(request, "dispatch/not_implemented.html", context)

