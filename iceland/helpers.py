import re
from .models import NgramShort, NgramFull, Sentence, Word
from django.db.models import Count


class ConstructionHelper:
    def __init__(self, full_ngrams):
        self.full_ngrams = full_ngrams

    def clean_text_(self, text_bit, phrase):
        text_bit = re.sub('[a-záæéíóöúýþð]( ([.!?,:"»;]))', r'\2', text_bit)
        text_bit = re.sub(' »', '»', text_bit)
        text_bit = re.sub('« ', '«', text_bit)
        text_bit = re.sub(phrase, '<span class="construction-occurence">%s</span>' % phrase, text_bit)

        return text_bit

    def collect_examples(self):
        examples = []

        for f in self.full_ngrams:
            quote_sentences = Sentence.objects.filter(text__id=f.text_id, sent_idx__gte=f.sentence_id-2,\
                                                                          sent_idx__lte=f.sentence_id+2)
            quote_words = Word.objects.filter(sentence__in=quote_sentences)

            sentence = Sentence.objects.get(text__id=f.text_id, sent_idx=f.sentence_id)
            phrase = Word.objects.filter(sentence=sentence, word_idx__gte=f.word_start, word_idx__lte=f.word_end)

            phrase = ' '.join([word.form for word in phrase])
            text_bit = ' '.join([word.form for word in quote_words])
            text_bit = self.clean_text_(text_bit, phrase)

            examples.append((f.full_text, text_bit))

        return examples

    def calculate_numbers(self):
        corpus_freq = len(self.full_ngrams)

        vars_num = self.full_ngrams.values('full_text').distinct().count()
        texts_num = self.full_ngrams.values('text').distinct().count()

        variants_counter = self.full_ngrams.values('full_text').annotate(variants_num=Count('full_text'))
        variants_counter = [(v['full_text'], v['variants_num']) for v in variants_counter]

        return corpus_freq, vars_num, texts_num, variants_counter