from django.conf.urls import url

from . import views


app_name = 'livros'

urlpatterns = [
    url(r'^$', views.show_livros, name='show_livros'),
    url(r'^login/$', views.log_in, name='login'),
    url(r'^logout/$', views.log_out, name='logout'),
    url(r'^add/$', views.add_book, name='add_book')
]
