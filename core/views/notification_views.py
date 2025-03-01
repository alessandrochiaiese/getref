from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..models.notification import Notification
from ..forms import NotificationForm
from django.contrib.auth.decorators import login_required

@login_required
def notification_list(request):
    notification_items = Notification.objects.all()
    return render(request, 'core/notification_list.html', {'notification_items': notification_items})

@login_required
def notification_detail(request, pk):
    notification_item = get_object_or_404(Notification, pk=pk)
    return render(request, 'core/notification_detail.html', {'notification_item': notification_item})

@login_required
def create_notification(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notification_list')
    else:
        form = NotificationForm()
    return render(request, 'core/notification_create.html', {'form': form})

@login_required
def update_notification(request, pk):
    notification_item = get_object_or_404(Notification, pk=pk)
    if request.method == 'POST':
        form = NotificationForm(request.POST, instance=notification_item)
        if form.is_valid():
            form.save()
            return redirect('notification_detail', pk=notification_item.pk)
    else:
        form = NotificationForm(instance=notification_item)
    return render(request, 'core/notification_update.html', {'form': form})

@login_required
def delete_notification(request, pk):
    notification_item = get_object_or_404(Notification, pk=pk)
    if request.method == 'POST':
        notification_item.delete()
        return redirect('notification_list')
    return render(request, 'core/notification_delete.html', {'notification_item': notification_item})
