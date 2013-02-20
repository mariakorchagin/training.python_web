from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from djangor.models import Books
from djangor.forms import BookForm
# from djangor.views import AddEntryView
from django.views.generic import CreateView


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

  url(r'^add/$',
        login_required(CreateView.as_view(
            model=Books,
            form_class=BookForm,
            template_name="books/add.html",
            success_url="/djangor/",
        )),
        name="books_add"),
)