Pelican 4.7 released
####################

:date: 2021-10-01
:slug: pelican-4.7-released

Pelican 4.7 is now available. This new release includes the following enhancements, fixes, and tweaks:

* Improve default theme rendering on mobile and other small screen devices `(#2914) <https://github.com/getpelican/pelican/pull/2914>`_
* Add support for hidden articles `(#2866) <https://github.com/getpelican/pelican/pull/2866>`_
* Improve word count behavior when generating summary CJK & other locales `(#2864) <https://github.com/getpelican/pelican/pull/2864>`_
* Add progress spinner during generation `(#2869) <https://github.com/getpelican/pelican/pull/2869>`_
  and richer logging `(#2897) <https://github.com/getpelican/pelican/pull/2897>`_, both via `Rich <https://github.com/willmcgugan/rich>`_
* Invoke tasks ``serve`` and ``livereload`` now auto-open a web browser pointing to the locally-served web site `(#2764) <https://github.com/getpelican/pelican/pull/2764>`_
* Support some date format codes used by ISO dates `(#2902) <https://github.com/getpelican/pelican/pull/2902>`_
* Document how to add a new writer `(#2901) <https://github.com/getpelican/pelican/pull/2901>`_

For more info, please refer to the `release page`_ or the `Release History`_
section of the documentation. For the full list of changes, see:
https://github.com/getpelican/pelican/compare/4.6.0...4.7.0

Upgrading from previous releases
================================

Upgrading from Pelican 4.6.x should be smooth and require few (if any) changes to
your environment. If upgrading from a previous release, review the other release
announcements on this site to better understand what action might be necessary.

As always, we do everything we can to maximize backwards compatibility and ensure
smooth Pelican upgrades. If you run into problems, please see the `How to Get Help
<https://docs.getpelican.com/en/latest/contribute.html#how-to-get-help>`_ section
of the documentation, and we will update this post with any upgrade tips
contributed by the Pelican community.

.. _release page: https://github.com/getpelican/pelican/releases/tag/4.7.0
.. _Release History: https://docs.getpelican.com/en/4.7.0/changelog.html
