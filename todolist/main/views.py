from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import View, generic

from .models import TodoList, ListItem

class TodoListListView(generic.ListView):
    model = TodoList
    template_name = "index.html"
    def get_queryset(self):
        return TodoList.objects.order_by("-pub_date")

class TodoListView(generic.DetailView):
    model = TodoList
    template_name = "todolist.html"

class AddTodoListView(View):
    def get(self, request):
        return render(request, "add_todolist.html", {})
    def post(self, request):
        try:
            name = request.POST["name"]
            if name=="":
                raise ValueError
        except (KeyError,ValueError):
            return render(
                request,
                "main/add_todolist.html",
                {"error_message" : "Please enter valid input"}
                    )
        else:
            todolist = TodoList(name=name,pub_date=timezone.now())
            todolist.save()
            return HttpResponseRedirect(reverse("main:add_item",args=(todolist.pk,)))

class RemoveTodoListView(View):
    def get(self,request,pk):
        todolist = get_object_or_404(TodoList,pk=pk)
        todolist.delete()
        return HttpResponseRedirect(reverse("main:index"))

class AddListItemView(View):
    def get(self,request,pk):
        todolist = get_list_or_404(TodoList,pk=pk)
        return render(request,"add_item.html", {'todolist' : todolist})
    def post(self,request,pk):
        todolist = get_list_or_404(TodoList,pk=pk)
        try:
            item_text = request.POST["item_text"]
            if item_text=="":
                raise ValueError
        except (KeyError,ValueError):
            return render(
                request,
                "add_item.html",
                {
                    "error_message": "submit valid text",
                }

            )            
        else:
            listitem = ListItem(todolist=todolist,item_text=item_text,pub_date=timezone.now())
            listitem.save()
            return HttpResponseRedirect(reverse("main:todolist", args=(todolist.id,)))

class RemoveListItemView(View):
    def get(self,request,pk):
        listitem = get_object_or_404(ListItem,pk=pk)
        todolist = listitem.todolist
        listitem.delete()
        return HttpResponseRedirect(reverse("main:add_item", args=(todolist.id,)))
            
        

             
            



