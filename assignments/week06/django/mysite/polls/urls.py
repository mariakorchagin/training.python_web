from django.conf.urls import patterns, url
from django.views.generic import ListView
from polls.models import Poll

urlpatterns = patterns('',
  url(r'^$', 
    ListView.as_view(
        queryset=Poll.objects.order_by('-pub_date')[:5],
        context_object_name='polls',
        template_name="polls/list.html"
    ), name="poll_list"),
)