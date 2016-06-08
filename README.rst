========================================
python-everywhere
========================================

|issues|
|travis|
|coveralls|
|pypi-dm|
|gitter|


Inspired by `rust-everywhere <https://github.com/japaric/rust-everywhere>`_.


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


Gitter
========================================

Please visit ``https://gitter.im/USERNAME#createroom``
to add chat room for your repo.


.. |issues| image:: https://img.shields.io/github/issues/wdv4758h/python-everywhere.svg
   :target: https://github.com/wdv4758h/python-everywhere/issues

.. |travis| image:: https://img.shields.io/travis/wdv4758h/python-everywhere.svg
   :target: https://travis-ci.org/wdv4758h/python-everywhere

.. |gitter| image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/wdv4758h/python-everywhere
   :target: https://gitter.im/wdv4758h/python-everywhere

.. |coveralls| image:: https://coveralls.io/repos/github/wdv4758h/python-everywhere/badge.svg
   :target: https://coveralls.io/github/wdv4758h/python-everywhere

.. |pypi-dm| image:: https://img.shields.io/pypi/dm/python-everywhere.svg
   :target: https://pypi.python.org/pypi/python-everywhere
