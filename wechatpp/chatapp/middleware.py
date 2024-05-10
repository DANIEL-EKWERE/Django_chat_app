from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect

class ChatAuthorizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call___(self,request):
        if not request.user or request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return self.get_response(request)