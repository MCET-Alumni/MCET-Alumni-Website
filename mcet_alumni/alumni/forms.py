from django import forms

class DepartmentBatchForm(forms.Form):

    ''' Form to get department and batch.'''

    department_choices = (
    ('cse', 'Computer Science and Engineering'),
    ('ece', 'Electrics and communication Engineering'),
    ('ce', 'Civil Engineering'),
    ('ee', 'Electrical Engineering'),
    ('it', 'Information Technology')
    )
    sem_choices = [ (ele, ele) for ele in range(2002, 2022)]
    dept_name = forms.ChoiceField(
        widget=forms.Select(attrs={'class':'form-control','id':'dept_name', 'placeholder':'Choose Department'}),
        choices=department_choices, 
        required=False
        )
    batch = forms.ChoiceField(
        widget=forms.Select(attrs={'class':'form-control','id':'semester', 'placeholder':'Choose Semester'}), 
        choices=sem_choices, 
        required=False
        )