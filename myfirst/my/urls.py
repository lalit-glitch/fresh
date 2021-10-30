from django.urls import include, path
from rest_framework import routers
# from .import views
from rest_framework_simplejwt import views as jwt_views
from .views import AdminViewSet,SignupViewSet,DateViewSet,LoginViewSet
# from .views import UserViewSet
from rest_framework import viewsets
from .views import ItemListView,AdvListView

router = routers.DefaultRouter()
router.register(r'admin/advisor', AdminViewSet)
router.register(r'register', SignupViewSet)
router.register(r'user-id/advisor/advisor-id', DateViewSet)
router.register(r'login', LoginViewSet)


app_name='my'

urlpatterns = [
   path('', include(router.urls)),
   path('user-id/advisor/',ItemListView.as_view()),
   path('user-id/advisor/booking',AdvListView.as_view()),
]
