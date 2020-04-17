#!/usr/bin/env python

import sys

for fn in sys.argv[1:]:
    try:
        f = open(fn)
    except FileNotFoundError:
        print("{}というファイルは存在しません".format(fn))
    else:
        try:
            print(fn, len(f.read()))
        finally:
            f.close()
