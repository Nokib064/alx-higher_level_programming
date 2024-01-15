#!/usr/bin/env python3
def uppercase(str):
    upp_alph = ""
    for s in str:
        if ord(s) >= 97 and ord(s) <= 122:
            return ord(s) - 32
        #s = str[s] + 1
        upp_alph += "%c"%s
        print("{}".format(upp_alph))
