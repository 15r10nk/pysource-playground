try:
    match name_3:
        case _ if name_0:
            pass
except* name_3:
    pass
else:
    name_5

# output:
# python: Python/flowgraph.c:511: no_redundant_jumps: Assertion `0' failed.
