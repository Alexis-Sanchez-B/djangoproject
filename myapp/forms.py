from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200)
    descripcion = forms.CharField(label="Descripcion de la tarea",widget=forms.Textarea)