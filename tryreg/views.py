from django.http import HttpResponse
from django.core.urlresolvers import reverse


def index(request):
    return HttpResponse('''<a href="{}">Register</a> | <a href="{}">Login in</a>
        '''.format(reverse('registration_register'), reverse('auth_login')))
