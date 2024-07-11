from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PasswordGeneratorForm
import random
import string
from .models import AmazonPassword, FlipkartPassword, AWSPassword

def generate_password(length):
    # Ensure password contains at least 1 upper case, 1 lower case, and 1 numeric digit
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits)
    ]
    # Fill the rest of the password length with random characters
    for _ in range(length - 3):
        password.append(random.choice(string.ascii_letters + string.digits))
    # Shuffle the list to ensure randomness
    random.shuffle(password)
    return ''.join(password)

def password_generator_view(request):
    if request.method == 'POST':
        form = PasswordGeneratorForm(request.POST)
        if form.is_valid():
            length = form.cleaned_data['length']
            count = form.cleaned_data['count']
            passwords = [generate_password(length) for _ in range(count)]
            return render(request, 'generator/passwords.html', {'passwords': passwords})
    else:
        form = PasswordGeneratorForm()
    return render(request, 'generator/form.html', {'form': form})

def save_service_password(request, service_name, password):
    if service_name == 'amazon':
        AmazonPassword.objects.create(password=password)
        return HttpResponse('Amazon password saved successfully!')
    elif service_name == 'flipkart':
        FlipkartPassword.objects.create(password=password)
        return HttpResponse('Flipkart password saved successfully!')
    elif service_name == 'aws':
        AWSPassword.objects.create(password=password)
        return HttpResponse('AWS password saved successfully!')
    else:
        return HttpResponse('Invalid service name', status=400)

def retrieve_password_view(request, service_name):
    if service_name == 'amazon':
        passwords = AmazonPassword.objects.all()
    elif service_name == 'flipkart':
        passwords = FlipkartPassword.objects.all()
    elif service_name == 'aws':
        passwords = AWSPassword.objects.all()
    else:
        return HttpResponse('Invalid service name', status=400)
    
    if passwords.exists():
        password_list = [password.password for password in passwords]
        return HttpResponse(', '.join(password_list))
    else:
        return HttpResponse(f'No passwords found for {service_name}.', status=404)

def main_page_view(request):
    services = ['Amazon', 'Flipkart', 'AWS']
    return render(request, 'generator/main.html', {'services': services})