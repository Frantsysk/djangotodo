from django.urls import path
from .views import todopage, addtask, deletetask, details, deleteall, update, updatetask

urlpatterns = [
    path('', todopage, name = 'todomain'),
    path('addnewtask', addtask, name = 'newtask'),
    path('deteletask', deletetask, name='deletetask'),
    path('deteleall', deleteall, name='deleteall'),
    path('update/<int:pk>/', update, name='update'),
    path('updatetask/<int:pk>', updatetask, name='updatetask'),
    path('details/<int:pk>/', details, name='details')
]