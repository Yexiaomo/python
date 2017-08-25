#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    f1 = input('Please enter infile name:').strip()
    f2 = input('Please enter outfile name:').strip()

    infile = open(f1, 'r')
    outfile = open(f2, 'w')

    # copy file content
    countLines = countChars = 0
    for line in infile:
        countLines += 1
        countChars += len(line)
        outfile.write(line)
    print(countLines,'Lines and',countChars,'charscopied')

    infile.close()
    outfile.close()

main()