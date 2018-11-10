from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        #Check if user already made an inquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquery for this listing')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, 
                            message=message, user_id=user_id )
        
        #Save the details into contact table.    
        contact.save()

        #Sending Email after submited
        send_mail(
            'Property listing Inquery',
            'There has been an inquery for'+ listing + '. sign into admin panel for more information : http://127.0.0.1:8000/admin',
            'prateekakshu@gmail.com',
            [realtor_email,email],
            fail_silently=False)
        
        messages.success(request,'Your message has been submited. Realtor will get back to you soon.')

        return redirect('/listings/'+listing_id)
                        
        
