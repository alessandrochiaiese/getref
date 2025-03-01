from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..models.transaction import Transaction
from ..forms import TransactionForm
from django.contrib.auth.decorators import login_required

@login_required
def transaction_list(request):
    transaction_items = Transaction.objects.all()
    return render(request, 'core/transaction_list.html', {'transaction_items': transaction_items})

@login_required
def transaction_detail(request, pk):
    transaction_item = get_object_or_404(Transaction, pk=pk)
    return render(request, 'core/transaction_detail.html', {'transaction_item': transaction_item})

@login_required
def create_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'core/transaction_create.html', {'form': form})

@login_required
def update_transaction(request, pk):
    transaction_item = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction_item)
        if form.is_valid():
            form.save()
            return redirect('transaction_detail', pk=transaction_item.pk)
    else:
        form = TransactionForm(instance=transaction_item)
    return render(request, 'core/transaction_update.html', {'form': form})

@login_required
def delete_transaction(request, pk):
    transaction_item = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction_item.delete()
        return redirect('transaction_list')
    return render(request, 'core/transaction_delete.html', {'transaction_item': transaction_item})
