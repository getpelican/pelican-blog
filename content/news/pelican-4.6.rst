Pelican 4.6 released
####################

:date: 2021-03-23
:slug: pelican-4.6-released

Pelican 4.6 is now available. Thanks to `Tom Adler’s contribution <https://github.com/getpelican/pelican/pull/1401>`_, this release contains a new feature that allows for more SEO-friendly index pages, whereby ``/page-1/`` contains the *oldest* articles, with newer articles placed on ``/page-2/``, ``/page-3/``, etc. That way, the names of the previous article index pages do not change every time a new index page is generated. Cool URLs don’t change!

To enable this feature, first add a pagination pattern for ``-1`` to your Pelican settings file. For example:

.. code-block:: python

    PAGINATION_PATTERNS = (
        (1, "{base_name}/page-1/", "{base_name}/page-1/index.html"),
        (2, "{base_name}/page-{number}/", "{base_name}/page-{number}/index.html"),
        (-1, "{base_name}/", "{base_name}/index.html"),
    )

You will also benefit from changing other settings to match the intended behavior. For example:

.. code-block:: python

    DEFAULT_PAGINATION = 5
    DEFAULT_ORPHANS = 4
    ARTICLE_ORDER_BY = "date"
    REVERSE_ARCHIVE_ORDER = True
    NEWEST_FIRST_ARCHIVES = True

In your theme’s ``index.html`` and ``tag.html`` templates, change the ``object_list`` loop to ``object_list[::-1]`` to reverse the order of the article list:

.. code-block:: jinja

    {% for article in articles_page.object_list[::-1] %}

Make sure the pagination links below the list are changed to reflect the switched direction of “next” vs. “previous” articles. For example:

.. code-block:: jinja

    {% if articles_page.has_next() %}
        <a class="pagination-item newer" href="{{ SITEURL }}/{{ articles_next_page.url }}">next</a>
        {% else %}
        <span class="pagination-item newer">next</span>
    {% endif %}
    {% if articles_page.has_previous() %}
        <a class="pagination-item older" href="{{ SITEURL }}/{{ articles_previous_page.url }}">previous</a>
        {% else %}
        <span class="pagination-item older">previous</span>
    {% endif %}

While this is general guidance and will apply differently depending on your chosen theme, hopefully the above helps you get further along experimenting with this new feature.

This new release also includes the following enhancements, fixes, and tweaks:

* Speed up ``livereload`` Invoke task via caching `(#2847) <https://github.com/getpelican/pelican/pull/2847>`_
* Ignore ``None`` return value from ``get_generators`` signal `(#2850) <https://github.com/getpelican/pelican/pull/2850>`_
* Relax dependency minimum versions and remove upper bounds

For more info, please refer to the `release page`_ or the `Release History`_
section of the documentation. For the full list of changes, see:
https://github.com/getpelican/pelican/compare/4.5.4...4.6.0

Upgrading from previous releases
================================

Upgrading from Pelican 4.5.x should be smooth and require few (if any) changes to your environment. If upgrading from a previous release, review the other release announcements on this site to better understand what action might be necessary.

As always, we do everything we can to maximize backwards compatibility and ensure
smooth Pelican upgrades. If you run into problems, please see the `How to Get Help
<https://docs.getpelican.com/en/latest/contribute.html#how-to-get-help>`_ section
of the documentation, and we will update this post with any upgrade tips
contributed by the Pelican community.

.. _release page: https://github.com/getpelican/pelican/releases/tag/4.6.0
.. _Release History: https://docs.getpelican.com/en/4.6.0/changelog.html
