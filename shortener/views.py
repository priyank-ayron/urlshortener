from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')


def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:10]
        new_url = Url(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)

def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    link = url_details.link
    if not link.startswith("https://"):
        link = "https://" + link
    return redirect(link)


