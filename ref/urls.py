from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import home_view,register



# urls for requests

urlpatterns = [
    path('',views.home_view, name = 'home-page'),
    path('register',views.register,name = 'register'),
    path('register_medic',views.register_medic,name = 'register_medic'),
    path('create_referal',views.create_referal,name='create_referal'),
    path('check_tests',views.check_tests,name = 'check_tests'),
    path('check_tests_medic',views.check_tests_medic,name = 'check_tests_medic'),
    path('testing_details/<int:pk>',views.testing_details,name = 'testing_details'),
    path('testing_printout/<int:test_pk>',views.groups,name='testing_printout'),
    path('testing/<int:pk>/modify', views.testing_update, name='testing_modify'),
    path('testing/<int:pk>/delete', views.TestDeleteView.as_view(), name='testing_delete'),
    path('login',auth_views.LoginView.as_view(template_name='ref/login.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name='ref/logout.html'),name='logout'),
    # where to keep static content
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)