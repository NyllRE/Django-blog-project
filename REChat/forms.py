from django import forms

class contactForm(forms.Form):
  full_name = forms.CharField()
  email    = forms.EmailField()
  content  = forms.CharField(widget=forms.Textarea)

  def clean_email(self, *args, **kwargs):
    full_name = self.cleaned_data.get('full_name')
    #                               title - title__iexact
    qs = contactForm.objects.filter(title__iexact=title)
    print(full_name)
    if qs.exists():
      raise forms.ValidationError('this name is taken')
    return full_name


# this is watasamya from hotomasyam tecnology constitutian and this is racist