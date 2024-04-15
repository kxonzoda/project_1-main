from django.shortcuts import render, redirect, get_object_or_404
from user.forms import SignUpForm, CustomLoginForm
from user.models import User, Follow
from blog.models import Post
from django.contrib.auth import logout
from django.core.paginator import Paginator
from django.contrib.auth.views import LoginView, LogoutView

####
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required


def is_superuser(user):
    return user.is_authenticated and user.is_superuser


check_is_superuser = user_passes_test(is_superuser)
####


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user:sign_in")
    else:
        form = SignUpForm()
    data = {
        "form": form,
    }
    return render(request, 'registration/signup.html', data)


class LoginView(LoginView):
    template_name = "registration/signin.html"
    authentication_form = CustomLoginForm


@login_required
def dashboard(request, id):
    user = get_object_or_404(User, id=id)
    if request.user != user:
        return redirect('blog:home')
    user_posts = Post.objects.filter(author=user)
    posts__count = user_posts.count()
    paginitor = Paginator(user_posts, 5)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginitor.page(page_number)
    except:
        posts = paginitor.page(1)

    data = {
        'user': user,
        'posts': posts,
        'posts__count': posts__count,
    }

    return render(request, 'dashboard.html', data)


@login_required
def profile(request, id):
    user = get_object_or_404(User, id=id)
    message = False
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        avatar = request.FILES.get('avatar')
        phone = request.POST.get('phone')
        job = request.POST.get('job')
        bio = request.POST.get('bio')
        user.full_name = full_name
        user.phone = phone
        user.job = job
        user.bio = bio
        user.avatar = avatar
        user.save()
        message = True

    try:
        status = Follow.objects.filter(
            user=user, follower=request.user).exists()
    except:
        status = None

    data = {
        'user': user,
        "status": status,
        "message": message,
    }

    return render(request, 'profile.html', data)


@login_required
def follow(request, id):
    user = get_object_or_404(User, id=id)

    following, created = Follow.objects.get_or_create(
        user=user, follower=request.user)

    if not created:
        following.delete()

    return redirect('user:profile', id=user.id)


@login_required
def follow_info(request, id):
    user = get_object_or_404(User, id=id)

    data = {
        'user': user,
    }

    return render(request, 'follow_info.html', data)


@login_required
def user_logout(request):
    logout(request)
    return redirect('blog:home')
