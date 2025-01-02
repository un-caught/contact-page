from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        try:
            send_mail(
                f"Message from {name}",
                f"This message is from {email}\n\n {message}",
                email,
                ["korodeleboluwatife@gmail.com"],
            )
            messages.success(request, "Your message has been sent successfully!")

        except Exception as e:
            messages.error(request, f"An error occurred while sending the message: {e}")
            return render(request, 'contact.html')

        return redirect('contact')
    
    else:
        return render(request, 'contact.html')



