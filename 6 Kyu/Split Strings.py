from itertools import zip_longest
def solution(s):
    return [''.join(a) for a in zip_longest(s[::2], s[1::2], fillvalue='_')]
