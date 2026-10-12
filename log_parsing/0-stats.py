#!/usr/bin/python3
"""Log parsing."""

import sys


def print_stats(size, codes):
    """Print statistics."""
    print("File size: {}".format(size))
    for code in sorted(codes):
        if codes[code] > 0:
            print("{}: {}".format(code, codes[code]))


def main():
    """Read stdin and calculate metrics."""
    size = 0
    count = 0
    codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }

    try:
        for line in sys.stdin:
            count += 1
            parts = line.split()

            try:
                size += int(parts[-1])
            except (ValueError, IndexError):
                pass

            try:
                if parts[-2] in codes:
                    codes[parts[-2]] += 1
            except IndexError:
                pass

            if count % 10 == 0:
                print_stats(size, codes)

    except KeyboardInterrupt:
        print_stats(size, codes)
        raise

    if count == 0 or count % 10 != 0:
        print_stats(size, codes)


if __name__ == "__main__":
    main()
