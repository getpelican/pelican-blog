#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Pelican Contributors"
SITENAME = u"Pelican Development Blog"
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'
LOCALE = 'en_US.UTF-8'

MENUITEMS = (('documentation', 'https://docs.getpelican.com'),
             ('contribute', 'https://donate.getpelican.com'),
             ('gratitude', '/pages/gratitude.html'),
            )
DISPLAY_PAGES_ON_MENU = False

# Blogroll
SOCIAL_WIDGET_NAME = "follow"
LINKS = (('Pelican Docs', 'https://docs.getpelican.com/'),
         ('Support Pelican', 'https://donate.getpelican.com/'),
         ('Justin Mayer', 'https://justinmayer.com/'))

SOCIAL = (('@getpelican', 'https://twitter.com/getpelican'),
          ('@jmayer', 'https://twitter.com/jmayer'),
          ('github', 'https://github.com/getpelican'),
         )

DEFAULT_PAGINATION = 5
