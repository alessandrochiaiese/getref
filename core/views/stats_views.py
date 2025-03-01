from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..models.stats import Stats
from ..forms import StatsForm
from django.contrib.auth.decorators import login_required

@login_required
def stats_list(request):
    stats_items = Stats.objects.all()
    return render(request, 'core/stats_list.html', {'stats_items': stats_items})

@login_required
def stats_detail(request, pk):
    stats_item = get_object_or_404(Stats, pk=pk)
    return render(request, 'core/stats_detail.html', {'stats_item': stats_item})

@login_required
def create_stats(request):
    if request.method == 'POST':
        form = StatsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stats_list')
    else:
        form = StatsForm()
    return render(request, 'core/stats_create.html', {'form': form})

@login_required
def update_stats(request, pk):
    stats_item = get_object_or_404(Stats, pk=pk)
    if request.method == 'POST':
        form = StatsForm(request.POST, instance=stats_item)
        if form.is_valid():
            form.save()
            return redirect('stats_detail', pk=stats_item.pk)
    else:
        form = StatsForm(instance=stats_item)
    return render(request, 'core/stats_update.html', {'form': form})

@login_required
def delete_stats(request, pk):
    stats_item = get_object_or_404(Stats, pk=pk)
    if request.method == 'POST':
        stats_item.delete()
        return redirect('stats_list')
    return render(request, 'core/stats_delete.html', {'stats_item': stats_item})
