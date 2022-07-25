import logging

AUTHOR = "Pelican Contributors"
SITENAME = "Pelican – A Python Static Site Generator"
SITEURL = ""

PATH = "content"

THEME = "themes/getpelican"

CACHE_CONTENT = False
LOAD_CONTENT_CACHE = False

TIMEZONE = "Europe/Rome"

DEFAULT_LANG = "en"
LOCALE = "en_US.UTF-8"

TEMPLATE_PAGES = {"homepage.html": "index.html"}

MENUITEMS = (
    ("documentation", "https://docs.getpelican.com"),
    ("contribute", "https://donate.getpelican.com"),
    ("gratitude", "/pages/gratitude.html"),
)
DISPLAY_PAGES_ON_MENU = False

# Blogroll
SOCIAL_WIDGET_NAME = "follow"
LINKS = (
    ("Pelican Docs", "https://docs.getpelican.com/"),
    ("Support Pelican", "https://donate.getpelican.com/"),
    ("Justin Mayer", "https://justinmayer.com/"),
)

SOCIAL = (
    ("@getpelican", "https://twitter.com/getpelican"),
    ("@jmayer", "https://twitter.com/jmayer"),
    ("github", "https://github.com/getpelican"),
)

DEFAULT_PAGINATION = 5

STATIC_PATHS = [
    "images",
    "extra",
]

EXTRA_PATH_METADATA = {
    "extra/apple-touch-icon.png": {"path": "apple-touch-icon.png"},
    "extra/apple-touch-icon-57x57.png": {"path": "apple-touch-icon-57x57.png"},
    "extra/apple-touch-icon-72x72.png": {"path": "apple-touch-icon-72x72.png"},
    "extra/apple-touch-icon-76x76.png": {"path": "apple-touch-icon-76x76.png"},
    "extra/apple-touch-icon-114x114.png": {"path": "apple-touch-icon-114x114.png"},
    "extra/apple-touch-icon-120x120.png": {"path": "apple-touch-icon-120x120.png"},
    "extra/apple-touch-icon-144x144.png": {"path": "apple-touch-icon-144x144.png"},
    "extra/apple-touch-icon-152x152.png": {"path": "apple-touch-icon-152x152.png"},
    "extra/apple-touch-icon-180x180.png": {"path": "apple-touch-icon-180x180.png"},
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/robots.txt": {"path": "robots.txt"},
}

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.admonition": {},
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {},
    },
    "output_format": "html5",
}

TAILWIND = {
    "version": "3.0.0",
    "plugins": [
        "@tailwindcss/typography",
        "@tailwindcss/line-clamp",
    ],
}

INDEX_SAVE_AS = "blog/index.html"
PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}/index.html"
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
ARTICLE_URL = 'blog/{slug}'
CATEGORIES_URL = 'blog/categories/'
CATEGORIES_SAVE_AS = 'blog/categories/index.html'
CATEGORY_URL = 'blog/category/{slug}/index.html'
CATEGORY_SAVE_AS = 'blog/category/{slug}/index.html'
TAGS_URL = 'blog/tags/'
TAGS_SAVE_AS = 'blog/tags/index.html'
TAG_URL = 'blog/tag/{slug}/index.html'
TAG_SAVE_AS = 'blog/tag/{slug}/index.html'
