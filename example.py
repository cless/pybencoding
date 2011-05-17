#!/usr/bin/python3

import bencoding;

initial = {'Life, the universe and everything': [42, 'forty-two']}

encoded = bencoding.encode(initial)
print(encoded)

decoded = bencoding.decode(encoded)
print(decoded)
