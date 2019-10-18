Pelican 4.1 released
####################

:date: 2019-07-14
:slug: pelican-4.1-released

Pelican 4.1 has been released and includes the following enhancements, fixes,
and tweaks:

* Live browser reload upon changed files (provided via Invoke task)
* Add ``pyproject.toml``, managed by Poetry
* Support for invoking ``python -m pelican``
* Add relative source path attribute to content
* Allow directories in ``EXTRA_PATH_METADATA``
* Add ``all_articles`` variable to period pages (for recent posts functionality)
* Improve debug mode output
* Remove blank or duplicate summaries from Atom feed
* Fix bugs in pagination, pelican-import, pelican-quickstart, and feed importer

For more info, please refer to the `release page`_ or the `Release History`_
section of the documentation. For a more comprehensive list of changes, please
review the respective milestone_ for this release. For the full list of changes,
see: https://github.com/getpelican/pelican/compare/4.0.1...4.1.0

As always, we do everything we can to maximize backwards compatibility and ensure
smooth Pelican upgrades. If you run into problems, please see the `How to Get Help
<https://docs.getpelican.com/en/latest/contribute.html#how-to-get-help>`_ section
of the documentation, and we will update this post with any upgrade tips
contributed by the Pelican community.

.. _release page: https://github.com/getpelican/pelican/releases/tag/4.1.0
.. _Release History: https://docs.getpelican.com/en/4.1.0/changelog.html
.. _milestone: https://github.com/getpelican/pelican/milestone/14?closed=1
