
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact,About,Achievement, Services,Skills,Testimonials,Portfolio


def index(request):
    aboutme = About.objects.get(pk=1)
    achievement=Achievement.objects.get(pk=1)
    skill=Skills.objects.get(pk=1)
    testimonials_section_name=Testimonials.objects.get(pk=1)
    testimonials=Testimonials.objects.all
    service_section=Services.objects.get(pk=1)
    services=Services.objects.all
    portfolio_section=Portfolio.objects.get(pk=1)
    portfolio=Portfolio.objects.all
    web_development_portfolio=Portfolio.objects.filter(category='Web Development')
    web_designing_portfolio=Portfolio.objects.filter(category='Web Designing')
    ecommerce_portfolio=Portfolio.objects.filter(category='eCommerce')
    wordpress_portfolio=Portfolio.objects.filter(category='WordPress')
    if request.method=="POST":
        print(request)
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        desc=request.POST.get('desc', '')
        
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(desc)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, desc=desc)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    context={
        'aboutme':aboutme,'achievement':achievement,
        'skill':skill,'testimonials':testimonials,
        'testimonials_section_name':testimonials_section_name,
        'service_section':service_section,
        'services':services,
        'portfolio_section':portfolio_section,
        'portfolio':portfolio,
        'web_development_portfolio':web_development_portfolio,
        'web_designing_portfolio':web_designing_portfolio,
        'ecommerce_portfolio':ecommerce_portfolio,
        'wordpress_portfolio':wordpress_portfolio
        }
    return render(request, 'index.html',context)

def contact(request):
    if request.method=="POST":
        print(request)
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        desc=request.POST.get('desc', '')
        
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(desc)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, desc=desc)
            contact.save()
            messages.success(request, "Your message has been successfully sent")

    return render(request, 'contact.html')



