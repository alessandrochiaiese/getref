from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..models.program import Program
from ..forms import ProgramForm
from django.contrib.auth.decorators import login_required

@login_required
def program_list(request):
    program_items = Program.objects.all()
    return render(request, 'core/program_list.html', {'program_items': program_items})

@login_required
def program_detail(request, pk):
    program_item = get_object_or_404(Program, pk=pk)
    return render(request, 'core/program_detail.html', {'program_item': program_item})

@login_required
def create_program(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('program_list')
    else:
        form = ProgramForm()
    return render(request, 'core/program_create.html', {'form': form})

@login_required
def update_program(request, pk):
    program_item = get_object_or_404(Program, pk=pk)
    if request.method == 'POST':
        form = ProgramForm(request.POST, instance=program_item)
        if form.is_valid():
            form.save()
            return redirect('program_detail', pk=program_item.pk)
    else:
        form = ProgramForm(instance=program_item)
    return render(request, 'core/program_update.html', {'form': form})

@login_required
def delete_program(request, pk):
    program_item = get_object_or_404(Program, pk=pk)
    if request.method == 'POST':
        program_item.delete()
        return redirect('program_list')
    return render(request, 'core/program_delete.html', {'program_item': program_item})
