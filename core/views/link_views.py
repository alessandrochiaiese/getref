from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..models.link import Link
from ..forms import LinkForm
from django.contrib.auth.decorators import login_required

@login_required
def link_list(request):
    link_items = Link.objects.all()
    return render(request, 'core/link_list.html', {'link_items': link_items})

@login_required
def link_detail(request, pk):
    link_item = get_object_or_404(Link, pk=pk)
    return render(request, 'core/link_detail.html', {'link_item': link_item})

@login_required
def create_link(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('link_list')
    else:
        form = LinkForm()
    return render(request, 'core/link_create.html', {'form': form})

@login_required
def update_link(request, pk):
    link_item = get_object_or_404(Link, pk=pk)
    if request.method == 'POST':
        form = LinkForm(request.POST, instance=link_item)
        if form.is_valid():
            form.save()
            return redirect('link_detail', pk=link_item.pk)
    else:
        form = LinkForm(instance=link_item)
    return render(request, 'core/link_update.html', {'form': form})

@login_required
def delete_link(request, pk):
    link_item = get_object_or_404(Link, pk=pk)
    if request.method == 'POST':
        link_item.delete()
        return redirect('link_list')
    return render(request, 'core/link_delete.html', {'link_item': link_item})
