import re
from django.views.generic import TemplateView, DetailView
from django.views.generic.list import ListView
from .models import NgramShort, NgramFull, Letter, Word, Sentence
from django.db.models import Count


class IndexView(TemplateView):
    template_name = 'iceland/index.html'


class ConstructionListView(ListView):
    template_name = 'iceland/formulas.html'
    model = NgramShort

    def get_context_data(self, **kwargs):
        alphabet = Letter.objects.all().order_by('letter')

        context = super().get_context_data(**kwargs)
        context['alphabet'] = alphabet
        
        return context

    def get_queryset(self):
        data = self.request.GET

        if 'filter' not in data:
        	#временная небольшая выдача для теста
        	queryset = NgramShort.objects.filter(letter_id=1).order_by('short_text')[:20]
        else:
        	queryset = NgramShort.objects.filter(letter_id=1).order_by('short_text')[:20]

        	#work in progress
        	#full_ngrams = NgramFull.objects.filter(short_ngram__in=queryset)


        return queryset

       

class ConstructionDetailView(DetailView):
    model = NgramShort
    template_name = 'iceland/construction.html'
    context_object_name = 'construction'

    def get_context_data(self, **kwargs):
        full_ngrams = NgramFull.objects.filter(short_ngram=self.object)

        examples = []

        for f in full_ngrams:
            quote_sentences = Sentence.objects.filter(text__id=f.text_id, sent_idx__gte=f.sentence_id-2, sent_idx__lte=f.sentence_id+2)
            quote_words = Word.objects.filter(sentence__in=quote_sentences)

            sentence = Sentence.objects.get(text__id=f.text_id, sent_idx=f.sentence_id)
            phrase = Word.objects.filter(sentence=sentence, word_idx__gte=f.word_start, word_idx__lte=f.word_end)

            phrase = ' '.join([word.form for word in phrase])
            text_bit = ' '.join([word.form for word in quote_words])
            text_bit = re.sub('[a-záæéíóöúýþð]( ([.!?,:"»;]))', r'\2', text_bit)
            text_bit = re.sub(' »', '»', text_bit)
            text_bit = re.sub('« ', '«', text_bit)
            text_bit = re.sub(phrase, '<span class="construction-occurence">%s</span>' % phrase, text_bit)

            examples.append((f.full_text, text_bit))

        corpus_freq = len(full_ngrams)
        vars_num = full_ngrams.values('full_text').distinct().count()
        texts_num = full_ngrams.values('text').distinct().count()

        variants_counter = full_ngrams.values('full_text').annotate(variants_num=Count('full_text'))
        variants_counter = [(v['full_text'], v['variants_num']) for v in variants_counter]

        context = super().get_context_data(**kwargs)
        context['examples'] = examples
        context['corpus_freq'] = corpus_freq
        context['vars_num'] = vars_num
        context['texts_num'] = texts_num
        context['variants_counter'] = variants_counter

        return context