import logging

AUTHOR = "Pelican Contributors"
SITENAME = "Pelican Development Blog"
SITEURL = ""

PATH = "content"

CACHE_CONTENT = False
LOAD_CONTENT_CACHE = False

TIMEZONE = 'Europe/Rome'

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
