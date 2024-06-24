from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.

@api_view()
def render_index(request):
  return render(request, "index.html")