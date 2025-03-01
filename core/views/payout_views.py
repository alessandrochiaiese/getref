from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..models.payout import Payout
from ..forms import PayoutForm
from django.contrib.auth.decorators import login_required

@login_required
def payout_list(request):
    payout_items = Payout.objects.all()
    return render(request, 'core/payout_list.html', {'payout_items': payout_items})

@login_required
def payout_detail(request, pk):
    payout_item = get_object_or_404(Payout, pk=pk)
    return render(request, 'core/payout_detail.html', {'payout_item': payout_item})

@login_required
def create_payout(request):
    if request.method == 'POST':
        form = PayoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payout_list')
    else:
        form = PayoutForm()
    return render(request, 'core/payout_create.html', {'form': form})

@login_required
def update_payout(request, pk):
    payout_item = get_object_or_404(Payout, pk=pk)
    if request.method == 'POST':
        form = PayoutForm(request.POST, instance=payout_item)
        if form.is_valid():
            form.save()
            return redirect('payout_detail', pk=payout_item.pk)
    else:
        form = PayoutForm(instance=payout_item)
    return render(request, 'core/payout_update.html', {'form': form})

@login_required
def delete_payout(request, pk):
    payout_item = get_object_or_404(Payout, pk=pk)
    if request.method == 'POST':
        payout_item.delete()
        return redirect('payout_list')
    return render(request, 'core/payout_delete.html', {'payout_item': payout_item})
