from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..models.referral_level import ReferralLevel
from ..forms import ReferralLevelForm
from django.contrib.auth.decorators import login_required

@login_required
def referral_level_list(request):
    referral_level_items = ReferralLevel.objects.all()
    return render(request, 'core/referral_level_list.html', {'referral_level_items': referral_level_items})

@login_required
def referral_level_detail(request, pk):
    referral_level_item = get_object_or_404(ReferralLevel, pk=pk)
    return render(request, 'core/referral_level_detail.html', {'referral_level_item': referral_level_item})

@login_required
def create_referral_level(request):
    if request.method == 'POST':
        form = ReferralLevelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('referral_level_list')
    else:
        form = ReferralLevelForm()
    return render(request, 'core/referral_level_create.html', {'form': form})

@login_required
def update_referral_level(request, pk):
    referral_level_item = get_object_or_404(ReferralLevel, pk=pk)
    if request.method == 'POST':
        form = ReferralLevelForm(request.POST, instance=referral_level_item)
        if form.is_valid():
            form.save()
            return redirect('referral_level_detail', pk=referral_level_item.pk)
    else:
        form = ReferralLevelForm(instance=referral_level_item)
    return render(request, 'core/referral_level_update.html', {'form': form})

@login_required
def delete_referral_level(request, pk):
    referral_level_item = get_object_or_404(ReferralLevel, pk=pk)
    if request.method == 'POST':
        referral_level_item.delete()
        return redirect('referral_level_list')
    return render(request, 'core/referral_level_delete.html', {'referral_level_item': referral_level_item})
