from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..models.tier import Tier
from ..forms import TierForm
from django.contrib.auth.decorators import login_required

@login_required
def tier_list(request):
    tier_items = Tier.objects.all()
    return render(request, 'core/tier_list.html', {'tier_items': tier_items})

@login_required
def tier_detail(request, pk):
    tier_item = get_object_or_404(Tier, pk=pk)
    return render(request, 'core/tier_detail.html', {'tier_item': tier_item})

@login_required
def create_tier(request):
    if request.method == 'POST':
        form = TierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tier_list')
    else:
        form = TierForm()
    return render(request, 'core/tier_create.html', {'form': form})

@login_required
def update_tier(request, pk):
    tier_item = get_object_or_404(Tier, pk=pk)
    if request.method == 'POST':
        form = TierForm(request.POST, instance=tier_item)
        if form.is_valid():
            form.save()
            return redirect('tier_detail', pk=tier_item.pk)
    else:
        form = TierForm(instance=tier_item)
    return render(request, 'core/tier_update.html', {'form': form})

@login_required
def delete_tier(request, pk):
    tier_item = get_object_or_404(Tier, pk=pk)
    if request.method == 'POST':
        tier_item.delete()
        return redirect('tier_list')
    return render(request, 'core/tier_delete.html', {'tier_item': tier_item})
