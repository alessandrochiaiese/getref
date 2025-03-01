from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..models.campaign import Campaign
from ..forms import CampaignForm
from django.contrib.auth.decorators import login_required

@login_required
def campaign_list(request):
    campaign_items = Campaign.objects.all()
    return render(request, 'core/campaign_list.html', {'campaign_items': campaign_items})

@login_required
def campaign_detail(request, pk):
    campaign_item = get_object_or_404(Campaign, pk=pk)
    return render(request, 'core/campaign_detail.html', {'campaign_item': campaign_item})

@login_required
def create_campaign(request):
    if request.method == 'POST':
        form = CampaignForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('campaign_list')
    else:
        form = CampaignForm()
    return render(request, 'core/campaign_create.html', {'form': form})

@login_required
def update_campaign(request, pk):
    campaign_item = get_object_or_404(Campaign, pk=pk)
    if request.method == 'POST':
        form = CampaignForm(request.POST, instance=campaign_item)
        if form.is_valid():
            form.save()
            return redirect('campaign_detail', pk=campaign_item.pk)
    else:
        form = CampaignForm(instance=campaign_item)
    return render(request, 'core/campaign_update.html', {'form': form})

@login_required
def delete_campaign(request, pk):
    campaign_item = get_object_or_404(Campaign, pk=pk)
    if request.method == 'POST':
        campaign_item.delete()
        return redirect('campaign_list')
    return render(request, 'core/campaign_delete.html', {'campaign_item': campaign_item})
