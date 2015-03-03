Using Pelican with Heroku
#########################

:date: 2013-07-25
:author: Kyle Fuller
:tags: deployment

Using Pelican with Heroku couldn't be easier. We have recently been working on
a buildpack allowing you to publish your Pelican site directly to Heroku.

This allows you to host your Pelican site on the Heroku platform with very little
effort. Simply create a Heroku application and push your repository to it.

You don't need to deal with generating the HTML with the Pelican command — the
buildpack takes care of this. Just push a git repository with the
`pelicanconf.py` file in the root directory.

To enable the Heroku buildpack for existing sites, run:

.. code-block:: bash
    
    heroku buildpack:set https://github.com/getpelican/heroku-buildpack-pelican

Alternatively, for those of you switching to Heroku, you can use the following
command to create your Pelican site on Heroku.

.. code-block:: bash

    heroku create myapp --buildpack https://github.com/getpelican/heroku-buildpack-pelican

