from django.conf.urls import url
from flights import views

app_name = "flights"
urlpatterns = [

    # view: create new flight
    # /flight/add/
    # url(r'^add/$', views.FlightCreate.as_view(), name='flight_add'),

    # view: update flight
    # /flight/2/
    # url(r'^(?P<pk>[0-9]+)/$', views.FlightUpdate.as_view(), name='flight_update'),

    # view: delete flight
    # /flight/2/delete/
    # url(r'^(?P<pk>[0-9]+)/delete/$', views.FlightDelete.as_view(), name='flight_delete'),

    # view: flight list
    # ex: /flight/
    url(r'^$', views.FlightIndexView.as_view(), name='flight_index'),

    # view:
    # ex: /flight/check
    url(r'^check/$', views.schedule_ok, name='check_schedule_ok'),


    # view: flight detail
    # /flight/71/
    # url(r'^(?P<pk>[0-9]+)/$', views.FlightDetailView.as_view(), name='flight_detail'),

]
