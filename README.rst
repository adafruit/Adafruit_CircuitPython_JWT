Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-jwt/badge/?version=latest
    :target: https://docs.circuitpython.org/projects/jwt/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_JWT/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_JWT/actions/
    :alt: Build Status

JSON Web Token (JWT) Authentication module for CircuitPython. JSON Web Tokens are an open, industry standard
`RFC 7519 <https://tools.ietf.org/html/rfc7519>`_ method for representing claims securely between two parties.

This library currently supports the following signature algorithms for JWT generation and verification:
 * No encoding ("none")
 * RS256/SHA-256 (via `Adafruit_CircuitPython_RSA <https://github.com/adafruit/Adafruit_CircuitPython_RSA>`_)
 * RS384/SHA-384 (via `Adafruit_CircuitPython_RSA <https://github.com/adafruit/Adafruit_CircuitPython_RSA>`_)
 * RS512/SHA-512 (via `Adafruit_CircuitPython_RSA <https://github.com/adafruit/Adafruit_CircuitPython_RSA>`_)

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Adafruit_CircuitPython_RSA <https://github.com/adafruit/Adafruit_CircuitPython_RSA>`_
* `Adafruit_CircuitPython_binascii <https://github.com/adafruit/Adafruit_CircuitPython_binascii>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Installing from PyPI
=====================
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

Generating encoded JWT

.. code-block:: python

        import adafruit_jwt
        # Import Private RSA key from a secrets.py file
        try:
            from secrets import secrets
        except ImportError:
            print("WiFi secrets are kept in secrets.py, please add them there!")
            raise

        # Create JWT Claims
        claims = {"iss": "joe",
                "exp": 1300819380,
                "name": "John Doe",
                "admin": True}

        # Generate JWT, sign with RSA private key and RS-256
        encoded_jwt = adafruit_jwt.JWT.generate(
            claims, secrets["private_key"], algo="RS256")
        print("Encoded JWT: ", encoded_jwt)


Validating a generated JWT, encoded_jwt.

.. code-block:: python

        import adafruit_jwt
        decoded_jwt = adafruit_jwt.JWT.validate(encoded_jwt)
        # The decoded JWT's JOSE header and claims set are returned as a tuple
        print('JOSE Header: {}\nJWT Claims: {}'.format(decoded_jwt[0], decoded_jwt[1]))

Documentation
=============

API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/jwt/en/latest/>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_JWT/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
