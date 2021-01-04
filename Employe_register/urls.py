from django.urls import path, include
from . import views
urlpatterns = [
        path('',views.employe_form,name='employee_insert'),
        path('delete/<int:id>/',views.employe_delete, name='employe_delete'),
        path('<int:id>/',views.employe_form, name='employee_update'),
        path('list/',views.employe_list,name='employe_list'),
]