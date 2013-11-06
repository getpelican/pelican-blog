Pelican 3.3 released
####################

:date: 2013-09-24
:slug: pelican-3.3-released

Today we are pleased to announce the release of Pelican 3.3. Highlights of the
improvements contained in this release follow below.

For those who are new to Pelican, please refer to the `Getting Started Guide
<http://docs.getpelican.com/en/3.3.0/getting_started.html>`_. There is also a
`Tutorials <https://github.com/getpelican/pelican/wiki/Tutorials>`_ page
available, which currently includes a link to a Pelican installation
screencast.

Highlights
==========

Python 3.3 support
------------------

Following up on the last release's `support for Python 3.2
<http://blog.getpelican.com/pelicans-unified-codebase.html>`_, this new version
of Pelican now supports Python 3.3. In order to do so, support for Python 3.2
unfortunately had to be dropped.

Cross-platform automation via Fabric
------------------------------------

Pelican has traditionally included a ``make``-based workflow that works well
enough for POSIX-based systems but at the expense of Windows users. In order to
improve cross-platform publishing automation, Pelican 3.3 includes support for
Fabric, a Python-based automation framework.

Retain certain files in output
------------------------------

Some folks apply version control to their output directories, the metadata for
which is obliterated when using the ``DELETE_OUTPUT_DIRECTORY`` directive.
Pelican 3.3 includes a new ``OUTPUT_RETENTION`` setting which allows you to
define arbitrary files/folders that should be retained during the
aforementioned output cleaning process (e.g., ``.hg``, ``.git``, et cetera).

Tumblr import
-------------

Tumblr posts can now be imported into Pelican sites.

Refactoring, fixes, and improvements
------------------------------------

Pelican 3.3 includes a significant number of other improvements, as indicated
by the long list of items in the `changelog
<https://github.com/getpelican/pelican/blob/master/docs/changelog.rst>`_ and
the `Pelican 3.3 milestone issues
<https://github.com/getpelican/pelican/issues?milestone=5&state=closed>`_ list.

Upgrade notes
=============

While we do everything we can to maximize backwards compatibility and ensure
smooth Pelican upgrades, it's possible that you may encounter un-anticipated
wrinkles. Following are a few notes that may help:

* The ``FILES_TO_COPY`` setting has been deprecated, so replace it with the
  ``STATIC_PATHS`` and ``EXTRA_PATH_METADATA`` settings. Refer to the
  corresponding entries in the `Settings section of the docs
  <http://docs.getpelican.com/en/3.3.0/settings.html#basic-settings>`_ for more
  information.

* Due to minor changes to the plugin API, some plugins may not function
  properly if they are not updated accordingly. Most (if not all) of the
  plugins in the official `Pelican Plugins Repository
  <https://github.com/getpelican/pelican-plugins>`_ have already been updated,
  but externally-hosted plugins may not be. If you are heavily dependent on
  such a plugin, consider holding off on upgrading to Pelican 3.3 until you are
  certain that your desired plugins will function correctly.

* PDF generation has been moved out of core and into a separate plugin. If you
  previously relied on this feature, please be sure to retrieve, install, and
  configure the new plugin from the `Pelican Plugins Repository
  <https://github.com/getpelican/pelican-plugins>`_.

* There is a new warning for ``<img>`` tags without ``alt=""`` attributes,
  which are important for accessibility reasons. Please consider adding these
  attributes to your ``<img>`` tags in order to improve accessibility (and
  eliminate the warnings).

* The syntax for linking to source content has been changed in order to ensure
  compatibility with Markdown and reST extensions. For example, the new syntax
  for Markdown: ``[a link relative to content root]({filename}/article1.md)``
  The previous ``|filename|/article1.md`` syntax will continue to be supported
  for backwards compatibility.

We will keep the above list updated with any additional items as we find them,
so please let us know if we missed anything.
