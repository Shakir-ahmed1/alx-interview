#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics
"""
import re
from sys import stdin

counter = 1
size_list = []
status_codes = {'200': 0,'301': 0, '400': 0, '401': 0, '403': 0,
                '404': 0, '405': 0,'500': 0}
try:
    for line in stdin:
        valid_line = re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - '
                              r'\[.+\] "GET \/projects\/260 HTTP\/1.1"'
                              r' (\d{3}) (\d+)', line)

        if not valid_line:
            continue
        status_code = re.group(1)

        file_size = re.group(2)
        size_list.append(int(file_size))

        if counter % 10 == 0:
            total_file_size = sum(size_list)
            print(f"File size: {total_file_size}")
            for st in sorted(status_codes):
                if status_codes[st] != 0:
                    print(f"{st}: {status_codes[st]}")
        counter += 1


except Exception:
    pass
finally:
    total_file_size = sum(size_list)
    print(f"File size: {total_file_size}")
    for st in sorted(status_codes):
        if status_codes[st] != 0:
            print(f"{st}: {status_codes[st]}")
