from django.shortcuts import render



posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2021'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2021'
    }
]



# Create your views here.

def home(request):
    posts = Post.objects.all()
    

    return render(request, 'blogapp/index.html', {'posts': posts})

def about(request):
    return render(request, 'blogapp/about.html')


