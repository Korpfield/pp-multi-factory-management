from django.shortcuts import render
from .mock_project import project_json
import json

# Main page
def index(request):
    return render(request, 'main/index.html', {'projects': project_json['projects']})