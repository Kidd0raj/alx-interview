#!/usr/bin/env python3
'''A script that reads stdin line by line and computes metrics'''

import sys

def process_line(line, cache, total_size, counter_limit):
    line_list = line.split(" ")
    if len(line_list) > 4:
        code = line_list[-2]
        size = int(line_list[-1])
        if code in cache:
            cache[code] += 1
        total_size += size
        counter_limit -= 1

    return total_size, counter_limit

def print_metrics(cache, total_size):
    print(f'File size: {total_size}')
    for key, value in sorted(cache.items()):
        if value != 0:
            print(f'{key}: {value}')

def main():
    cache = {'200': 0, '301': 0, '400': 0, '401': 0,
             '403': 0, '404': 0, '405': 0, '500': 0}
    total_size = 0
    counter_limit = 10

    try:
        for line in sys.stdin:
            total_size, counter_limit = process_line(line, cache, total_size, counter_limit)
            if counter_limit == 0:
                counter_limit = 10
                print_metrics(cache, total_size)

    except Exception as err:
        # Handle specific exceptions if needed
        pass

    finally:
        print_metrics(cache, total_size)

if __name__ == "__main__":
    main()

