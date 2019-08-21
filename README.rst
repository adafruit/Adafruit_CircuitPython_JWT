Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-jwt/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/jwt/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

.. image:: https://travis-ci.com/adafruit/Adafruit_CircuitPython_JWT.svg?branch=master
    :target: https://travis-ci.com/adafruit/Adafruit_CircuitPython_JWT
    :alt: Build Status

JSON Web Token (JWT) Authentication module for CircuitPython. JSON Web Tokens are an open, industry standard
`RFC 7519 <https://tools.ietf.org/html/rfc7519>`_ method for representing claims securely between two parties. Module
includes methods for JWT generation and verification.


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Installing from PyPI
=====================
.. note:: This library is not available on PyPI yet. Install documentation is included
   as a standard element. Stay tuned for PyPI availability!

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-jwt/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-jwt

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-jwt

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-jwt

Usage Example
=============

.. todo:: Add a quick, simple example. It and other examples should live in the examples folder and be included in docs/examples.rst.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_JWT/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Sphinx documentation
-----------------------

Sphinx is used to build the documentation based on rST files and comments in the code. First,
install dependencies (feel free to reuse the virtual environment from above):

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install Sphinx sphinx-rtd-theme

Now, once you have the virtual environment activated:

.. code-block:: shell

    cd docs
    sphinx-build -E -W -b html . _build/html

This will output the documentation to ``docs/_build/html``. Open the index.html in your browser to
view them. It will also (due to -W) error out on any warning like Travis will. This is a good way to
locally verify it will pass.
