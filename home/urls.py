from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("browse/", views.browse, name='browse'),
    path("dare/", views.dare, name='dare'),
    path("about/", views.about, name='about_us'),
    path("contact/", views.contact, name='contact_us'),
    path('create-dare/', views.create_dares, name='create_dares'), 
    path("delete-dare/<int:id>",views.delete_dare,name="delete_dare"),

    path('display/',views.display,name='display'),
    path('display_contact/',views.dcontact,name='dcontact'),
    path("edit-dare/<int:id>",views.edit_dare,name="edit_dare"),


]