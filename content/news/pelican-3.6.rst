Pelican 3.6 released
####################

:date: 2015-06-15
:slug: pelican-3.6-released

Pelican 3.6 has been released. Highlights of the improvements contained in this
release follow below.

For those who are new to Pelican, please refer to the `Quickstart Guide
<http://docs.getpelican.com/en/latest/quickstart.html>`_. There is also a
`Tutorials <https://github.com/getpelican/pelican/wiki/Tutorials>`_ page
available, which also includes a link to a Pelican installation screencast.

Highlights
==========

* Disable caching by default in order to prevent potential confusion
* Improve caching behavior, replacing ``pickle`` with ``cpickle``
* Allow Markdown or reST content in metadata fields other than ``summary``
* Support semicolon-separated author/tag lists
* Improve flexibility of article sorting
* Add ``--relative-urls`` argument
* Support devserver listening on addresses other than localhost
* Unify HTTP server handlers to ``pelican.server`` throughout
* Handle intra-site links to draft posts
* Move ``tag_cloud`` from core to plugin
* Load default theme's external resources via HTTPS
* Import drafts from WordPress XML
* Improve support for Windows users
* Enhance logging and test suite
* Clean up and refactor codebase
* New signals: ``all_generators_finalized`` and ``page_writer_finalized``

For a full list of changes, see: https://github.com/getpelican/pelican/compare/3.5.0...3.6.0

Upgrading from previous releases
================================

`Content generation caching
<http://docs.getpelican.com/en/latest/settings.html#reading-only-modified-content>`_
is now disabled by default. If you have a large site with many articles/pages
and notice that site generation takes longer than you would prefer, follow
these two steps:

1. Delete the ``cache`` folder, if it exists
2. Add the following to your settings file::

    CACHE_CONTENT = True
    LOAD_CONTENT_CACHE = True

While we do everything we can to maximize backwards compatibility and ensure
smooth Pelican upgrades, it's possible that you may encounter un-anticipated
wrinkles. If you run into problems, please see the `How to Get Help
<http://docs.getpelican.com/en/latest/contribute.html#how-to-get-help>`_ section
of the documentation, and we will update this post with any upgrade tips
contributed by the Pelican community.
