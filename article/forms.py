from django.forms import ModelForm
from . models import Articles


class ArticlesFroms(ModelForm):
	class Meta:
		model = Articles
		fields =  '__all__'

	def clean(self):
		cleaned_data  = self.cleaned_data
		print("all cleaned Data", cleaned_data)
		return cleaned_data

	def clean(self):
		data = self.cleaned_data
		title = data.get("title")
		qs = Articles.objects.filter(title__icontains=title)
		return data
