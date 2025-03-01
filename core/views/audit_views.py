from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..models.audit import Audit
from ..forms import AuditForm
from django.contrib.auth.decorators import login_required

@login_required
def audit_list(request):
    audit_items = Audit.objects.all()
    return render(request, 'core/audit_list.html', {'audit_items': audit_items})

@login_required
def audit_detail(request, pk):
    audit_item = get_object_or_404(Audit, pk=pk)
    return render(request, 'core/audit_detail.html', {'audit_item': audit_item})

@login_required
def create_audit(request):
    if request.method == 'POST':
        form = AuditForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('audit_list')
    else:
        form = AuditForm()
    return render(request, 'core/audit_create.html', {'form': form})

@login_required
def update_audit(request, pk):
    audit_item = get_object_or_404(Audit, pk=pk)
    if request.method == 'POST':
        form = AuditForm(request.POST, instance=audit_item)
        if form.is_valid():
            form.save()
            return redirect('audit_detail', pk=audit_item.pk)
    else:
        form = AuditForm(instance=audit_item)
    return render(request, 'core/audit_update.html', {'form': form})

@login_required
def delete_audit(request, pk):
    audit_item = get_object_or_404(Audit, pk=pk)
    if request.method == 'POST':
        audit_item.delete()
        return redirect('audit_list')
    return render(request, 'core/audit_delete.html', {'audit_item': audit_item})
