try:
    pass
except* name_2:
    pass
finally:
    if name_3:
        pass
    else:
        pass
name_2 >> name_0

# output:
# python: Python/flowgraph.c:511: no_redundant_jumps: Assertion `0' failed.
