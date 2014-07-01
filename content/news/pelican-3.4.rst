Pelican 3.4 released
####################

:date: 2014-07-01
:slug: pelican-3.4-released

Today we are pleased to announce the release of Pelican 3.4, which is one of
the more significant updates Pelican has ever seen. Take a look at the `changelog
<https://github.com/getpelican/pelican/blob/master/docs/changelog.rst>`_ and
the `Pelican 3.4 milestone issues
<https://github.com/getpelican/pelican/issues?milestone=6&state=closed>`_ list
to see all the features, fixes, and miscellaneous improvements that are
included in this release.

Major highlights
================

Faster rebuild times
--------------------

Thanks to a new caching mechanism and selective output writing, rebuilding
a site can take just a few seconds. Tinkering with posts and themes is now
even easier.

Fixed locale and encoding issues
--------------------------------

Finally URLs can include, for example, localized month names.

Improved documentation, both in style and content
-------------------------------------------------

The documentation has been ported to the new ReadTheDocs theme, including a
functional search bar and a navigation side panel. A quickstart section is now
provided to jump-start your Pelican experience.

Support for multiple post authors
----------------------------------

The new ``:authors:`` metadata field makes it possible to easily manage
multi-user sites.


Upgrading from previous releases
================================

While we do everything we can to maximize backwards compatibility and ensure
smooth Pelican upgrades, it's possible that you may encounter un-anticipated
wrinkles. If you run into problems, please reach out via the #pelican channel
on IRC, and we will update this post with any upgrade tips contributed by the
Pelican community.
