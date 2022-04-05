from django import forms

sem_choices = [ (ele, ele) for ele in range(2002, 2022)]

class DepartmentBatchForm(forms.Form):

    ''' Form to get department and batch.'''

    department_choices = (
    ('cse', 'Computer Science and Engineering'),
    ('ece', 'Electrics and communication Engineering'),
    ('ce', 'Civil Engineering'),
    ('ee', 'Electrical Engineering'),
    ('it', 'Information Technology')
    )
    dept_name = forms.ChoiceField(
        widget=forms.Select(attrs={'class':'form-control font-100','id':'dept_name', 'placeholder':'Choose Department'}),
        choices=department_choices, 
        required=False
        )
    batch = forms.ChoiceField(
        widget=forms.Select(attrs={'class':'form-control font-100','id':'semester', 'placeholder':'Choose Semester'}), 
        choices=sem_choices, 
        required=False
        )

class BatchForm(forms.Form):
    ''' Form to get batch '''
    batch = forms.ChoiceField(
        widget=forms.Select(attrs={'class':'form-control font-100','id':'semester', 'placeholder':'Choose Semester'}), 
        choices=sem_choices, 
        required=False
        )