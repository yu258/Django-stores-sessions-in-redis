from django.shortcuts import render, HttpResponse


# Create your views here.

def set_session(request):
    request.session['username'] = 'long'
    request.session['passworda'] = '123456a'
    return HttpResponse("设置成功")


def get_session(request):
    username = request.session.get('username')
    password = request.session.get('password')
    passworda = request.session.get('passworda')
    text = 'username=%s, password=%s,passworda=%s' % (username, password,passworda)
    return HttpResponse(text)
