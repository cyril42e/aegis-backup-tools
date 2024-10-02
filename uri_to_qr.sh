#!/bin/sh

# Usage: [command] | uri_to_qr.sh
#
# Description:
# This script reads a list of otpauth:// URIs from standard input,
# and displays a QR code for each URI (using qrencode and display).
#
# Example:
#   ./decrypt.py backup.json | ./json_to_uri.py | ./uri_to_qr.sh
#
# Requirements:
# - qrencode: A tool to generate QR codes.
# - display: An image viewer (part of ImageMagick) to display the QR codes.

while IFS= read -r uri; do
    # Extract the label (between 'totp/' and '?')
    label=$(echo "$uri" | sed -n 's|.*totp/\([^?]*\).*|\1|p')

    # Display the label
    echo "$label"

    # Generate QR code and display
    echo "$uri" | qrencode -o - | display
done
