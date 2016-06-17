========================================
python-everywhere
========================================

|python|
|version|
|issues|
|travis|
|license|
|coveralls|
|pypi-v|
|pypi-dm|
|pypi-dd|
|gitter|
|code-climate|


This is a sample to help you with
integrating services into your Python project !

Inspired by `rust-everywhere <https://github.com/japaric/rust-everywhere>`_.


.. contents:: Table of Contents



Features
========================================

* Travis CI integration
* pytest integration for testing
* flake8 integration (invoke by pytest)
* pylint integration (invoke by pytest)
* coverage integration (invoke by pytest)
* pydocstyle integration
* mypy integration (optional static type checker)
* Publish to PyPI with Travis CI automatically (when tagging new release)
* Publish to GitHub with Travis CI automatically (when tagging new release)



Installation
========================================

.. code-block:: sh

    python setup.py install



Testing
========================================

pytest
------------------------------

With `pytest-runner <https://github.com/pytest-dev/pytest-runner>`_,
we will have ``python setup.py pytest``.

With ``addopts = --doctest-modules`` in ``pytest.ini``,
we will also invoke doctest.

With alias in ``setup.cfg``, we can just use ``python setup.py test``.

run your test code :

.. code-block:: sh

    python setup.py test
    python setup.py test --addopts -v   # verbose


Here is the pytest's `documetation <https://pytest.org/latest/goodpractices.html#integrating-with-setuptools-python-setup-py-test-pytest-runner>`_ about integrating with setuptools.


Coverage
------------------------------

With ``coverage``, we can generate testing coverage report.
With ``pytest-cov`` and
``--cov-report html`` ``--cov-report term`` in the ``pytest.ini``,
we can generate testing coverage report along with running testing code.


Coveralls
------------------------------

Please visit ``https://coveralls.io/`` to create coveralls for your repo.



Linter
========================================

Flake8
------------------------------

.. code-block:: sh

    python setup.py flake8


Here is the flake8's `documetation <http://flake8.readthedocs.io/en/latest/setuptools.html>`_ about integrating with setuptools.



Type Checking
========================================

mypy
------------------------------

.. code-block:: sh

    mypy everywhere



Continuous Integration
========================================

Travis CI
------------------------------

Please visit ``https://travis-ci.org/profile/USERNAME``
to open Travis CI support for your repo.


Documentation
========================================

.. code-block:: sh

    python build_doc.py



Comunication
========================================

Gitter
------------------------------

Please visit ``https://gitter.im/USERNAME#createroom``
to add chat room for your repo.


Code Review
========================================

Code Climate
------------------------------

Please visit ``https://codeclimate.com/github/signup``
to add automated code review for your repo.



.. |python| image:: https://img.shields.io/badge/language-python-blue.svg
   :target: https://www.python.org/

.. |version| image:: https://img.shields.io/pypi/pyversions/python-everywhere.svg
   :target: https://www.python.org/

.. |issues| image:: https://img.shields.io/github/issues/wdv4758h/python-everywhere.svg
   :target: https://github.com/wdv4758h/python-everywhere/issues

.. |travis| image:: https://img.shields.io/travis/wdv4758h/python-everywhere.svg
   :target: https://travis-ci.org/wdv4758h/python-everywhere

.. |gitter| image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/wdv4758h/python-everywhere
   :target: https://gitter.im/wdv4758h/python-everywhere

.. |coveralls| image:: https://coveralls.io/repos/github/wdv4758h/python-everywhere/badge.svg
   :target: https://coveralls.io/github/wdv4758h/python-everywhere

.. |pypi-v| image:: https://img.shields.io/pypi/v/python-everywhere.svg
   :target: https://pypi.python.org/pypi/python-everywhere

.. |pypi-dm| image:: https://img.shields.io/pypi/dm/python-everywhere.svg
   :target: https://pypi.python.org/pypi/python-everywhere

.. |pypi-dd| image:: https://img.shields.io/pypi/dd/python-everywhere.svg
   :target: https://pypi.python.org/pypi/python-everywhere

.. |license| image:: https://img.shields.io/github/license/wdv4758h/python-everywhere.svg
   :target: https://github.com/wdv4758h/python-everywhere/blob/master/LICENSE

.. |code-climate| image:: https://img.shields.io/codeclimate/github/wdv4758h/python-everywhere.svg
   :target: https://codeclimate.com/github/wdv4758h/python-everywhere
