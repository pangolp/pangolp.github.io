#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import datetime

AUTHOR = 'Pagani Walter'
SITENAME = 'El blog de Pango | Stevej'
SITEURL = 'https://pangolp.github.io'

PATH = 'content'

TIMEZONE = 'America/Argentina/Buenos_Aires'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'default'

MENU_ITEMS_LEFT = (
    ('AzerothCore', 'https://www.azerothcore.org/'),
    ('BlizzCMS', 'https://wow-cms.com/'),
)

DATE = datetime.datetime.now().year
