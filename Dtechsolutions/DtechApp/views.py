from email.message import Message
from django.shortcuts import redirect, render
from DtechApp.models import ContactForm
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.

def Home(request):
    return render (request, 'uifiles/index.html')

def ConctactData(request):
    if request.method == "POST":
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        subject = request.POST.get('subject',"")
        message = request.POST.get('message',"")
        
        oContactinfo = ContactForm(Name=name,Email=email,Subject=subject,Message=message)
        oContactinfo.save()
        # messages.success(request ,"username all reddy in our database")

        sucess =f'hi {name} sucessfully Sending email'
        message ='''
        Subject:{}
        Message:{}
        From:{}
        '''.format(subject,message,email)
        try:
            send_mail(subject, message,'noreplaybadugudinesh94@gmail.com',recipient_list=['badugudinesh94@gmail.com']) 
            messages.success(request,sucess)
        except:
            messages.error(request,'your emsil sending fail')
        return redirect("/")
        # message ='''
        # Subject:{}
        # Message:{}
        # From:{}
        # '''.format(subject,message,email)
        # try:
        #     send_mail(subject=subject, message=message,'noreplaybadugudinesh94@gmail.com',recipient_list=['badugudinesh94@gmail.com']) 
        #     sucess =f'hi {name} sucessfully Sending email'
        #     messages.success(request,sucess)
        # except:
        #     messages.error("message sennding failuer")     
        # return render(request, 'uifiles/contact.html')
    #     #return HttpResponse(sucess) 
    