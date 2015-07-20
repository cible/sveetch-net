# -*- coding: utf-8 -*-
"""
Map your sveedocuments urls
"""
from sveedocuments.views.page import (HelpPageView, PageIndexView, PageDetailsView, 
                                    PageSourceView)

urlpatterns += patterns('',
    (r'^board/', include('sveedocuments.urls_board')),
    
    # Mount sveedocuments public ressources
    url(r'^documents-help/$', HelpPageView.as_view(), name='documents-help'),
    url(r'^sitemap/$', PageIndexView.as_view(), name='documents-index'),
    url(r'^(?P<slug>[-\w]+)/$', PageDetailsView.as_view(), name='documents-page-details'),
    url(r'^(?P<slug>[-\w]+)/source/$', PageSourceView.as_view(), name='documents-page-source'),
)
