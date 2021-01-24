from rest_framework import routers
from .views import TableUsersView, TableScheduleDaysView, TableSchedulePictureView
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
router = routers.SimpleRouter()

router.register('users', TableUsersView, basename='users')
router.register('weeks', TableSchedulePictureView, basename='weeks')
router.register('days', TableScheduleDaysView, basename='days')
urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/token', obtain_auth_token, name='token')
]

urlpatterns += router.urls
