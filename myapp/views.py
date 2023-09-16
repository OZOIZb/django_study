from django.shortcuts import render, HttpResponse

topics = [
    {'id':1, 'title':'Routing', 'body':'Routing is ...'},
    {'id':2, 'title':'View', 'body':'View is ...'},
    {'id':3, 'title':'Model', 'body':'Model is ...'},
]

def HTMLTemplate():
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
    <html>
    <body>
        <h1>Django</h1>
        <ol>
            {ol}
        </ol>
        <h2>Welcome</h2>
        Hello, Django
    </body>
    </html>
    '''

def index(request):
    return HttpResponse(HTMLTemplate())

def read(request, id):
    return HttpResponse('Read!'+id)

def create(request):
    return HttpResponse('Create!')
