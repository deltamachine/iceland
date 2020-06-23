import string
from django.db.models import Count
from django.core.paginator import InvalidPage, EmptyPage
from django.core.paginator import Paginator


class AlphabetPaginator(Paginator):
    def find_letters(self, page_index):
        objects = self.page(page_index).object_list.select_related('letter')
        letters = {}

        for i, obj in enumerate(objects):
            let = obj.letter

            if let not in letters.values():
                letters[i] = let

        return letters