#!/usr/bin/python3
"""task 7"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


save_to_json_file(sys.argv, "add_item.json")
print(load_from_json_file("add_item.json"))
