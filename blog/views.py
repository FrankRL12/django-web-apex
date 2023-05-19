from django.shortcuts import render
from blog.models import Blog

# Create your views here.
def blog(request):
    blog = Blog.objects.all()
    return render(request, 'templates/blog.html',{"blogs": blog})
