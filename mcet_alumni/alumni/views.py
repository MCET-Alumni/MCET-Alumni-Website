from django.shortcuts import render

from .models import Alumni
from .forms import DepartmentBatchForm

# Create your views here.
def alumni(request):
    if request.method=='POST':
        form = DepartmentBatchForm(request.POST)
        context = {'form':form}
        if form.is_valid():
            dept_name = form.cleaned_data['dept_name']
            batch = form.cleaned_data['batch']
            querset = Alumni.objects.filter(department = dept_name, batch=batch)
            alumunis= []
            for alumni in querset:
                tmp= {}
                tmp['name'] = alumni.first_name + ' ' + alumni.last_name
                tmp['batch'] = alumni.batch
                tmp['department'] = alumni.department
                if alumni.profile_pic:
                    tmp['photo'] = alumni.profile_pic.url
                else:
                    tmp['photo'] = '/media/profile_pics/default.jpg'
                tmp['linked_url'] = alumni.linked_url
                alumunis.append(tmp)
            context['alumunis'] = alumunis
        return render(request, 'alumni/alumni.html', context)
    else:
        form = DepartmentBatchForm()
        msg = "Please select department and batch."
        return render(request, 'alumni/alumni.html', {'form':form, 'msg':msg})

def alumni_speaks(request):
    return render(request, 'alumni/alumuni_speaks.html')

def register(request):
    return render(request, 'alumni/register.html')
