from django.db.models import query,Q
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView,CreateView, DetailView,UpdateView,DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here
from .models import Post
import operator
from django.urls import reverse_lazy
from django.contrib.staticfiles.views import serve

def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)
def search(request):
    template = 'blog/home.html'
    query = request.GET.get('q')
    result = Post.objects.filter(Q(title__icontains = query) | Q(author__username__icontains=query) | Q(content__icontains=query))
    paginate_by = 3
    context = {'posts':result}
    return render(request,template,context)

def getfile(request):
   return serve(request, 'File')

class PostListView(ListView):                       #list the all posts
    model = Post
    template_name = 'blog/home.html'            #define template name
    context_object_name = 'posts'
    print(context_object_name)
    ordering = ['-date_posted']
    paginate_by = 3
    

class UserPostListView(ListView):                     #list the userposts
    model = Post
    template_name = 'blog/user_post.html'
    context_object_name='posts'
    paginate_by =3

    def get_queryset(self):
        user = get_object_or_404(User , username=self.kwargs.get('username'))
        #return posts then 
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):                           #see the individual created post details 
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin , CreateView):          #creat post     
    model =Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content' , 'file']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):      #updatepost
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'file']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):          #delete post
    model = Post
    success_url = '/'
    template_name = 'blog/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False







