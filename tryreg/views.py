from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response


def index(request):
    return HttpResponse('''<a href="{}">Register</a> | <a href="{}">Login in</a>
        '''.format(reverse('registration_register'), reverse('auth_login')))


def newHomepage(request):
    return render_to_response('html/index.html')


def newlogin(request):
    return render_to_response('registration/login.html')

