#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Matthew Lapworth'
SITENAME = 'Dragonn Development'
SITEURL = 'https://dragonndev.github.io'

THEME = '/Users/matthew/Documents/projects/python/pelican-themes/bootstrap'

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'America/Los_Angeles'
DEFAULT_DATE_FORMAT = '%Y/%m/%d'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/dragonndev'),
          ('Keybase', 'https://keybase.io/dragonndev'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True