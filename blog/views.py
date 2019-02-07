from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Article
from .models import Query
from blog.forms import Query
from django.contrib.auth.decorators import login_required
from blog.forms import CreateArticle



def article_list(request):
    articles = Article.objects.all().order_by('date');
    return render(request, 'blog/article_list.html', { 'articles': articles })

def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'blog/article_detail.html', { 'article': article })


@login_required(login_url="/users/login/")
def article_create(request):
    title = "Create an Article"
    if request.method == 'POST':
        form = CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return HttpResponseRedirect(reverse('article_list'))
    else:
        form = CreateArticle()

    context = {"title": title, "form": form}
    return render(request, 'blog/article_create.html', context)



def register_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        title = "Create an Account"
        form = UserRegistrationForm(
            request.POST or None,
            request.FILES or None
            )

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()
            new_user = authenticate(email=user.email, password=password)
            login(request, new_user)

            return HttpResponseRedirect(reverse('home_page'))

        context = {"title": title, "form": form}

        return render(request, "users/form.html", context)

def query_create(request):
    title= "Query"
    if request.method == 'POST':
        form = Query(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            user = request.user
            instance.save()
            return HttpResponseRedirect(reverse('home_page'))
    else:
        form = Query()
    context = {"title": title, "form": form}
    return render(request, 'blog/form.html', context )




def contact_us(request):
    return render(request, 'blog/contact_us.html')

def home_page(request):
    return render(request, 'blog/homepage.html')

def about(request):
    return render(request, 'about.html')
