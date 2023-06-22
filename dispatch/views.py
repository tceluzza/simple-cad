from django.shortcuts import render

# Create your views here.

def view_calls(request):
    return render(request, "dispatch/view_calls.html", {"nav":"view_calls"})

def new_call(request):
    return render(request, "dispatch/new_call.html", {"nav":"new_call"})

def closed_calls(request):
    return render(request, "dispatch/closed_calls.html", {"nav":"closed_calls"})

def shift(request):
    return render(request, "dispatch/shift.html", {"nav":"shift"})
