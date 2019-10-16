from django.conf.urls import url, include
from loginreg import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'login', views.Login)
router.register(r'register', views.Register)
# router.register(r'emails', views.ByEmailId, base_name='email')

urlpatterns = [

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
