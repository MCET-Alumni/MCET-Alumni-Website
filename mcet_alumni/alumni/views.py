from django.shortcuts import render

from .forms import DepartmentBatchForm

# Create your views here.
def alumni(request):
    if request.method=='POST':
        form = DepartmentBatchForm(request.POST)
        context = {'form':form}
        if form.is_valid():
            dept_name = form.cleaned_data['dept_name']
            batch = form.cleaned_data['batch']
            context['members'] = [
                {'name':'Upendra Kumar', 'Batch':'1998', 'department':'CSE'},
            ]
        return render(request, 'alumni/alumni.html', context)
    else:
        form = DepartmentBatchForm()
        return render(request, 'alumni/alumni.html', {'form':form})

def notable_alumni(request):
    return render(request, 'alumni/notable_alumni.html')

def register(request):
    return render(request, 'alumni/register.html')
