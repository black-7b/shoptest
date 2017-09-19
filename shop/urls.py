from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<category_slug>[-\w]+)/$', views.ProductList, name='ProductListByCategory'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.ProductDetail, name='ProductDetail'),
    url(r'^$', views.ProductList, name='ProductList'),
   # url(r'^$', views.post_list, name='post_list'),
   # url(r'^(?P<id>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<id>\d+)/new/$', views.post_new, name='post_new'),
]