from django.urls import path
from .views import home
from .views import *

urlpatterns = [
    path('', home, name='crud_home'),          # /crud/
    path('home/', home, name='home'),           # /crud/home/
    path('add_crud/', crud_add, name='add_crud'),
    path('delete_crud/<int:roll>/', crud_delete, name='delete_crud'),
    path('update_crud/<int:roll>/', crud_update, name='update_crud'),
    path('docrud_update/<int:roll>/', docrud_update, name='update_docrud'),

]
