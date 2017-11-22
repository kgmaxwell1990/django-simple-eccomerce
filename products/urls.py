from django.conf.urls import url
from .views import all_products, do_search


urlpatterns = [
    url(r'^$', all_products, name="home"),
    url(r'^search', do_search, name="search"),

    ]