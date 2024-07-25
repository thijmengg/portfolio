from typing import Any
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = "index/index.html"