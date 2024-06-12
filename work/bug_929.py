try:
    pass
except* name_1:
    pass
finally:
    if name_3:
        pass
    else:
        pass
{name_1 for name_2 in name_3}

# output:
# python: Python/flowgraph.c:511: no_redundant_jumps: Assertion `0' failed.
