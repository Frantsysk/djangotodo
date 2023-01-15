from django.urls import path
from .views import (
    todopage, addtask, deletetask, details, deleteall, update,
    updatetask, userlogout, authpage, loginaction, signup, signupaction
)

urlpatterns = [
    path('', todopage, name='todomain'),
    path('addnewtask', addtask, name='newtask'),
    path('deteletask', deletetask, name='deletetask'),
    path('deteleall', deleteall, name='deleteall'),
    path('update/<int:pk>/', update, name='update'),
    path('updatetask/<int:pk>', updatetask, name='updatetask'),
    path('details/<int:pk>/', details, name='details'),
    path('userlogout', userlogout, name='userlogout'),
    path('authpage', authpage, name='authpage'),
    path('loginaction', loginaction, name='loginaction'),
    path('signup', signup, name='signup'),
    path('signupaction', signupaction, name='signupaction')
]