from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..models.engagement import Engagement
from ..forms import EngagementForm
from django.contrib.auth.decorators import login_required

@login_required
def engagement_list(request):
    engagement_items = Engagement.objects.all()
    return render(request, 'core/engagement_list.html', {'engagement_items': engagement_items})

@login_required
def engagement_detail(request, pk):
    engagement_item = get_object_or_404(Engagement, pk=pk)
    return render(request, 'core/engagement_detail.html', {'engagement_item': engagement_item})

@login_required
def create_engagement(request):
    if request.method == 'POST':
        form = EngagementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('engagement_list')
    else:
        form = EngagementForm()
    return render(request, 'core/engagement_create.html', {'form': form})

@login_required
def update_engagement(request, pk):
    engagement_item = get_object_or_404(Engagement, pk=pk)
    if request.method == 'POST':
        form = EngagementForm(request.POST, instance=engagement_item)
        if form.is_valid():
            form.save()
            return redirect('engagement_detail', pk=engagement_item.pk)
    else:
        form = EngagementForm(instance=engagement_item)
    return render(request, 'core/engagement_update.html', {'form': form})

@login_required
def delete_engagement(request, pk):
    engagement_item = get_object_or_404(Engagement, pk=pk)
    if request.method == 'POST':
        engagement_item.delete()
        return redirect('engagement_list')
    return render(request, 'core/engagement_delete.html', {'engagement_item': engagement_item})
