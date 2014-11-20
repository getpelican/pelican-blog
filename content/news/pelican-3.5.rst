Pelican 3.5 released
####################

:date: 2014-11-20
:slug: pelican-3.5-released

Today we are pleased to announce the release of Pelican 3.5. Highlights of the
improvements contained in this release follow below.

For those who are new to Pelican, please refer to the `Quickstart Guide
<http://docs.getpelican.com/en/3.5.0/quickstart.html>`_. There is also a
`Tutorials <https://github.com/getpelican/pelican/wiki/Tutorials>`_ page
available, which currently includes a link to a Pelican installation
screencast.

Highlights
==========

* Introduce ``ARTICLE_ORDER_BY`` and ``PAGE_ORDER_BY`` settings to control the
  order of articles and pages.
* Include time zone information in dates rendered in templates.
* Expose the reader name in the metadata for articles and pages.
* Allow storing static files in the same directory as content source files,
  without causing the raw content sources to be published.
* Introduce the ``{attach}`` internal link syntax for placing a static file in
  the same output directory as the document that links to it.
* Prevent Pelican from raising an exception when there are duplicate pieces of
  metadata in a Markdown file.
* Introduce the ``TYPOGRIFY_IGNORE_TAGS`` setting to add HTML tags to be ignored
  by Typogrify.
* Add the ability to use ``-`` in date formats to strip leading zeros. For
  example, ``%-d/%-m/%y`` will now result in the date ``9/8/12``.
* Ensure feed generation is correctly disabled during quickstart configuration.
* Fix ``PAGE_EXCLUDES`` and ``ARTICLE_EXCLUDES`` from incorrectly matching
  sub-directories.
* Introduce ``STATIC_EXCLUDE`` setting to add static file excludes.
* Fix an issue when using ``PAGINATION_PATTERNS`` while ``RELATIVE_URLS``
  is enabled.
* Fix feed generation causing links to use the wrong language for month
  names when using other locales.
* Fix an issue where the authors list in the simple template wasn't correctly
  formatted.
* Fix an issue when parsing non-string URLs from settings.
* Improve consistency of debug and warning messages.

For a full list of changes, see: https://github.com/getpelican/pelican/compare/3.4.0...3.5.0

Upgrading from previous releases
================================

While we do everything we can to maximize backwards compatibility and ensure
smooth Pelican upgrades, it's possible that you may encounter un-anticipated
wrinkles. If you run into problems, please reach out via the #pelican channel
on IRC, and we will update this post with any upgrade tips contributed by the
Pelican community.
