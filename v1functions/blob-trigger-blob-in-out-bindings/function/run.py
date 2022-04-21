# -*- coding: utf-8 -*-

"""

Azure Functions Blob Trigger Python Sample
- Simple reading file from Azure Blob Storage and write an output file to Azure Blob Storage

"""


import os

with open(os.environ['inputBlob'], 'r') as input_file:
    clear_text = input_file.read()
# Encrypt text with ROT13 encryption
encrypted_text= clear_text.decode('rot13')

with open(os.environ['outputBlob'], 'w') as output_file:
    output_file.write(encrypted_text)

