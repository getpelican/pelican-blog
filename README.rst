The pelican's blog
##################

This is the pelican's project weblog. You can add content to it by forking it
or pushing direcly on github. When you do so, if you update the gh-pages
branch, then you'll update the content of the generated blog.

The makefile has a rule to do that for you, when you're ready to publish, and
if you have the rights, you just have to type::

    make github

If you have an error, ensure that you have "ghp-import" installed on your
machine. If not you can install it with `pip install ghp-import`.

and it will generate the content locally, create a commit in the good git
branch and push it to github.
