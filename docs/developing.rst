.. _developing:

Contributing to Tron
====================

Tron is an open source project and welcomes contributions from the community.
The source and issue tracker are hosted on github at
http://github.com/yelp/Tron.

Setting Up an Environment
-------------------------

Tron works well with `virtualenv <http://www.virtualenv.org>`_, which can be
setup using `virtualenvwrapper
<http://www.doughellmann.com/projects/virtualenvwrapper/>`_::

    $ mkvirtualenv tron --distribute --no-site-packages
    $ pip install -r dev/req_dev.txt

``req_dev.txt`` contains a list of packages required for development, including:
`Testify <https://github.com/yelp/testify>`_ to run the tests and `Sphinx
<http://sphinx.pocoo.org/>`_ to build the documentation.

Coding Standards
----------------

All code should be `PEP8 <http://www.python.org/dev/peps/pep-0008/>`_ compliant,
and should pass pyflakes without warnings. All new code should include full
test coverage, and bug fixes should include a test which reproduces the
reported issue.

This documentation must also be kept up to date with any changes in functionality.


Running Tron in a Sandbox
-------------------------

The source package includes a development logging.conf and a
sample configuration file with a few test cases. To run a development intsance
of Tron create a working directory and start
:command:`trond` using the following::

    $ make dev


Running the Tests
-----------------
Tron uses the `Testify <https://github.com/Yelp/Testify>`_ unit testing
framework.


Run the tests using ``make tests`` or ``testify tests``.  If you're using a
virtualenv you may want to run ``python `which testify` test`` to have it
use the correct environment.

This package also includes a ``.pyautotest`` file which can be used with
https://github.com/dnephin/PyAutoTest to auto run tests when you save a file.

Contributing
------------

There should be a github issue created prior to all pull requests.  Pull requests
should be made to the ``Yelp:development`` branch, and should include additions to
``CHANGES.txt`` which describe what has changed.
