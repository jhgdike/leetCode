# coding: utf-8

def ugly_qsort(seq):
    if not seq:
        return []
    pivot = seq[0]
    lesser = ugly_qsort([x for x in seq[1:] if x < pivot])
    greater = ugly_qsort([x for x in seq[1:] if x >= pivot])
    return lesser + [pivot] + greater
