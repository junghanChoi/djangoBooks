from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.views.generic.dates import ArchiveIndexView
from django.views.generic.dates import YearArchiveView
from django.views.generic.dates import MonthArchiveView
from django.views.generic.dates import DayArchiveView
from django.views.generic.dates import TodayArchiveView


from blog.models import Post
from tagging.models import Tag, TaggedItem
from tagging.views import TaggedObjectList

from django.views.generic.edit import FormView
from blog.forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render
# Create your views here.

#--- ListView
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2

#--- DetailView
class PostDV(DetailView):
    model = Post

#--- ArchiveView
class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_date'

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_date'
    make_object_list = True

class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_date'

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_date'

class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_date'

class TagTV(TemplateView):
    template_name = 'tagging/tagging_cloud.html'

class PostTOL(TaggedObjectList):
    model = Post
    template_name = 'tagging/tagging_post_list.html'

#--- form  View
class  SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        schWord = '%s' % self.request.POST['search_word']
        post_list = Post.objects.filter(Q(title__icontains=schWord)|
                Q(description__icontains=schWord) | Q(content__icontains=schWord)).distint()
        
        context = {}
        context['form'] = form
        context['search_term'] = schWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)
