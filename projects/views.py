from django.shortcuts import render
from django.http import HttpResponse

data = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]

def projects(request):
    return render(request, 'projects.html', {'data':data})

def project(request, pk):
    content = None
    for project in data:
        if project['id'] == str(pk):
            content = project
    return render(request, 'project.html', context=content)

