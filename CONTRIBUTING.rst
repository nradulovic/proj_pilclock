.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/nradulovic/pilclock/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

PilClock could always use more documentation, whether as part of the
official PilClock docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at 
https://github.com/nradulovic/pilclock/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `pilclock` for local development.

1. Fork the `pilclock` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/pilclock.git

3. Install your local copy into a virtualenv. Assuming you have 
   virtualenvwrapper installed, this is how you set up your fork for local 
   development::

    $ mkvirtualenv pilclock
    $ cd pilclock/
    $ python setup.py develop

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the
   tests, including testing other Python versions with tox::

    $ flake8 pilclock tests
    $ python setup.py test or py.test
    $ tox

   To get flake8 and tox, just pip install them into your virtualenv.

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Using tox automation project
----------------------------

Preferred way of development is to use tox which aims to automate and
standardize testing in Python. Tox is generic virtualenv management and test
command line tool. For more details, please, refer to: tox_.

1. Fork the `pilclock` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/pilclock.git

3. Install tox using your distribution package manager. On Ubuntu/Debian do::
    
    $ sudo apt install tox

4. Navigate to `pilclock` directory and start tox::

    $ tox

This will create Python virtualenvs, install necessary dependencies and execute
necessary tests and flake8.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for multiple versions of Python. Check
   https://travis-ci.org/nradulovic/pilclock/pull_requests
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests::

$ py.test tests.test_pilclock


Deploying
---------

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in HISTORY.rst).
Then run::

$ bumpversion patch # possible: major / minor / patch
$ git push
$ git push --tags

Travis will then deploy to PyPI if tests pass.

.. _tox: https://tox.readthedocs.io
