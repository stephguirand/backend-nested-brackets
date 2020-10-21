#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = """
stephguirand
Help from youtube videos,
stack overflow, google search, Tutors.
"""

import sys

open_b = ['[', '(', '<', '{', '(*']
closed_b = [']', ')', '>', '}', '*)']


def is_nested(line):
    """Validate a single input line for correct nesting"""
    stack = []
    i = 0
    while i < len(line):
        if i+2 < len(line) and line[i: i+2] in open_b:
            stack.append(line[i: i+2])
            i += 1
        elif i + 2 < len(line) and line[i:i+2] in closed_b:
            if len(stack) == 0:
                print("No", i)
                return
            tem = stack.pop()
            if open_b.index(tem) != closed_b.index(line[i:i+2]):
                print("No", i)
                return
            i += 1
        elif line[i] in open_b:
            stack.append(line[i])
        elif line[i] in closed_b:
            if len(stack) == 0:
                print("No", i)
                return
            tem = stack.pop()
            if open_b.index(tem) != closed_b.index(line[i]):
                print("No", i)
                return
        i += 1

    if len(stack) > 0:
        print("No", i)
    else:
        print("Yes")


def read_file(filename):
    with open(filename, 'r') as f:
        for string in f:
            is_nested(string)


def main(args):
    """Open the input file and call `is_nested()` for each line"""
    # Results: print to console and also write to output file
    if len(args) != 2:
        print('usage: python nested.py output.txt')
        # sys.exit(1)
        read_file('input.txt')


if __name__ == '__main__':
    main(sys.argv[1:])
    # main(sys.argv)
