'''
run server:
python prototypes.py runserver
'''

import os
import sys
from django.conf import settings

BASE_DIR = os.path.dirname(__file__)

settings.configure(
    DEBUG=True,
    SECRET_KEY='b0mqvak1p2sqm6p#+8o8fyxf+ox(le)8&jh_5^sxa!=7!+wxj0',
    ROOT_URLCONF='sitebuilder.urls',
    MIDDLEWARE_CLASSES=(),
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
        'sitebuilder',
    ),
    STATIC_URL='/static/',
    SITE_PAGES_DIRECTORY=os.path.join(BASE_DIR, 'pages'),
    SITE_OUTPUT_DIRECTORY=os.path.join(BASE_DIR, '_build'),
    STATIC_ROOT=os.path.join(BASE_DIR, '_build', 'static'),
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(os.path.join(BASE_DIR, 'sitebuilder'), 'templates')],
            # 'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
)

if __name__ == '__main__':
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
