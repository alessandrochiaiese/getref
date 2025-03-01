from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..models.bonus import Bonus
from ..forms import BonusForm
from django.contrib.auth.decorators import login_required

@login_required
def bonus_list(request):
    bonus_items = Bonus.objects.all()
    return render(request, 'core/bonus_list.html', {'bonus_items': bonus_items})

@login_required
def bonus_detail(request, pk):
    bonus_item = get_object_or_404(Bonus, pk=pk)
    return render(request, 'core/bonus_detail.html', {'bonus_item': bonus_item})

@login_required
def create_bonus(request):
    if request.method == 'POST':
        form = BonusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bonus_list')
    else:
        form = BonusForm()
    return render(request, 'core/bonus_create.html', {'form': form})

@login_required
def update_bonus(request, pk):
    bonus_item = get_object_or_404(Bonus, pk=pk)
    if request.method == 'POST':
        form = BonusForm(request.POST, instance=bonus_item)
        if form.is_valid():
            form.save()
            return redirect('bonus_detail', pk=bonus_item.pk)
    else:
        form = BonusForm(instance=bonus_item)
    return render(request, 'core/bonus_update.html', {'form': form})

@login_required
def delete_bonus(request, pk):
    bonus_item = get_object_or_404(Bonus, pk=pk)
    if request.method == 'POST':
        bonus_item.delete()
        return redirect('bonus_list')
    return render(request, 'core/bonus_delete.html', {'bonus_item': bonus_item})
