def longest(a, b):
    return "".join(sorted(set(a)|set(b)-set(a)&set(b)))
