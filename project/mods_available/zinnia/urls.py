# -*- coding: utf-8 -*-
from zinnia.views.archives import EntryIndex

urlpatterns = patterns('',
    url(r'^$', EntryIndex.as_view(), name='homepage'),
    url(r'^weblog/', include('zinnia.urls', namespace="zinnia")),
    url(r'^comments/', include('django_comments.urls')),
    ) + urlpatterns
