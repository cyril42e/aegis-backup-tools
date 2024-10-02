#!/bin/env python3

# Usage: [command] | json_to_uri.py
#
# Description:
# This script reads an Aegis Authenticator decrypted json backup file
# from standard input, and outputs a list of otpauth:// URIs on the standard output.
#
# Example:
#   ./decrypt.py backup.json | ./json_to_uri.py
#

import json
import sys

def json_to_otpauth(json_data):
    uris = []
    for entry in json_data.get('entries', []):
        # read parameters
        secret = entry['info']['secret']
        name = entry['name']
        issuer = entry['issuer']
        digits = entry['info']['digits']
        algo = entry['info']['algo']
        period = entry['info']['period']

        # construct otpauth URI
        uri = (f'otpauth://totp/{issuer}:{name}?secret={secret}&issuer={issuer}'
               f'&digits={digits}&algorithm={algo}&period={period}')

        uris.append(uri)

    return uris

if __name__ == "__main__":
    # read json from standard input
    json_data = json.load(sys.stdin)

    otpauth_uris = json_to_otpauth(json_data)

    # Output the list of otpauth URIs to the console
    for uri in otpauth_uris:
        print(uri)
