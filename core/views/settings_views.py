from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..models.settings import Settings
from ..forms import SettingsForm
from django.contrib.auth.decorators import login_required

@login_required
def settings_list(request):
    settings_items = Settings.objects.all()
    return render(request, 'core/settings_list.html', {'settings_items': settings_items})

@login_required
def settings_detail(request, pk):
    settings_item = get_object_or_404(Settings, pk=pk)
    return render(request, 'core/settings_detail.html', {'settings_item': settings_item})

@login_required
def create_settings(request):
    if request.method == 'POST':
        form = SettingsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('settings_list')
    else:
        form = SettingsForm()
    return render(request, 'core/settings_create.html', {'form': form})

@login_required
def update_settings(request, pk):
    settings_item = get_object_or_404(Settings, pk=pk)
    if request.method == 'POST':
        form = SettingsForm(request.POST, instance=settings_item)
        if form.is_valid():
            form.save()
            return redirect('settings_detail', pk=settings_item.pk)
    else:
        form = SettingsForm(instance=settings_item)
    return render(request, 'core/settings_update.html', {'form': form})

@login_required
def delete_settings(request, pk):
    settings_item = get_object_or_404(Settings, pk=pk)
    if request.method == 'POST':
        settings_item.delete()
        return redirect('settings_list')
    return render(request, 'core/settings_delete.html', {'settings_item': settings_item})
