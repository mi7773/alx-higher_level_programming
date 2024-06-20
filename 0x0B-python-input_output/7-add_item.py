#!/usr/bin/python3

"""
7-add_item module.
"""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    saved = load_from_json_file('add_items.json')
except Exception as e:
    saved = []

for i in sys.argv:
    if i == sys.argv[0]:
        pass
    else:
        saved.append(i)

save_to_json_file(saved, 'add_items.json')
