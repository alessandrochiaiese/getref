from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..models.conversion import Conversion
from ..forms import ConversionForm
from django.contrib.auth.decorators import login_required

@login_required
def conversion_list(request):
    conversion_items = Conversion.objects.all()
    return render(request, 'core/conversion_list.html', {'conversion_items': conversion_items})

@login_required
def conversion_detail(request, pk):
    conversion_item = get_object_or_404(Conversion, pk=pk)
    return render(request, 'core/conversion_detail.html', {'conversion_item': conversion_item})

@login_required
def create_conversion(request):
    if request.method == 'POST':
        form = ConversionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('conversion_list')
    else:
        form = ConversionForm()
    return render(request, 'core/conversion_create.html', {'form': form})

@login_required
def update_conversion(request, pk):
    conversion_item = get_object_or_404(Conversion, pk=pk)
    if request.method == 'POST':
        form = ConversionForm(request.POST, instance=conversion_item)
        if form.is_valid():
            form.save()
            return redirect('conversion_detail', pk=conversion_item.pk)
    else:
        form = ConversionForm(instance=conversion_item)
    return render(request, 'core/conversion_update.html', {'form': form})

@login_required
def delete_conversion(request, pk):
    conversion_item = get_object_or_404(Conversion, pk=pk)
    if request.method == 'POST':
        conversion_item.delete()
        return redirect('conversion_list')
    return render(request, 'core/conversion_delete.html', {'conversion_item': conversion_item})
