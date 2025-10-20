from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView, name= 'home'),
    path('detail/<int:todo_id>', views.DetailView, name= 'detail'),
    path('delete/<int:todo_id>', views.DeleteView, name= 'delete'),
    path('create/', views.CreateView, name= 'create'),
    path('update/<int:todo_id>', views.UpdateView, name= 'update'),
]
