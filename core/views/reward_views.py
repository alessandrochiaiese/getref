from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..models.reward import Reward
from ..forms import RewardForm
from django.contrib.auth.decorators import login_required

@login_required
def reward_list(request):
    reward_items = Reward.objects.all()
    return render(request, 'core/reward_list.html', {'reward_items': reward_items})

@login_required
def reward_detail(request, pk):
    reward_item = get_object_or_404(Reward, pk=pk)
    return render(request, 'core/reward_detail.html', {'reward_item': reward_item})

@login_required
def create_reward(request):
    if request.method == 'POST':
        form = RewardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reward_list')
    else:
        form = RewardForm()
    return render(request, 'core/reward_create.html', {'form': form})

@login_required
def update_reward(request, pk):
    reward_item = get_object_or_404(Reward, pk=pk)
    if request.method == 'POST':
        form = RewardForm(request.POST, instance=reward_item)
        if form.is_valid():
            form.save()
            return redirect('reward_detail', pk=reward_item.pk)
    else:
        form = RewardForm(instance=reward_item)
    return render(request, 'core/reward_update.html', {'form': form})

@login_required
def delete_reward(request, pk):
    reward_item = get_object_or_404(Reward, pk=pk)
    if request.method == 'POST':
        reward_item.delete()
        return redirect('reward_list')
    return render(request, 'core/reward_delete.html', {'reward_item': reward_item})
