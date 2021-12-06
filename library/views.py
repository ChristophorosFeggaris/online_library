from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import BookForm, CreateUserForm
from .models import Book


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def add_book(request):
    form = BookForm()

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'addBook.html', context)

@login_required(login_url='login')
def show_book(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'allBooks.html', context)

@login_required(login_url='login')
def search_book(request):
    if request.method == 'POST':
        search_book = request.POST['searched_book']
        books = Book.objects.filter(title__contains='search_book')
    context = {'books':books}
    return render(request, 'searchBook.html', context)

@login_required(login_url='login')
def delete_book(request):
    pass

def login_student(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    context = {}
    return render(request, 'Login.html', context)

def register_student(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'Register.html', context)

@login_required(login_url='login')
def logout_student(request):
    logout(request)
    return redirect('login')
