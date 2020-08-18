Pelican 4.5 released
####################

:date: 2020-08-20
:slug: pelican-4.5-released

Pelican 4.5 is now available. Its marquee feature is support for “namespace” plugins, which means any plugin listed under the new `Pelican Plugins`_ organization can be installed via Pip, after which Pelican should automatically detect and enable the new plugin.

This also means that Pelican projects can specify and pin plugin versions, which helps ensure plugin updates do not cause unexpected problems building your site. For example, here we define a project’s Pelican and plugin versions via Poetry_ and ``pyproject.toml``:

.. code-block:: toml

   [tool.poetry.dependencies]
   pelican = "^4.5"
   pelican-simple-footnotes = "^1.0"
   pelican-sitemap = "^1.0"
   pelican-webring = "^1.0"

If one of the above plugins introduces a breaking change in v2.0, for example, there shouldn’t be any related disruption since above we have effectively pinned plugin versions to: ``>= 1.0, <2.0``

This new release also includes the following enhancements, fixes, and tweaks:

* List registered plugins via ``pelican-plugins`` command
* Override settings via ``-e`` / ``--extra-settings`` CLI option flags
* Add settings for custom Jinja globals and tests
* Customize article summary ellipsis via ``SUMMARY_END_MARKER`` setting
* Customize Typogrify dash handling via new ``TYPOGRIFY_DASHES`` setting
* Support Unicode when generating slugs
* Support Asciidoc ``.adoc`` file generation in Pelican importer
* Improve user experience when ``pelican --listen`` web server is quit
* Improve Invoke tasks template
* Include tests in source distributions
* Switch CI from Travis to GitHub Actions
* Remove support for Python 2.7

For more info, please refer to the `release page`_ or the `Release History`_
section of the documentation. For a more comprehensive list of changes, please
review the respective milestone_ for this release. For the full list of changes,
see: https://github.com/getpelican/pelican/compare/4.2.0...4.5.0

Upgrading from previous releases
================================

First, since Python 2.7 support has been dropped, ensure you are using Python 3.6+.

Next, if your site uses any Pelican plugins:

1. Have all your plugins been migrated to the new `Pelican Plugins`_ organization? If so, you can Pip-install those plugins, comment out the ``PLUGINS`` variable in your settings file, and ensure your site builds properly. If everything seems to be in order, you can remove the ``PLUGINS`` setting as well as any local ``plugin`` folders that contain legacy plugins.

2. If you are using one or more plugins that have not yet been migrated to the new `Pelican Plugins`_ organization, this is a great opportunity to contribute to Pelican by assisting with plugin migration. Create a new issue at the `legacy plugin repo <https://github.com/getpelican/pelican-plugins/issues>`_ and communicate which plugin you would like to help migrate, after which a Pelican maintainer will guide you through the process.

3. If you want to use a mix of namespace & legacy plugins, or if you prefer to manually specify plugins instead of relying on Pelican’s automatic detection, you can use the ``PLUGINS`` setting as described in the `How to Use Plugins <https://docs.getpelican.com/en/latest/plugins.html#how-to-use-plugins>`_ documentation.

As always, we do everything we can to maximize backwards compatibility and ensure
smooth Pelican upgrades. If you run into problems, please see the `How to Get Help
<https://docs.getpelican.com/en/latest/contribute.html#how-to-get-help>`_ section
of the documentation, and we will update this post with any upgrade tips
contributed by the Pelican community.

.. _Pelican Plugins: https://github.com/pelican-plugins
.. _Poetry: https://python-poetry.org/
.. _release page: https://github.com/getpelican/pelican/releases/tag/4.5.0
.. _Release History: https://docs.getpelican.com/en/4.5.0/changelog.html
.. _milestone: https://github.com/getpelican/pelican/milestone/16?closed=1

