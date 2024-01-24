from django.urls import path

from . import views

appname = "uzless"

urlpatterns = [
    path("printer/", views.printerView, name="printerView"),
    path("", views.indexView, name="index"),
    path("contractor/", views.contractorView, name="contractorView"),
    path("spool/", views.spoolView, name="spoolView"),
    path("printer/insert/", views.printerInsertView, name="printerInsert"),
    path("printer/delete/", views.printerDeleteView, name="printerDelete"),
    path("contractor/insert/", views.contractorInsertView, name="contractorInsert"),
    path("contractor/delete/", views.contractorDeleteView, name="contractorDelete"),
    path("spool/insert/", views.spoolInsertView, name="spoolInsert"),
    path("spool/delete/", views.spoolDeleteView, name="spoolDelete"),
]
