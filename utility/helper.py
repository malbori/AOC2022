
# convert string to int
def ints(s, sep=None):
    if isinstance(s, str):
        return [int(x) for x in s.split(sep)]
    else:
        return [int(x) for x in s]