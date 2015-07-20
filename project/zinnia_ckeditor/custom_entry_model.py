"""
Must not be in models.py to avoid a clash with zinnia models
"""
from django.utils.translation import ugettext_lazy as _

from zinnia.models_bases.entry import AbstractEntry

from ckeditor.fields import RichTextField

class EntryWithCkeditor(AbstractEntry):
    class Meta(AbstractEntry.Meta):
        abstract = True
