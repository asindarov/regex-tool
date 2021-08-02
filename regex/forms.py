from django import forms


class RegexForm(forms.Form):
	string_input = forms.CharField(widget=forms.Textarea)
	regex_input =  forms.CharField(label='Regex', max_length=200)