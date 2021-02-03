import sys

def to_row(line):
    return list(map(lambda c: c.strip(), line.split(',')))


for [crate, returncode, _] in map(to_row, sys.stdin.readlines()):
    if returncode != '0':
        print(crate, flush=True)
