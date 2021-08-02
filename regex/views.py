from django.shortcuts import render
from .forms import RegexForm
import re
# Create your views here.


def regex_query_home_view(request):
	if request.method == 'POST':
		form = RegexForm(request.POST)
		if form.is_valid():
			
			action = request.POST.get('action')

			regex = form.cleaned_data.get('regex_input')
			string = form.cleaned_data.get('string_input')
			mapping = {
				'full' : re.fullmatch,
				'first' : re.search,
				'all' : re.findall,
			}
			matches = mapping[action](regex, string)
			if isinstance(matches, list):
				context = {'form' : form, 'match' : ','.join(matches), 'after' : True}
			else:	
				context = {'form' : form, 'match' : matches.group() if matches else None, 'after' : True}
			return render(request, 'regex/home.html', context)
	else :
		return render(request, 'regex/home.html', {'form' : RegexForm, 'after' : False})


