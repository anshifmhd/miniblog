from django.urls import path
from . import views

app_name = "user"
urlpatterns = [
    path('index',views.index, name='index'),
    path('',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('add_blog',views.add_blog, name='add_blog'),
    path('edit_profile',views.edit_profile, name='edit_profile'),
    path('change_password',views.change_password, name='change_password'),
    path('comment/<int:idd>',views.comment, name='comment'),
    path('view_comment/<int:idd>',views.view_comment, name='view_comment'),







]