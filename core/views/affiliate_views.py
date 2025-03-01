from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..models.affiliate import Affiliate
from ..forms import AffiliateForm
from django.contrib.auth.decorators import login_required

@login_required
def affiliate_list(request):
    affiliate_items = Affiliate.objects.all()
    return render(request, 'core/affiliate_list.html', {'affiliate_items': affiliate_items})

@login_required
def affiliate_detail(request, pk):
    affiliate_item = get_object_or_404(Affiliate, pk=pk)
    return render(request, 'core/affiliate_detail.html', {'affiliate_item': affiliate_item})

@login_required
def create_affiliate(request):
    if request.method == 'POST':
        form = AffiliateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('affiliate_list')
    else:
        form = AffiliateForm()
    return render(request, 'core/affiliate_create.html', {'form': form})

@login_required
def update_affiliate(request, pk):
    affiliate_item = get_object_or_404(Affiliate, pk=pk)
    if request.method == 'POST':
        form = AffiliateForm(request.POST, instance=affiliate_item)
        if form.is_valid():
            form.save()
            return redirect('affiliate_detail', pk=affiliate_item.pk)
    else:
        form = AffiliateForm(instance=affiliate_item)
    return render(request, 'core/affiliate_update.html', {'form': form})

@login_required
def delete_affiliate(request, pk):
    affiliate_item = get_object_or_404(Affiliate, pk=pk)
    if request.method == 'POST':
        affiliate_item.delete()
        return redirect('affiliate_list')
    return render(request, 'core/affiliate_delete.html', {'affiliate_item': affiliate_item})
