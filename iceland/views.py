import re
from django.views.generic import TemplateView, DetailView
from django.views.generic.list import ListView
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from .models import NgramShort, NgramFull, Letter
from .helpers import ConstructionHelper
from .custom_pagination import AlphabetPaginator


@method_decorator(require_http_methods(['GET']), name='dispatch')
class IndexView(TemplateView):
    template_name = 'iceland/index.html'


@method_decorator(require_http_methods(['GET']), name='dispatch')
class ConstructionListView(ListView):
    template_name = 'iceland/formulas.html'
    model = NgramShort

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        page_index = self.request.GET.get('page', 1)
        paginator = AlphabetPaginator(self.get_queryset(), 20)

        context['alphabet'] = Letter.objects.all().order_by('letter')
        context['paginator'] = paginator
        context['page_obj'] = paginator.page(page_index)
        context['letters'] = paginator.find_letters(page_index)
        
        return context

    def get_queryset(self):
        queryset = NgramShort.objects.all().order_by('short_text')

        return queryset
     

@method_decorator(require_http_methods(['GET']), name='dispatch')
class ConstructionDetailView(DetailView):
    model = NgramShort
    template_name = 'iceland/construction.html'
    context_object_name = 'construction'

    def get_context_data(self, **kwargs):
        full_ngrams = NgramFull.objects.filter(short_ngram=self.object)
        helper = ConstructionHelper(full_ngrams)

        examples = helper.collect_examples()
        corpus_freq, vars_num, texts_num, variants_counter = helper.calculate_numbers()

        context = super().get_context_data(**kwargs)
        context['examples'] = examples
        context['corpus_freq'] = corpus_freq
        context['vars_num'] = vars_num
        context['texts_num'] = texts_num
        context['variants_counter'] = variants_counter

        return context