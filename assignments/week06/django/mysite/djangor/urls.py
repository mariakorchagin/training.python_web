from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from djangor.models import Books


urlpatterns = patterns('',
  url(r'^$', ListView.as_view(
        queryset=Books.objects.order_by('-pub_date')[:5],
        context_object_name='books',
        template_name="books/list.html"),
    name="books_list"),

  url(r'^(?P<pk>\d+)/$', DetailView.as_view(
        model=Books,
        template_name="books/detail.html"),
    name="books_detail"),

  url(r'^add/$', DetailView.as_view(
        model=Books,
        template_name="books/add.html"),
    name="books_add"),
)