from django.shortcuts import render, redirect
from news.models import News, Category, User
from news.forms import CreateCategoryForm, CreateNewsForm
from rest_framework import viewsets
from news.serializers import CategorySerializer, UserSerializer


def index(request):
    context = {"news": News.objects.all()}
    return render(request, "home.html", context)


def news_details(request, id):
    context = {"news": News.objects.get(id=id)}
    return render(request, "news_details.html", context)


def categories(request):
    form = CreateCategoryForm()

    if request.method == "POST":
        form = CreateCategoryForm(request.POST)
        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect("home-page")

    context = {"form": form}
    return render(request, "categories_form.html", context)


def news(request):
    form = CreateNewsForm()

    if request.method == "POST":
        form = CreateNewsForm(request.POST, request.FILES)
        if form.is_valid():
            news_instance = News(
                title=form.cleaned_data["title"],
                content=form.cleaned_data["content"],
                author=form.cleaned_data["author"],
                created_at=form.cleaned_data["created_at"],
                image=form.cleaned_data["image"],
            )
            news_instance.save()

            news_instance.categories.set(form.cleaned_data["categories"])
            return redirect("home-page")

    context = {"form": form}
    return render(request, "news_form.html", context)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
