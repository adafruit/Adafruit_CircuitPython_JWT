# The MIT License (MIT)
#
# Copyright (c) 2019 Brent Rubell for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`adafruit_jwt`
================================================================================

JSON Web Token Authentication

* Author(s): Brent Rubell

Implementation Notes
--------------------

**Hardware:**

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

* Adafruit's RSA library:
  https://github.com/adafruit/Adafruit_CircuitPython_RSA
"""
import io
import json
from adafruit_rsa import PrivateKey, sign

from adafruit_binascii import b2a_base64, a2b_base64

import string

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_JWT.git"

# pylint: disable=no-member
class JWT:
    """JSON Web Token helper for CircuitPython. Warning: JWTs are
    credentials, which can grant access to resources. Be careful
    where you paste them!
    :param str algo: Encryption algorithm used for claims. Can be None.

    """

    @staticmethod
    def validate(jwt):
        """Validates a provided JWT. Does not support nested signing.
        :param str jwt: JSON Web Token.
        :returns: The message's decoded JOSE header and claims.
        :rtype: tuple
        """
        # Verify JWT contains at least one period ('.')
        if jwt.find(".") == -1:
            raise ValueError("JWT must have at least one period")
        # Separate the encoded JOSE Header
        jose_header = jwt.split(".")[0]
        # Decode JOSE Header
        try:
            jose_header = STRING_TOOLS.urlsafe_b64decode(jose_header)
        except UnicodeError:
            raise UnicodeError("Invalid JOSE Header encoding.")
        if "type" not in jose_header:
            raise TypeError("JOSE Header does not contain required type key.")
        if "alg" not in jose_header:
            raise TypeError("Jose Header does not contain required alg key.")
        # Separate encoded claim set
        claims = jwt.split(".")[1]
        try:
            claims = json.loads(STRING_TOOLS.urlsafe_b64decode(claims))
        except UnicodeError:
            raise UnicodeError("Invalid claims encoding.")
        if not hasattr(claims, "keys"):
            raise TypeError("Provided claims is not a JSON dict. object")
        return (jose_header, claims)


    @staticmethod
    def generate(claims, private_key_data=None, algo=None):
        """Generates and returns a new JSON Web Token.
        :param dict claims: JWT claims set
        :param str private_key_data: Decoded RSA private key data.
        :rtype: str
        """
        # Allow for unencrypted JWTs
        if algo is not None:
            priv_key = PrivateKey(*private_key_data)
        else:
            algo = "none"
        # Create the JOSE Header
        # https://tools.ietf.org/html/rfc7519#section-5
        jose_header = {"typ": "JWT", "alg": algo}
        payload = "{}.{}".format(
            string.b42_urlsafe_encode(json.dumps(jose_header).encode("utf-8")),
            string.b42_urlsafe_encode(json.dumps(claims).encode("utf-8")),
        )
        # Compute the signature
        if algo == "none":
            jwt = "{}.{}".format(jose_header, claims)
        elif algo == "RS256" or algo == "RS384" or algo == "RS512" or algo == "RSA":
            #sig = sign(payload, priv_key, "SHA-256")
            signature = string.b42_urlsafe_encode(sign(payload, priv_key, "SHA-256"))
            jwt = payload + "." + signature
        else:
            raise TypeError(
                "Adafruit_JWT is currently only compatible with algorithms within"
                "the Adafruit_RSA module."
            )
        return jwt


# pylint: disable=invalid-name
class STRING_TOOLS:
    """Tools and helpers for URL-safe string encoding.
    """
    # Some strings for ctype-style character classification
    whitespace = " \t\n\r\v\f"
    ascii_lowercase = "abcdefghijklmnopqrstuvwxyz"
    ascii_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ascii_letters = ascii_lowercase + ascii_uppercase
    digits = "0123456789"
    hexdigits = digits + "abcdef" + "ABCDEF"
    octdigits = "01234567"
    punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    printable = digits + ascii_letters + punctuation + whitespace

    @staticmethod
    def urlsafe_b64encode(payload):
        """Encode bytes-like object using the URL- and filesystem-safe alphabet,
        which substitutes - instead of + and _ instead of / in
        the standard Base64 alphabet, and return the encoded bytes.
        :param bytes payload: bytes-like object.
        """
        return STRING_TOOLS.translate(
            b2a_base64(payload)[:-1].decode("utf-8"), {ord("+"): "-", ord("/"): "_"}
        )

    @staticmethod
    def urlsafe_b64decode(payload):
        """Decode bytes-like object or ASCII string using the URL
        and filesystem-safe alphabet
        :param bytes payload: bytes-like object or ASCII string
        """
        return a2b_base64(STRING_TOOLS._bytes_from_decode_data(payload)).decode("utf-8")

    @staticmethod
    def _bytes_from_decode_data(str_data):
        # Types acceptable as binary data
        bit_types = (bytes, bytearray)
        if isinstance(str_data, str):
            try:
                return str_data.encode("ascii")
            except:
                raise ValueError("string argument should contain only ASCII characters")
        elif isinstance(str_data, bit_types):
            return str_data
        else:
            raise TypeError(
                "argument should be bytes or ASCII string, not %s"
                % str_data.__class__.__name__
            )

    # Port of CPython str.translate to Pure-Python by Johan Brichau, 2019
    # https://github.com/jbrichau/TrackingPrototype/blob/master/Device/lib/string.py
    @staticmethod
    def translate(s, table):
        """Return a copy of the string in which each character
        has been mapped through the given translation table.
        :param string s: String to-be-character-table.
        :param dict table: Translation table.
        """
        sb = io.StringIO()
        for c in s:
            v = ord(c)
            if v in table:
                v = table[v]
                if isinstance(v, int):
                    sb.write(chr(v))
                elif v is not None:
                    sb.write(v)
            else:
                sb.write(c)
        return sb.getvalue()
