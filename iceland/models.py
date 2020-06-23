from django.db import models


class Clustering(models.Model):
    short_ngram = models.ForeignKey('NgramShort', on_delete=models.CASCADE, blank=True, null=True)
    pos_mask =  models.ForeignKey('PosMask', on_delete=models.CASCADE, blank=True, null=True)
    cluster = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clustering'

    def __str__(self):
        return int(self.cluster)


class NgramFull(models.Model):
    text = models.ForeignKey('Text', on_delete=models.CASCADE, blank=True, null=True)
    sentence = models.ForeignKey('Sentence', on_delete=models.CASCADE, blank=True, null=True)
    word_start = models.IntegerField(blank=True, null=True)
    word_end = models.IntegerField(blank=True, null=True)
    full_text = models.TextField(blank=True, null=True)
    short_ngram = models.ForeignKey('NgramShort', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ngram_full'

    def __str__(self):
        return self.full_text


class NgramShort(models.Model):
    short_text = models.TextField(blank=True, null=True)
    pos_mask = models.ForeignKey('PosMask', on_delete=models.CASCADE, blank=True, null=True)
    letter = models.ForeignKey('Letter', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ngram_short'

    def __str__(self):
        return self.short_text


class PosMask(models.Model):
    mask = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_mask'

    def __str__(self):
        return self.mask


class Sentence(models.Model):
    text = models.ForeignKey('Text', on_delete=models.CASCADE, blank=True, null=True)
    sent_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sentences'

    def __str__(self):
        return self.text


class Text(models.Model):
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'texts'

    def __str__(self):
        return self.name


class Word(models.Model):
    sentence = models.ForeignKey('Sentence', on_delete=models.CASCADE, blank=True, null=True)
    word_idx = models.IntegerField(blank=True, null=True)
    form = models.TextField(blank=True, null=True)
    lemma = models.TextField(blank=True, null=True)
    gram = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'words'

    def __str__(self):
        return self.lemma


class Letter(models.Model):
    letter = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'letters'

    def __str__(self):
        return self.letter
