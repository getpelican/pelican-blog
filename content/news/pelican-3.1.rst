Pelican 3.1 released
####################

:date: 2012-12-03

Pelican development has progressed steadily over the last few months, and we're
pleased to announce the release of version 3.1, which can be obtained via
`Crate.io <https://crate.io/packages/pelican/>`_ or
`GitHub <https://github.com/getpelican/pelican/tags>`_. This release contains
some exciting new features; following is a summary of changes since the last
3.0.1 release.

Easier intra-site linking
=========================

Whether linking from one post to another or including locally-hosted images on
a page, linking to intra-site resources has been significantly enhanced. In
addition to improving reliability, it's now possible to link to a resource in
your *source content* hierarchy instead of the *generated* hierarchy.

Find more information here:
http://docs.getpelican.com/en/3.1.1/getting_started.html#linking-to-internal-content

Metadata extraction from filename
=================================

There is a new ``FILENAME_METADATA`` setting that adds support for metadata
extraction from the filename via regular expressions. For example, if you
would like to extract both the date and the post slug from the filename, you
could set your ``FILENAME_METADATA`` setting to something like:
``'(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'``



Web asset processing moved to separate plugin
=============================================

We are trying to move non-essential features out of the Pelican core and
instead make them available as plugins. Web asset management is an example of
this effort — we don't think this is a core component of Pelican, but it's
still a useful feature and remains available to those who want to use it.

New gzip cache plugin
=====================

The gzip cache plugin allows generated text files to be compressed once during
site generation and thus served without needing any server-side compression.
This obviates the need for the web server to compress these text files
on-the-fly, which can result in lower web server CPU utilization.

Basic functional tests restored
===============================

We now have a way to fully test Pelican's output, which helps us understand
whether code changes break Pelican's intended behavior (for developers and for
end users) while we are developing new features.

Template pages
==============

If you want to generate custom pages besides your blog entries, you can use
any Jinja template file with a path pointing to the file and the destination
path for the generated file. For instance, if you have a blog with three
static pages — a list of books, your resume, and a contact page — you could
set them up via:

.. code-block:: python

    TEMPLATE_PAGES = {'src/books.html': 'dest/books.html',
                      'src/resume.html': 'dest/resume.html',
                      'src/contact.html': 'dest/contact.html'}

Feed improvements
=================

The ``FEED_ALL_ATOM`` and ``FEED_ALL_RSS`` directives have been introduced as
distinct from their ``FEED_ATOM`` and ``FEED_RSS`` brethren.  The former show
entries in all available language translations, while the latter only include
entries written in the site's primary language.

Use folders as category
=======================

Until now, Pelican made the assumption that the folders used to organize your
content should be used as the respective categories of the articles contained
within. You now can configure this behavior via the ``USE_FOLDER_AS_CATEGORY``
setting.

New signals
===========

Plugins now have additional signals at their disposal:

* We now provide a ``generator_init`` signal that is sent when the generator
  is initialized. You'll receive the generator as an argument.
* ``get_generators`` is invoked in ``Pelican.get_generator_classes`` and can
  return a Generator or several generators in a tuple or list. This is useful
  when you want to add your own generators.
* ``article_generate_preread`` is invoked before an article is read in
  ``ArticlesGenerator.generate_context``. Use this if the code needs to do
  something before every article is parsed.

Minor enhancements and fixes
============================

* Empty value for the ``AUTHOR`` setting is now allowed
* Improved WordPress importing
* Generated content doesn't contain as much blank lines as it did previously
* New icon for Google+ and improvements to many others
* Many small documentation and bug fixes not described here

On the horizon
==============

* We are working on moving plugins out of the main Pelican repository and into a
  `separate repository <http://github.com/getpelican/pelican-plugins>`_.

* We would like to implement measures designed to speed up site generation in
  order to reduce processing time.

* In order to provide more regular updates on development progress, we intend
  to publish blog posts on a more frequent basis.

That's all for now. More to come soon!  :-)
