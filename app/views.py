from django.shortcuts import get_object_or_404, redirect, render
from .models import App
from .forms import AppForm
from django.shortcuts import get_object_or_404
# Create your views here.
def index(request):
    return render(request, 'index.html')
   
def app_list(request):
    apps = App.objects.all().order_by('-created_at')
    return render(request, 'app_list.html', {'apps': apps})

def app_create(request):
    if request.method == 'POST':
        form = AppForm(request.POST, request.FILES)
        if form.is_valid():
            app = form.save(commit=False)
            app.user = request.user
            app.save()
            return redirect('app_list')
    else:
        form = AppForm()
    return render(request, 'app_form.html', {'form': form})

def app_edit(request, app_id):
    app = get_object_or_404(App, pk=app_id, user=request.user)
    if request.method == 'POST':
        form = AppForm(request.POST, request.FILES, instance=app)
        if form.is_valid():
            app.user = form.save(commit=False)
            app.user = request.user
            app.save()
            return redirect('app_list')
    else:
        form = AppForm(instance=app)
    return render(request, 'app_form.html', {'form': form})

def app_delete(request, app_id):
    app = get_object_or_404(App, pk=app_id, user=request.user)
    if request.method == 'POST':
        app.delete()
        return redirect('app_list')
    return render(request, 'app_confirm_delete.html', {'app': app})