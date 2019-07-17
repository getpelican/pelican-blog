Pelican 4.0 released
####################

:date: 2018-11-13
:slug: pelican-4.0-released

Pelican 4.0 has been released, including many enhancements, fixes, and tweaks.
Highlights include:

* Replace ``develop_server.sh`` script with ``pelican --listen``
* Improved copy/link behavior for large static files (e.g., videos)
* New ``{static}`` syntax to link to static content
* Pages can now have ``draft`` status
* Show current settings via new ``--print-settings`` flag
* Replace Fabric’s ``fabfile.py`` with Invoke’s ``task.py``
* Importer improvements

For more info, please refer to the `release page`_ or the `Release History`_
section of the documentation. For a more comprehensive list of changes, please
review the respective milestone_ for this release. For the full list of changes,
see: https://github.com/getpelican/pelican/compare/3.7.1...4.0.0

Upgrading from previous releases
================================

You may see deprecation warnings for certain settings. If that occurs, please
change the specified setting to the new setting mentioned in the deprecation
message.

Due to `Python-Markdown changes`_, Markdown users must ensure they are using
version < 3.0 or >= 3.1 to ensure proper rendering of code blocks.

Some user-submitted themes use positional argument formatting on object-related
feed URLs, which will cause sites to fail to build with: "TypeError: not all
arguments converted during string formatting". In that case, the theme needs to
be updated. For example, substitute ``TAG_FEED_ATOM|format(tag.slug)`` with
``TAG_FEED_ATOM.format(slug=tag.slug)``. Affected variables include:

* ``CATEGORY_FEED_ATOM``
* ``CATEGORY_FEED_ATOM_URL``
* ``CATEGORY_FEED_RSS``
* ``CATEGORY_FEED_RSS_URL``
* ``AUTHOR_FEED_ATOM``
* ``AUTHOR_FEED_ATOM_URL``
* ``AUTHOR_FEED_RSS``
* ``AUTHOR_FEED_RSS_URL``
* ``TAG_FEED_ATOM``
* ``TAG_FEED_ATOM_URL``
* ``TAG_FEED_RSS``

As always, we do everything we can to maximize backwards compatibility and ensure
smooth Pelican upgrades. If you run into problems, please see the `How to Get Help
<https://docs.getpelican.com/en/latest/contribute.html#how-to-get-help>`_ section
of the documentation, and we will update this post with any upgrade tips
contributed by the Pelican community.

.. _release page: https://github.com/getpelican/pelican/releases/tag/4.0.0
.. _Release History: https://docs.getpelican.com/en/4.0.0/changelog.html
.. _milestone: https://github.com/getpelican/pelican/milestone/12?closed=1
.. _Python-Markdown changes: https://github.com/getpelican/pelican/issues/2493
