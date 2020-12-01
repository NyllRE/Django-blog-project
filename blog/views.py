from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
# Create your views here.
from .models import blogPost
from .forms import BlogPostModelForm


def blogPage(request, slug):
  # queryset = blogPost.objects.filter(slug=slug)
  # if queryset.count() == 0:
  #   raise Http404
  # obj = queryset.first()

  obj = get_object_or_404(blogPost, slug=slug)
  template_name = 'blog/Page.html'
  context = {'object': obj}
  return render(request, template_name, context)




def blog_post_list_view(request):
  # list out objects 
  # could be search
  qs = blogPost.objects.all() # queryset -> list of python object
  
  # form = BlogPostModelForm(request.POST or None)
  # if form.is_valid():
  #   obj = form.save(commit=False)
  #   obj.user = request.user
  #   obj.save()
  #   # form.save()
  #   form = BlogPostModelForm()
  #   return redirect(f'/blog/{ obj.slug }')

  template_name = 'blog/list.html'
  context = {'object_list': qs, 'title': 'blogs'}
  return render(request, template_name, context) 


@login_required
def blog_post_create_view(request):
  # creates objects
  form = BlogPostModelForm(request.POST or None)
  if form.is_valid():
    obj = form.save(commit=False)
    obj.user = request.user
    obj.save()
    # form.save()
    form = BlogPostModelForm()
    return redirect(f'/blog/{ obj.slug }')

  template_name = 'form.html'
  context = {'form': form}
  return render(request, template_name, context) 


def blog_post_detail_view(request, slug):
  # 1 object -> detail view
  obj = get_object_or_404(blogPost, slug=slug)
  template_name = 'blog/retrieve.html'
  context = {'object': obj}
  return render(request, template_name, context)

@staff_member_required
def blog_post_edit_view(request, slug):
  obj = get_object_or_404(blogPost, slug=slug)
  form = BlogPostModelForm(request.POST or None, instance=obj)
  if form.is_valid():
    form.save()
    return redirect(f'/blog/{slug}')
  template_name = 'form.html'
  context = {'form': form, 'title': f"Edit {obj.slug}"}
  return render(request, template_name, context)

@staff_member_required
def blog_post_delete_view(request, slug):
  obj = get_object_or_404(blogPost, slug=slug)
  template_name = 'blog/delete.html'
  if request.method == 'POST':
    obj.delete()
    return redirect('/blog')
  context = {'object': obj}
  return render(request, template_name, context)

