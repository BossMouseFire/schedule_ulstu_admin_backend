from rest_framework import routers
from .views import TableUsersView, TableScheduleDaysView, TableSchedulePictureView
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
router = routers.SimpleRouter()

router.register('users', TableUsersView, basename='users')
router.register('weeks', TableSchedulePictureView, basename='weeks')
router.register('days', TableScheduleDaysView, basename='days')
urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/login', obtain_jwt_token, name='token'),
    path('auth/verify-token', verify_jwt_token, name='verify-token')

]

urlpatterns += router.urls
