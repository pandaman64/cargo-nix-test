# Run from the root directory

import re
import sys
import subprocess

store_path = re.compile(b'/nix/[^\n]+')

for line in sys.stdin.readlines():
    line = line.strip()
    proc = subprocess.run(['cargo-nix', '-n', 'nix/nixpkgs.nix', line], stdout=subprocess.PIPE)
    result = store_path.search(proc.stdout)
    if result is not None:
        print(line, proc.returncode, result.group(0).decode(encoding='utf-8'), sep=',', flush=True)
    else:
        print(line, proc.returncode, '', sep=',', flush=True)
