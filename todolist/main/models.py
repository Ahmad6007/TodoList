from django.db import models


class TodoList(models.Model):
    name = models.CharField(max_length=100)
    pub_date = models.DateField()

    def __str__(self) -> str:
        return self.name
    
class ListItem(models.Model):
    todolist = models.ForeignKey(TodoList,on_delete=models.CASCADE)
    item_text = models.CharField(max_length=10000)
    pub_date = models.DateField()

    def __str__(self) -> str:
        return self.item_text
       
