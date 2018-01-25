import os
import sys


from django.conf import settings

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
settings.configure(
    DEBUG=True,
    SECRET_KEY='hard to guess',
    ROOT_URLCONF='sitebuilder.urls',
    ALLOWED_HOSTS=['0.0.0.0'],
    MIDDLEWARE_CLASSES=(),
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
        'sitebuilder',
    ),
    TEMPLATES=(
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'sitebuilder', 'template'),],
            'APP_DIRS': True,
        },
    ),
    SITE_PAGES_DIRECTORY=os.path.join(BASE_DIR, 'pages'),
    STATIC_URL='/static/',
)

if __name__  == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)