from django.urls import path
from .views import ActivityDetail, AddTodo, DeleteTodo,UpdateTodo

urlpatterns = [
    path('', ActivityDetail.as_view(), name='home'),
    path('Add/', AddTodo.as_view(), name='addTodo'),
    path('delete/<int:pk>', DeleteTodo.as_view(), name='deleteView'),
    path('update/<int:pk>',UpdateTodo.as_view(),name='updateView')
]
