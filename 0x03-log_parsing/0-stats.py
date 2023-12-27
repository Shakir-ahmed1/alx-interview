#!/usr/bin/python3

"""
Write a script that reads stdin line by line and computes metrics
"""
import re
from sys import stdin

counter = 1
size_list = []
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                '404': 0, '405': 0, '500': 0}
try:
    for line in stdin:
        valid_line = re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - '
                              r'\[.+\] "GET \/projects\/260 HTTP\/1.1"'
                              r' (\d+) (\d+)', line)

        if not valid_line:
            continue
        size_list.append(int(valid_line.group(2)))
        status_codes[valid_line.group(1)] += 1
        if counter % 10 == 0:
            total_file_size = sum(size_list)
            print(f"File size: {total_file_size}")
            for st in sorted(status_codes):
                if status_codes[st] != 0:
                    print(f"{st}: {status_codes[st]}")
        counter += 1


except KeyboardInterrupt:
    pass
finally:
    total_file_size = sum(size_list)
    print(f"File size: {total_file_size}")
    for st in sorted(status_codes):
        if status_codes[st] != 0:
            print(f"{st}: {status_codes[st]}")
