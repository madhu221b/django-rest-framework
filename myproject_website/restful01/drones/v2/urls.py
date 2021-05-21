from django.conf.urls import url
from ..views import DroneCategoryList,  DroneDetail, DroneCategoryDetail, DroneList, CompetitionList, CompetitionDetail, PilotList, PilotDetail
from ..v2 import views as views_v2

app_name = 'drones'

urlpatterns = [
    url(r'^vehicle-categories/$',
        DroneCategoryList.as_view(),
        name=DroneCategoryList.name),
    url(r'^vehicle-categories/(?P<pk>[0-9]+)$',
        DroneCategoryDetail.as_view(),
        name=DroneCategoryDetail.name),
    url(r'^vehicles/$',
        DroneList.as_view(),
        name=DroneList.name),
    url(r'^vehicles/(?P<pk>[0-9]+)$',
        DroneDetail.as_view(),
        name=DroneDetail.name),
    url(r'^pilots/$',
        PilotList.as_view(),
        name=PilotList.name),
    url(r'^pilots/(?P<pk>[0-9]+)$',
        PilotDetail.as_view(),
        name=PilotDetail.name),
    url(r'^competitions/$',
        CompetitionList.as_view(),
        name=CompetitionList.name),
    url(r'^competitions/(?P<pk>[0-9]+)$',
        CompetitionDetail.as_view(),
        name=CompetitionDetail.name),
    url(r'^$',
        views_v2.ApiRootVersion2.as_view(),
        name=views_v2.ApiRootVersion2.name)
    ]