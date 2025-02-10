from django.views.generic import CreateView, FormView, View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.http import HttpResponse


class SignupView(CreateView):
    model = User
    template_name = "accounts/signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("user_login")

    def form_valid(self, form):
        response = super().form_valid(form)
        # 회원가입 후 자동 로그인
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")  # UserCreationForm uses password1
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return response

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        username = request.POST.get("username")
        email = request.POST.get("email", "")

        # 커스텀 유효성 검사
        if not username:
            return HttpResponse("이름과 패스워드는 필수입니다.")
        if User.objects.filter(username=username).exists():
            return HttpResponse("유저이름이 이미 있습니다.")
        if email and User.objects.filter(email=email).exists():
            return HttpResponse("이메일이 이미 있습니다.")

        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)


class LoginView(FormView):
    template_name = "accounts/login.html"
    form_class = AuthenticationForm
    success_url = "/blog"

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form, error="아이디나 패스워드가 맞지 않습니다.")
        )


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("user_login")
