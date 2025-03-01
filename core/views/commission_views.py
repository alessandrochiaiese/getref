from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..models.commission import Commission
from ..forms import CommissionForm
from django.contrib.auth.decorators import login_required

@login_required
def commission_list(request):
    commission_items = Commission.objects.all()
    return render(request, 'core/commission_list.html', {'commission_items': commission_items})

@login_required
def commission_detail(request, pk):
    commission_item = get_object_or_404(Commission, pk=pk)
    return render(request, 'core/commission_detail.html', {'commission_item': commission_item})

@login_required
def create_commission(request):
    if request.method == 'POST':
        form = CommissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('commission_list')
    else:
        form = CommissionForm()
    return render(request, 'core/commission_create.html', {'form': form})

@login_required
def update_commission(request, pk):
    commission_item = get_object_or_404(Commission, pk=pk)
    if request.method == 'POST':
        form = CommissionForm(request.POST, instance=commission_item)
        if form.is_valid():
            form.save()
            return redirect('commission_detail', pk=commission_item.pk)
    else:
        form = CommissionForm(instance=commission_item)
    return render(request, 'core/commission_update.html', {'form': form})

@login_required
def delete_commission(request, pk):
    commission_item = get_object_or_404(Commission, pk=pk)
    if request.method == 'POST':
        commission_item.delete()
        return redirect('commission_list')
    return render(request, 'core/commission_delete.html', {'commission_item': commission_item})
