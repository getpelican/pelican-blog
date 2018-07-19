Pelican 3.7 released
####################

:date: 2016-12-12
:slug: pelican-3.7-released

Pelican 3.7 has been released, incorporating a year and a half worth of
enhancements and bug fixes.

To see highlights, please refer to the `release page`_ or the `Release History`_
section of the documentation. For a more comprehensive list of changes, please
review the respective milestone_ for this release. For the full list of changes,
see: https://github.com/getpelican/pelican/compare/3.6.3...3.7.0

Upgrading from previous releases
================================

Unlike Atom, the RSS feed specification does not contain a ``<content>`` field
and only contains a ``<summary>`` field. Pelican previously put the full content
in this field, which could cause odd behavior in feed readers that only expected
a summary. For this reason, RSS feeds in Pelican 3.7 will by default only contain
article summaries. To revert to the previous full-content behavior, either
use Atom (which supports both ``<summary>`` and ``<content>`` fields) or set:
``RSS_FEED_SUMMARY_ONLY = False``

If you have defined ``MD_EXTENSIONS`` in your settings file, you will see
deprecation warnings since that setting has been replaced by the ``MARKDOWN``
setting in Pelican 3.7. Refer to the corresponding entry in the Settings_
documentation to see the new default value and replace any existing
``MD_EXTENSIONS`` settings with your preferred customized variation of the
``MARKDOWN`` setting.

Themes originally had access to two identical context variables: ``PAGES`` and
``pages``. This redundancy was removed in Pelican 3.7, so any themes that use
``PAGES`` will need to be updated to use ``pages`` instead.

``JINJA_EXTENSIONS`` has been replaced by the ``JINJA_ENVIRONMENT`` setting.
Any plugins that refer to the former setting will need to be updated. Refer to
the corresponding entry in the Settings_ documentation for more information.

As always, we do everything we can to maximize backwards compatibility and ensure
smooth Pelican upgrades. If you run into problems, please see the `How to Get Help
<http://docs.getpelican.com/en/latest/contribute.html#how-to-get-help>`_ section
of the documentation, and we will update this post with any upgrade tips
contributed by the Pelican community.

.. _release page: https://github.com/getpelican/pelican/releases/tag/3.7.0
.. _Release History: http://docs.getpelican.com/en/3.7.0/changelog.html
.. _milestone: https://github.com/getpelican/pelican/milestone/9?closed=1
.. _Settings: http://docs.getpelican.com/en/3.7.0/settings.html
