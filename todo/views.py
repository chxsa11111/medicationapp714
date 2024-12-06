from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import TodoModel, VaccinationTodoModel
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import TodoForm, VaccinationTodoForm

from django.contrib import messages
from django.db.models import Q
from django.views import generic


# ToDoの一覧表示機能
class TodoList(ListView):
    template_name = 'todo/list.html'
    model = TodoModel
    
    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        query = self.request.GET
    
        if keyword := query.get('keyword'):
            queryset = queryset.filter(title__icontains=keyword)
        
        return queryset.order_by('-created_at','-update_at','duedate')


# ToDoの詳細表示機能
class TodoDetail(DetailView):
    template_name = 'todo/detail.html'
    model = TodoModel

# ToDoの作成機能
class TodoCreate(CreateView):
    template_name = 'todo/create.html'
    model = TodoModel
    fields = ('title','contents','img','created_at','update_at', 'duedate')
    success_url = reverse_lazy('todo:list')
    
    
    def create(request):
        if request.method == 'POST':
            form = TodoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
            return render(request,'todo/list.html')

# ToDoの削除機能
class TodoDelete(DeleteView):
    template_name = 'todo/delete.html'
    model = TodoModel
    success_url = reverse_lazy('todo:list')

# ToDoの編集機能
class TodoUpdate(UpdateView):
    template_name = 'todo/update.html'
    model = TodoModel
    fields = ('title','contents','img','created_at','update_at','duedate')
    success_url = reverse_lazy('todo:list')
    
    def update(request):
        if request.method == 'POST':
            form = TodoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
            return render(request,'todo/list.html')

# ToDoの画像アップロード機能
class ImageUploadView(CreateView):
    template_name = 'todo/image_upload.html'
    form_class = TodoForm
    success_url = reverse_lazy('todo:list')




# VaccinationToDoの一覧表示機能
class VaccinationTodoList(ListView):
    template_name = 'todo/vaccinationlist.html'
    model = VaccinationTodoModel
    
    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        query = self.request.GET
    
        if keyword := query.get('keyword'):
            queryset = queryset.filter(title__icontains=keyword)
        
        return queryset.order_by('-created_at','-update_at','duedate')



# VaccinationToDoの詳細表示機能
class VaccinationTodoDetail(DetailView):
    template_name = 'todo/vaccinationdetail.html'
    model = VaccinationTodoModel

# VaccinationToDoの作成機能
class VaccinationTodoCreate(CreateView):
    template_name = 'todo/vaccinationcreate.html'
    model = VaccinationTodoModel
    fields = ('title','contents','img','created_at','update_at','duedate')
    success_url = reverse_lazy('todo:vaccinationlist')

    def create(request):
        if request.method == 'POST':
            form = VaccinationTodoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
            return render(request,'todo/vaccinationlist.html')


# VaccinationToDoの削除機能
class VaccinationTodoDelete(DeleteView):
    template_name = 'todo/vaccinationdelete.html'
    model = VaccinationTodoModel
    success_url = reverse_lazy('todo:vaccinationlist')

# VaccinationToDoの編集機能
class VaccinationTodoUpdate(UpdateView):
    template_name = 'todo/vaccinationupdate.html'
    model = VaccinationTodoModel
    fields = ('title','contents','img','created_at','update_at','duedate')
    success_url = reverse_lazy('todo:vaccinationlist')


    def update(request):
        if request.method == 'POST':
            form = VaccinationTodoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
            return render(request,'todo/vaccinationlist.html')
