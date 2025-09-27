from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def contact_view(request):
    success = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # You can customize the email sending or save to DB as needed
        send_mail(
            subject=f'Agri Community Contact from {name}',
            message=f'From: {name} <{email}>\n\n{message}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
            fail_silently=True,
        )
        success = True
    return render(request, 'contact.html', {'success': success})
