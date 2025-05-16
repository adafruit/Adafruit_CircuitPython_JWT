# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

from os import getenv

import adafruit_jwt

# Get private RSA key from a settings.toml file
private_key = getenv("private_key")

# Run jwt_simpletest_secrets.py to generate the private key
if not private_key:
    raise KeyError("Run jwt_simpletest_secrets.py to generate the private key!")

# Sample JWT Claims
claims = {"iss": "joe", "exp": 1300819380, "name": "John Doe", "admin": True}

# Generate a JWT
print("Generating JWT...")
encoded_jwt = adafruit_jwt.JWT.generate(claims, private_key, algo="RS256")
print("Encoded JWT: ", encoded_jwt)

# Validate a provided JWT
print("Decoding JWT...")
decoded_jwt = adafruit_jwt.JWT.validate(encoded_jwt)
print(f"JOSE Header: {decoded_jwt[0]}\nJWT Claims: {decoded_jwt[1]}")
