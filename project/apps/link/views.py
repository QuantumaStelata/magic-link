from django.shortcuts import render
from django.core.mail import EmailMessage
from .models import Link
import random

# Create your views here.

def main(request):
    return render(request, 'main.html')

def index(request):
    try:
        url = request.path[1:]
        token = Link.objects.get(token=url)

        if token.active == True:
            token.number_visits = int(token.number_visits) + 1
            token.save()

            return render(request, 'correct.html', {'n': token.number_visits})
        
        error = 'Error. Token is not active'
        return render(request, 'error.html', {'error': error}) 
    except:
        error = 'Error. Invalid token'
        return render(request, 'error.html', {'error': error})

def send_email(request):
    user_email = request.POST['email']
    token = ''.join(str(random.randint(0,9)) for i in range(4))
    subject = 'Token'
    body = 'Your Token - {}\nYour link - 127.0.0.1:8000/{}'.format(token, token)

    try:
        email = EmailMessage(subject=subject, body=body, to=[user_email])
        email.send()

        Link.objects.create(email=user_email, token=token)

        return render(request, 'send_email.html', {'email': user_email})
    except:
        error = 'Error. Invalid email'
        return render(request, 'error.html', {'error': error})
