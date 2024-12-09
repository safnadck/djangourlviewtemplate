from django.shortcuts import render

def home_view(request):
    return render(request, 'cms/home.html')

def about_view(request):
    return render(request, 'cms/about.html')

def contact_view(request):
    return render(request, 'cms/contact.html')

def services_view(request):
    return render(request, 'cms/services.html')

def blog_view(request):
    return render(request, 'cms/blog.html')
