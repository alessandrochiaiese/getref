from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..models.support_ticket import SupportTicket
from ..forms import SupportTicketForm
from django.contrib.auth.decorators import login_required

@login_required
def support_ticket_list(request):
    support_ticket_items = SupportTicket.objects.all()
    return render(request, 'core/support_ticket_list.html', {'support_ticket_items': support_ticket_items})

@login_required
def support_ticket_detail(request, pk):
    support_ticket_item = get_object_or_404(SupportTicket, pk=pk)
    return render(request, 'core/support_ticket_detail.html', {'support_ticket_item': support_ticket_item})

@login_required
def create_support_ticket(request):
    if request.method == 'POST':
        form = SupportTicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('support_ticket_list')
    else:
        form = SupportTicketForm()
    return render(request, 'core/support_ticket_create.html', {'form': form})

@login_required
def update_support_ticket(request, pk):
    support_ticket_item = get_object_or_404(SupportTicket, pk=pk)
    if request.method == 'POST':
        form = SupportTicketForm(request.POST, instance=support_ticket_item)
        if form.is_valid():
            form.save()
            return redirect('support_ticket_detail', pk=support_ticket_item.pk)
    else:
        form = SupportTicketForm(instance=support_ticket_item)
    return render(request, 'core/support_ticket_update.html', {'form': form})

@login_required
def delete_support_ticket(request, pk):
    support_ticket_item = get_object_or_404(SupportTicket, pk=pk)
    if request.method == 'POST':
        support_ticket_item.delete()
        return redirect('support_ticket_list')
    return render(request, 'core/support_ticket_delete.html', {'support_ticket_item': support_ticket_item})
