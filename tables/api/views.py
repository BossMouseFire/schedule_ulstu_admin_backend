from rest_framework import viewsets
from .serializers import BotUsersSerializers, BotSchedulePicturesSerializers, BotScheduleUlSTUSerializers
from ..models import BotUsers, BotSchedulePictures, BotScheduleUlSTU
from rest_framework.response import Response
from rest_framework.decorators import action
# from rest_framework import permissions


class TableUsersView(viewsets.ModelViewSet):
    queryset = BotUsers.objects.all()
    serializer_class = BotUsersSerializers
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def get_ids(self, request):
        array_vk_ids = []
        users = BotUsers.objects.all()
        for user in users:
            array_vk_ids.append(user.user_id)
        return Response({'vk_ids': array_vk_ids})

    @action(detail=False, methods=['get'])
    def get_specific_ids(self, request):
        query_params = self.request.query_params
        users = BotUsers.objects.all()
        groups = query_params.get('groups', None)
        groups = groups.split(',')

        array_vk_ids = []

        for group in groups:
            for user in users:
                group = group.lower()
                group_name = user.group_name.lower()
                if group == group_name:
                    array_vk_ids.append(user.user_id)
                    
        return Response({'vk_ids': array_vk_ids})


class TableSchedulePictureView(viewsets.ModelViewSet):
    queryset = BotSchedulePictures.objects.all()
    serializer_class = BotSchedulePicturesSerializers
    # permission_classes = [permissions.IsAuthenticated]


class TableScheduleDaysView(viewsets.ModelViewSet):
    queryset = BotScheduleUlSTU.objects.all()
    serializer_class = BotScheduleUlSTUSerializers
    # permission_classes = [permissions.IsAuthenticated]
