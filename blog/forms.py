from django import forms
from .models import blogPost

class blogPostForm(forms.Form):
  title = forms.CharField(max_length=35)
  slug  = forms.SlugField()
  content = forms.CharField(max_length=100, required=True)


class BlogPostModelForm(forms.ModelForm):
  class Meta:
    model = blogPost
    fields = ['title', 'slug', 'content']

  def clean_title(self, *args, **kwargs):
    instance = self.instance
    title = self.cleaned_data.get('title')
    qs = blogPost.objects.filter(title__iexact=title)
    if instance is not None:
      qs = qs.exclude(pk=instance.pk) # id=instance.id
    if qs.exists():
      raise forms.ValidationError("This title has already been used. Please try again.")
    return title