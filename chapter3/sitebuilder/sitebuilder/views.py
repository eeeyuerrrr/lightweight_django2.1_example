import os
from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.template import Template
from django.utils._os import safe_join


def get_page_or_404(name):
    try:
        file_path = safe_join(settings.SITE_PAGES_DIRECTORY, name)
        if not os.path.exists(file_path):
            raise ValueError
        with open(file_path, 'r') as f:
            page = Template(f.read())
        return page

    except ValueError:
        raise Http404('Page Not Found')


def page(request, slug='index'):
    file_name = '{}.html'.format(slug)
    page = get_page_or_404(file_name)
    context = {
        'slug': slug,
        'page': page,
    }
    return render(request, 'page.html', context)