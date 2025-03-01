from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..models.performance import Performance
from ..forms import PerformanceForm
from django.contrib.auth.decorators import login_required

@login_required
def performance_list(request):
    performance_items = Performance.objects.all()
    return render(request, 'core/performance_list.html', {'performance_items': performance_items})

@login_required
def performance_detail(request, pk):
    performance_item = get_object_or_404(Performance, pk=pk)
    return render(request, 'core/performance_detail.html', {'performance_item': performance_item})

@login_required
def create_performance(request):
    if request.method == 'POST':
        form = PerformanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('performance_list')
    else:
        form = PerformanceForm()
    return render(request, 'core/performance_create.html', {'form': form})

@login_required
def update_performance(request, pk):
    performance_item = get_object_or_404(Performance, pk=pk)
    if request.method == 'POST':
        form = PerformanceForm(request.POST, instance=performance_item)
        if form.is_valid():
            form.save()
            return redirect('performance_detail', pk=performance_item.pk)
    else:
        form = PerformanceForm(instance=performance_item)
    return render(request, 'core/performance_update.html', {'form': form})

@login_required
def delete_performance(request, pk):
    performance_item = get_object_or_404(Performance, pk=pk)
    if request.method == 'POST':
        performance_item.delete()
        return redirect('performance_list')
    return render(request, 'core/performance_delete.html', {'performance_item': performance_item})
