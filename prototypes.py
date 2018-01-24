import sys

from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY='hard to guess',
    ROOT_URLCONF='sitebuilder.urls',
    MIDDLEWARE_CLASSES=(),
    INSTALL_APPS=(
        'django.contrib.staticfiles',
        'sitebuilder',
    ),
    TEMPLATE=(
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIR': [],
            'APP_DIRS': True,
        },
    ),
    STATIC_URL='/static/',
)

if __name__  == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
    