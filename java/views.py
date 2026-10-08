from django.shortcuts import render, get_object_or_404, redirect
from .models import Kik
from django.contrib.auth import login as auth_login, logout as auth_logout , authenticate ,get_user_model

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import logging
logger = logging.getLogger(__name__)

from django.shortcuts import redirect


  
@login_required(login_url='salom')
def home(request):
    kik = Kik.objects.all()
    return render(request, 'home.html', {"kik": kik})

def logo(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username:
            messages.error(
                request,
                "Iltimos, foydalanuvchi nomini kiriting"
            )
            return redirect("logo")

        try:
            user = User.objects.get(username=username)

            if user.is_superuser:
                auth_login(request, user)
                logger.info("Admin tizimga kirdi")
                return redirect("home")
            else:
                if not password:
                    logger.warning(
                        username,
                        "Login qilishda Nomalum xato"
                    )
                    return redirect("logo")

                user = authenticate(
                    request,
                    username=username,
                    password=password
                )

                if user:
                    auth_login(request, user)
                    messages.success(
                        request,
                        "Siz muvaffaqiyatli tizimga kirdingiz"
                    )
                    return redirect("home")
                else:
                    logger.warning(
                        username,
                        "Login qilishda Nomalum xato"
                    )
                    return redirect("logo")

        except User.DoesNotExist:
            messages.error(
                request,
                "Bunday foydalanuvchi mavjud emas"
            )
            return redirect("logo")

    return render(request, "logo.html")


def salom(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        parolni_taslash = request.POST.get("parolni_taslash")

        if password != parolni_taslash:
            messages.error(request, "Parollar mos kelmadi, qayta tekshiring")
            return redirect("salom")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Bunday email mavjud")
            return redirect("salom")

        user = User.objects.create_user(
            email=email,
            username=username,
            password=password
        )
        user.save()

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            auth_login(request, user)
            messages.success(
                request,
                "Siz muvaffaqiyatli ro'yxatdan o'tdingiz"
            )
            return redirect("salom")
        else:
            messages.error(request, "Noma'lum xatolik")
            return redirect("home")

    return render(request, "salom.html")

def reklama(request):
    return render(request, 'reklama.html', )


def detail(request, tovar_id):
    kik = get_object_or_404(Kik, id=tovar_id)

    context = {
        'kik': kik,

  
    }   
    return render(request, 'detail.html', context)

def chiqish(request):
    auth_logout(request)
    return redirect("home")

def loyiha(request):
    return render(request, 'loyiha.html')
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username:
            messages.error(
                request,
                "Iltimos, foydalanuvchi nomini kiriting"
            )
            return redirect("login")

        try:
            user = User.objects.get(username=username)

            if user.is_superuser:
                auth_login(request, user)
                logger.info("Admin tizimga kirdi")
                return redirect("loyiha")
            else:
                if not password:
                    logger.warning(
                        username,
                        "Login qilishda Nomalum xato"
                    )
                    return redirect("login")

                user = authenticate(
                    request,
                    username=username,
                    password=password
                )

                if user:
                    auth_login(request, user)
                    messages.success(
                        request,
                        "Siz muvaffaqiyatli tizimga kirdingiz"
                    )
                    return redirect("loyiha")
                else:
                    logger.warning(
                        username,
                        "Login qilishda Nomalum xato"
                    )
                    return redirect("login")

        except User.DoesNotExist:
            messages.error(
                request,
                "Bunday foydalanuvchi mavjud emas"
            )
            return redirect("login")

    return render(request, "login.html")


def yolhat(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        parolni_taslash = request.POST.get("parolni_taslash")

        if password != parolni_taslash:
            messages.error(request, "Parollar mos kelmadi, qayta tekshiring")
            return redirect("yolhat")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Bunday email mavjud")
            return redirect("yolhat")

        user = User.objects.create_user(
            email=email,
            username=username,
            password=password
        )
        user.save()

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            auth_login(request, user)
            messages.success(
                request,
                "Siz muvaffaqiyatli ro'yxatdan o'tdingiz"
            )
            return redirect("yolhat")
        else:
            messages.error(request, "Noma'lum xatolik")
            return redirect("home")

    return render(request, "yolhat.html")