from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def post_list(request):
    return render(request, "blog/post_list.html", {})
