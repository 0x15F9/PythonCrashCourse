from django.shortcuts import render

# Create your views here.
def index(request):
    """ The homepage for Learning Logs app """
    return render(request, 'learning_logs/index.html')