from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..models.participant import Participant
from ..forms import ParticipantForm
from django.contrib.auth.decorators import login_required

@login_required
def participant_list(request):
    participant_items = Participant.objects.all()
    return render(request, 'core/participant_list.html', {'participant_items': participant_items})

@login_required
def participant_detail(request, pk):
    participant_item = get_object_or_404(Participant, pk=pk)
    return render(request, 'core/participant_detail.html', {'participant_item': participant_item})

@login_required
def create_participant(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('participant_list')
    else:
        form = ParticipantForm()
    return render(request, 'core/participant_create.html', {'form': form})

@login_required
def update_participant(request, pk):
    participant_item = get_object_or_404(Participant, pk=pk)
    if request.method == 'POST':
        form = ParticipantForm(request.POST, instance=participant_item)
        if form.is_valid():
            form.save()
            return redirect('participant_detail', pk=participant_item.pk)
    else:
        form = ParticipantForm(instance=participant_item)
    return render(request, 'core/participant_update.html', {'form': form})

@login_required
def delete_participant(request, pk):
    participant_item = get_object_or_404(Participant, pk=pk)
    if request.method == 'POST':
        participant_item.delete()
        return redirect('participant_list')
    return render(request, 'core/participant_delete.html', {'participant_item': participant_item})
