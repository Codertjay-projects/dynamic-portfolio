from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.base import View

from blog.forms import PostCreateForm
from blog.models import Post
from blog.utils import get_read_time
from comments.forms import CommentForm
from comments.models import Comment
from users.models import User


class BlogListView(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'HomePage/blog/blog.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        username = self.request.GET.get('username')
        post = Post.objects.all()
        if query:
            object_list = post.filter(
                Q(category__icontains=query) |
                Q(description__icontains=query) |
                Q(user__username__icontains=query) |
                Q(title__icontains=query)
            ).distinct()
        elif username:
            object_list = post.filter(user__username__icontains=username)
        else:
            object_list = Post.objects.all()
        return object_list


def blog_user_list_view(request, username=None):
    if username:
        user = get_object_or_404(User, username=username)
        if user:
            page = request.GET.get('page', 1)

            post = Post.objects.filter(user=user)
            paginator = Paginator(post, 10)
            try:
                post = paginator.page(page)
            except PageNotAnInteger:
                post = paginator.page(1)
            except EmptyPage:
                post = paginator.page(paginator.num_pages)
            return render(request, 'HomePage/blog/blog_user.html', {'post': post, 'user': user})
    else:
        return redirect('blog:blog_list')


class BlogDetailView(DetailView):
    template_name = 'HomePage/blog/blog-single.html'
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = context['object']
        """ note this instance.get_content_type is from our models where we 
        linked the comment models and the blog models with content_type and object_id """
        context['comment'] = instance.get_content_type

        print('read time :', get_read_time(instance.description))
        print('read time :', get_read_time(instance.get_markdown()))

        context['form'] = CommentForm()
        return context


class BlogCreateView(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):
        form = PostCreateForm()
        post = Post.objects.filter(user=self.request.user)
        return render(self.request, 'dashboard/blog_create.html', {'form': form, 'post': post})

    def post(self, *args, **kwargs):
        form = PostCreateForm(self.request.POST, self.request.FILES or None)
        print(self.request.POST)
        print('form:', form.errors)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = self.request.user
            instance.save()
            messages.success(self.request, 'Article was successfully created ')
            return HttpResponseRedirect(instance.get_absolute_url())

        elif not form.is_valid():
            messages.error(self.request, 'invalid form data')
        return redirect('blog:blog_create')


@login_required
def update_post_view(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    form = PostCreateForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        print(instance.read_time)
        print(instance.slug)
        print(instance.slug)
        instance.save()
        print('updating the post', request.POST, '\n', instance.user)
        messages.success(request, 'Successfully updated article')
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.warning(request, 'The form isn\'t valid')

    return render(request, 'HomePage/blog/blog_update.html', {'form': form, 'post': instance})


class DeletePostView(DeleteView):
    model = Post
    template_name = 'HomePage/blog/post_delete.html'
    success_url = '/blog/'


@login_required
def create_comment(request, slug=None):
    try:
        instance = Post.objects.get(slug=slug)
    except ObjectDoesNotExist:
        instance = None
    form = CommentForm(request.POST or None)
    print('The form data :', form)
    if form.is_valid():
        print(form.cleaned_data)
        form_data = form.save(commit=False)
        form_data.user = request.user
        form_data.content_type = instance.get_content_type
        form_data.object_id = instance.id
        form_data.parent = None
        try:
            parent_id = int(request.POST.get('parent_id'))
        except:
            parent_id = None

        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists() and parent_qs.count() == 1:
                parent_obj = parent_qs.first()
                print('parent_obj :', parent_obj)
                form_data.parent = parent_obj
        form.save()
        messages.success(request, 'form has being submitted')
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, f'{form.errors}')
    return redirect('blog:blog_detail', instance.slug)
