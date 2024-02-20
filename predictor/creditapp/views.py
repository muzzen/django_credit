from django.shortcuts import render
import pickle
import pandas as pd

def home(request):
        return render(request, 'home.html')