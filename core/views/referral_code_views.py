from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..models.referral_code import ReferralCode
from ..forms import ReferralCodeForm
from django.contrib.auth.decorators import login_required

@login_required
def referral_code_list(request):
    referral_code_items = ReferralCode.objects.all()
    return render(request, 'core/referral_code_list.html', {'referral_code_items': referral_code_items})

@login_required
def referral_code_detail(request, pk):
    referral_code_item = get_object_or_404(ReferralCode, pk=pk)
    return render(request, 'core/referral_code_detail.html', {'referral_code_item': referral_code_item})

@login_required
def create_referral_code(request):
    if request.method == 'POST':
        form = ReferralCodeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('referral_code_list')
    else:
        form = ReferralCodeForm()
    return render(request, 'core/referral_code_create.html', {'form': form})

@login_required
def update_referral_code(request, pk):
    referral_code_item = get_object_or_404(ReferralCode, pk=pk)
    if request.method == 'POST':
        form = ReferralCodeForm(request.POST, instance=referral_code_item)
        if form.is_valid():
            form.save()
            return redirect('referral_code_detail', pk=referral_code_item.pk)
    else:
        form = ReferralCodeForm(instance=referral_code_item)
    return render(request, 'core/referral_code_update.html', {'form': form})

@login_required
def delete_referral_code(request, pk):
    referral_code_item = get_object_or_404(ReferralCode, pk=pk)
    if request.method == 'POST':
        referral_code_item.delete()
        return redirect('referral_code_list')
    return render(request, 'core/referral_code_delete.html', {'referral_code_item': referral_code_item})
