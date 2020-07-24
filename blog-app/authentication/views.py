from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model

from .forms import LoginUser, UserRegisterForm
from .tokens import account_activation_token

User = get_user_model()


def login_user(request):
    """
    checking user credentials and allowing access if credentials were matched
    :param request: client request
    :return: redirect to his/her profile
    """
    if request.method == 'POST':
        login_form = LoginUser(request.POST)
        if login_form.is_valid():
            print(login_form.cleaned_data)
            user = authenticate(email=login_form.cleaned_data['email'], password=login_form.cleaned_data['password'])
            print(user)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('blog:blog-list')
                else:
                    messages.warning(request, "User is not active")
                    return redirect('authentication:login-user')

            else:
                messages.warning(request, "Invalid login")
                return redirect('authentication:login-user')

        else:
            login_form = LoginUser(request.POST)
    else:
        login_form = LoginUser()

    return render(request, 'authentication/login.html', {'form': login_form})


def logout_user(request):
    """
    logging out the user
    :param request:
    :return: redirect to login page
    """
    logout(request)
    return redirect('authentication:login-user')


class UserRegisterView(CreateView):
    """
    view allowing user to register
    """
    form_class = UserRegisterForm
    template_name = 'authentication/register.html'
    success_url = '/login'

    def form_valid(self, form):
        self.object = form.save()
        current_site = get_current_site(self.request)
        mail_subject = "Activate Your Blog Account"
        message = render_to_string('authentication/account_activation.html', {
            'user': self.object,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(self.object.pk)),
            'token': account_activation_token.make_token(self.object)
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        messages.info(self.request, "Activate your account before you proceed")
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('authentication:login-user')
    else:
        return HttpResponse('Activation link is invalid!')