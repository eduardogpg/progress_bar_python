#!/usr/bin/env python
# -*- coding: utf-8 -*-

def print_progress_bar(current=0, total=100, prefix='progress', suffix='completed', length=100, space=' ', fill='█', show_balance=False):
    import sys

    percentage = (current * 100) / total
    progress = int((percentage * length)/100)
    bar =  space * int(length - progress)
    progress = fill * progress

    balance = " ({}/{})".format(current,total) if show_balance else ""
    skip = "\n" if percentage == 100 else ""

    sys.stdout.write("\r{} : |{}{}| {}%{} {}{}".format(prefix, progress, bar, percentage, balance, suffix, skip))
    sys.stdout.flush()
