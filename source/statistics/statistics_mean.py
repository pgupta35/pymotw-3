#!/usr/bin/env python3
# encoding: utf-8
#
"""Arithmetic mean
"""
#end_pymotw_header

import statistics

data = [1, 2, 2, 5, 10, 12]

print('{:0.2f}'.format(statistics.mean(data)))
