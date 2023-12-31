from django.urls import path

from . import views

app_name = "dispatch"
urlpatterns = [
    path("", views.CallsListView.as_view(), name="view_calls"),
    # path("view-call/<int:pk>/", views.CallDetailView.as_view(), name="call_details"),
    
    path("call/add/", views.CallCreateView.as_view(), name="call_add"),
    path("call/<int:pk>/", views.CallUpdateView.as_view(), name="call_update"),
    path("call/<int:pk>/delete", views.CallDeleteView.as_view(), name="call_delete"),
    
    path("closed-calls/", views.closed_calls, name="closed_calls"),
    path("shift/", views.shift, name="shift"),
    path("not-implemented/", views.not_implemented, name="not_implemented"),
]
