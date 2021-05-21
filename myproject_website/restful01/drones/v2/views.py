from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from ..views import DroneCategoryList, DroneList, PilotList, CompetitionList


class ApiRootVersion2(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'vehicle-categories': reverse(DroneCategoryList.name, request=request),
            'vehicles': reverse(DroneList.name, request=request),
            'pilots': reverse(PilotList.name, request=request),
            'competitions': reverse(CompetitionList.name, request=request)

        })