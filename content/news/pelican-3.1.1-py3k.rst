==========================
Pelican's Unified Codebase
==========================

:date: 2013-04-16

*In this post by* `Dirk Makowski <https://github.com/dmdm>`_, *he
explains how he added preliminary Python 3.x support to the forthcoming
Pelican 3.2 release.*

------------------------------------------------------------------------------

When referring to Pelican's "unified" codebase, this means the code runs
without changes (or requiring ``2to3``) on both Python 2.x and 3.x.
Specifically, this unified codebase is tested on Python 2.7 and 3.2.

At the time of this writing all tests pass, whether manually invoked
via ``python -m unittest discover`` within manually-created virtual
environments or via ``tox``, which automatically creates virtual environments
for Python 2.7 and 3.2 and runs tests on both Python versions::

    74 tests, 9 skips, no errors

During my first attempt to port Pelican to Python 3, I had used 2to3 and
manually applied corrections to achieve syntactical correctness. But as the
tests showed, more subtle bugs in the encoding of strings remained (e.g.
outputting b'...' instead of '...'). Also, the code was suitable for Python 3
only and would not run properly on Python 2.

Building on the lessons learned with 2to3, the current in-development version
of Pelican now provides a single codebase for Python 2 and 3. The following
section lists some hints about what had to be changed in order to achieve this.
These hints may also be valuable for anyone who wants to contribute new Pelican
features or bug fixes, since all Pelican code submissions must now run on both
Python versions.


Unification
===========


- Assume every string and literal is Unicode (import unicode_literals):

  - Do not use prefix ``u'``.
  - Do not encode/decode strings in the middle. Follow the code to the source
    (or target) of a string and encode/decode at the first/last possible point.
  - In other words, write your functions to expect and to return Unicode.
  - Encode/decode strings if the source is a Python function that is known
    to handle this badly, e.g., ``strftime()`` in Python 2.

- Use new syntax: print function, "except ... *as* e" (not comma) etc.
- Refactor method calls like ``dict.iteritems()``, ``xrange()`` etc. in a way
  that runs without code change in both Python versions.
- Do not use magic method ``__unicode()__`` in new classes. Use only ``__str()__``
  and decorate the class with ``@python_2_unicode_compatible``.
- Do not start int literals with a zero. This is a syntax error in Py3k.
- Unfortunately I did not find an octal notation that is valid in both
  Pythons. Use decimal instead.
- use ``six``, e.g.:

  - ``isinstance(.., basestring) -> isinstance(.., six.string_types)``
  - ``isinstance(.., unicode) -> isinstance(.., six.text_type)``

- ``setlocale()`` in Python 2 bails when we give the locale name as Unicode,
  and since we are using ``from __future__ import unicode_literals``, we do
  that everywhere! As a workaround, I enclosed the localename with ``str()``;
  in Python 2 this casts the name to a byte string, and in Python 3 this should
  do nothing, because the locale name is already in Unicode.

- Kept range() almost everywhere as-is (2to3 suggests list(range())) — just
  changed it where I felt necessary.

- Changed xrange() back to range(), so it is valid in both Python versions.


About External Libraries
========================

Core
----

Pelican core depends on ``feedgenerator``. To run on Py3k, you will need
``feedgenerator`` 1.5, which also now has a unified codebase and is available
on PyPI.

BeautifulSoup had to be upgraded to bs4 (only bs4 supports Py3k), which has some
consequences:

- To parse XML (e.g., which the WordPress importer does), the ``lxml`` package
  is now required.
- bs4 does not have ``convertEntities`` anymore.

Plugins
-------

On Python 2 you still can use all plugins and their dependencies as they are.
But if you want to use Pelican plugins on Python 3, you must seek out and
install compatible packages yourself.

For **Typogrify** and **SmartyPants**, on which Typogrify depends, I provide
ready-made 2to3'd code:

- https://github.com/dmdm/smartypants.git
- https://github.com/dmdm/typogrify/tree/py3k

For **webassets**, I also have 2to3'd code available:

- https://github.com/dmdm/webassets/tree/py3k

But ``webassets`` still has issues. One is that the less-css compiler is not
correctly invoked when I build the blog (e.g., with ``make html``); I have to
manually invoke the compiler afterwards::

    lessc themes/pymblog/static/less/pymblog.less > output/theme/css/pymblog.css

Be aware that the 2to3'd code of aforementioned libraries runs on Python 3 only.


Testing
=======

Testing on Python 2 is straightforward.

On Python 3, if you have installed the Python 3.x-compatible versions of the
plugins, like shown in the previous chapter, manual testing with
``python -m unittest discover`` is also straightforward.

However, you must tell tox to use those Py3k libraries. If you forget this,
tox will pull the regular packages from PyPI and the tests will fail.

Tell tox about the local packages thusly: enter the source directory of
SmartyPants and run tox there. Do this again for Typogrify and webassets.
SmartyPants and Typogrify do not have real tests, and webassets will fail
noisily, but as a result we get these libraries neatly packaged in tox's
distshare directory. And this is what we need to order to run tox for Pelican.

See also the comments in ``tox.ini`` for more detail.
