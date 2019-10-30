from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(resquest):
    return HttpResponse("###### You are in the index file. ######")


def hello(resquest):
    return HttpResponse("###### This is another message. ######")

def List_Client(resquest):
    return HttpResponse("###### Here you must list the clients in BD. ######")