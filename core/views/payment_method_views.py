from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..models.payment_method import PaymentMethod
from ..forms import PaymentMethodForm
from django.contrib.auth.decorators import login_required

@login_required
def payment_method_list(request):
    payment_method_items = PaymentMethod.objects.all()
    return render(request, 'core/payment_method_list.html', {'payment_method_items': payment_method_items})

@login_required
def payment_method_detail(request, pk):
    payment_method_item = get_object_or_404(PaymentMethod, pk=pk)
    return render(request, 'core/payment_method_detail.html', {'payment_method_item': payment_method_item})

@login_required
def create_payment_method(request):
    if request.method == 'POST':
        form = PaymentMethodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_method_list')
    else:
        form = PaymentMethodForm()
    return render(request, 'core/payment_method_create.html', {'form': form})

@login_required
def update_payment_method(request, pk):
    payment_method_item = get_object_or_404(PaymentMethod, pk=pk)
    if request.method == 'POST':
        form = PaymentMethodForm(request.POST, instance=payment_method_item)
        if form.is_valid():
            form.save()
            return redirect('payment_method_detail', pk=payment_method_item.pk)
    else:
        form = PaymentMethodForm(instance=payment_method_item)
    return render(request, 'core/payment_method_update.html', {'form': form})

@login_required
def delete_payment_method(request, pk):
    payment_method_item = get_object_or_404(PaymentMethod, pk=pk)
    if request.method == 'POST':
        payment_method_item.delete()
        return redirect('payment_method_list')
    return render(request, 'core/payment_method_delete.html', {'payment_method_item': payment_method_item})
