from django.urls import path

from .import views
app_name = "main"
urlpatterns = [
    path("", views.TodoListListView.as_view(), name="index"),
    path("<int:pk>", views.TodoListView.as_view(), name="todolist"),
    path("add_todolist", views.AddTodoListView.as_view(), name="add_todolist"),
    path("add_item/<int:pk>", views.AddListItemView.as_view(), name="add_item"),
    path("delete_item/<int:pk>", views.RemoveListItemView.as_view(), name="delete_item"),
    path("delete_todo/<int:pk>", views.RemoveTodoListView.as_view(), name="delete_todo"),

]