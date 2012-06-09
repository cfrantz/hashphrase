#!/usr/bin/python

# Generate word list from Project Gutenburgs "Moby Word Lists" COMMON.TXT

# accept all words that don't have builtin punctuation marks and are 4 to 8 characters long

import json
import re
import sys

def words(fn):
	wlist = []
	f = file(fn)
	for line in f:
		line = line.strip()
		m = re.search(r'[^a-zA-Z]', line)

		if not m and 4<=len(line)<=8:
			wlist.append(line)

	f.close()
	return wlist


if __name__ == '__main__':
	wlist = words(sys.argv[1])
	with file(sys.argv[2], 'w') as f:
		f.write("var wordlist = ")
		json.dump(wlist, f, indent=0)
