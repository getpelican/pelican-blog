Weekly update #1
################

:date: 30/11/2012

Okay, what do we want to put there, then?  Pelican development is going well,
we've been working on different things in the past months, and there are tons
of exciting stuff to read about; in order to keep you updated, we'll try to
write a blog post from time to time (weekly maybe?) to keep you posted on the
new features.  This tries to summarize what's been worked since the last
release (3.0.1).

Metadata extraction from filename
=================================

There is a new ``FILENAME_METADATA`` setting which adds support for metadata
extraction from the filename via regular expressions.  For example, if you
would like to extract both the date and the post slug from the filename, you
could set your ``FILENAME_METADATA`` setting to something like:
``'(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'``

Moved webassets to separate plugin
==================================

We are trying to move a maximum of non-core features of pelican out of pelican
itself, and making them available as plugins.  That's the case for the
management of webassets. We don't think this is a core component of pelican,
but that's still an useful feature.  In case you want to use it, you'll need to 

A new gzip cache plugin
=======================

We have discussions going on about a new gzip plugin which would allow the
generated content to be compressed once and served directly compressed. This
means less work to compress the files on the fly by the web-server, and thus
eats less cpu.

Restored the basic functional tests
===================================

We now have a way to fully test the output of pelican.  That's useful to know
if we're breaking pelican's behaviours while developing new features (for us or
for you).

Template pages
==============

If you want to generate custom pages besides your blog entries, you can point
any Jinja2 template file with a path pointing to the file and the destination
path for the generated file.  For instance, if you have a blog with three
static pages, for a list of books, your resume and a contact page, you could
have:

.. code-block::

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

Until now, pelican worked making the assumption that the folders you put your
content into was the category of the article.  You now can configure this
behavior, using the USE_FOLDER_AS_CATEGORY setting.

Minor enhancements and fixes
============================

* Blank AUTHOR value is now supported
* The generated content doesn't contain as much blank lines as it did
  previously
* New icon for Google+ and improvements to many others 
* Of course, there are a lot of little doc and bug fixes which aren't described
  here

new signals
-----------

The plugins can now use more signals:

*  We now provide a `generator_init` signal, which is sent when the  generator
   is initialized.You'll receive the generator as an argument.
* `get_generators`  is invoked in Pelican.get_generator_classes, and can
  return a Generator, or several generator in a tuple or in a list. That's useful
  to add you own generators.
* `article_generate_preread` is invoked before a article is read in
  ArticlesGenerator.generate_context; use if code needs to do something before
  every article is parsed

On the pipes
============

* We're working on moving the plugins away from pelican-core and making them
  available in a separate repository
  (http://github.com/getpelican/pelican-plugins ) in order to keep pelican core
  clean.
* This is a long awaited feature: we're removing the url-rewriting done by
  pelican, and adding a way to do cross-site links. Check out
  https://github.com/getpelican/pelican/pull/460/

And that's it for now :-)
