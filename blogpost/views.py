import markdown
from django.shortcuts import render, get_object_or_404
from .models import Blog, Category, Tag
from comments.forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    posts = Blog.objects.all().order_by('-created')

    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.paginator(paginator.num_pages)

    return render(request, 'blogpost/index.html', {'post_list': post_list})

def detail(request, id):
    post = get_object_or_404(Blog, pk=id)

    post.increase_views()

    post.content = markdown.markdown(post.content, extensions=['markdown.extensions.extra',
                                                               'markdown.extensions.codehilite',
                                                               'markdown.extensions.toc',
                                                               ])

    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }

    return render(request, 'blogpost/detail.html', context=context)

def archives(request, year, month):
    posts = Blog.objects.filter(created__year = year,
                        created__month = month).order_by('-created')

    return render(request, 'blogpost/archives.html', {'posts': posts})

def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    posts = Blog.objects.filter(category=cate).order_by('-created')

    return render(request, 'blogpost/category.html', {'posts': posts})

def tags(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    posts = Blog.objects.filter(tags=tag).order_by('-created')

    return render(request, 'blogpost/tags.html', {'posts': posts})

def search(request):
    # s为表单输入的参数
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request, 'blogpost/index.html')
        else:
            post_list = Blog.objects.filter(title__icontains = s)
            if len(post_list) == 0:
                return render(request, 'blogpost/search.html', {'post_list': post_list,
                                                       'error': True})
            else:
                return render(request, 'blogpost/search.html', {'post_list': post_list,
                                                       'error': False})
    return redirect('/')