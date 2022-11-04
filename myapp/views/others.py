from django.shortcuts import render

def stationloc(request):
    return render(request, 'stationloc.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blogs.html')

def blog_post(request, slug):
    return render(request, 'blog.html')

# def seat(request):
#     return render(request, 'seat.html')

# def mastercard(request):
#     return render(request, 'mastercard.html')
