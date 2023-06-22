from django.urls import path

from . import views

app_name = "dispatch"
urlpatterns = [
    path("", views.view_calls, name="view_calls"),
    path("new-call", views.new_call, name="new_call"),
    path("closed-calls", views.closed_calls, name="closed_calls"),
    path("shift", views.shift, name="shift"),
]
